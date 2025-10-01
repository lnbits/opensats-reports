#!/usr/bin/env python3
"""
List GitHub repos in an org that had commits between two dates (inclusive).

Usage:
  ./find_repos_worked_on.py <org_or_org_url> <since YYYY-MM-DD> <until YYYY-MM-DD>

Auth (recommended to avoid low rate limits):
  export GITHUB_TOKEN=ghp_xxx   # or rely on `gh auth token` if you use GitHub CLI
"""
import os, sys, time, json, re, urllib.parse, urllib.request
from datetime import datetime

API = "https://api.github.com/search/commits"
PER_PAGE = 100
MAX_RESULTS = 1000  # GitHub search hard cap

def parse_org(arg: str) -> str:
    # Accept "lnbits" or "https://github.com/lnbits"
    if re.match(r'https?://', arg):
        parts = urllib.parse.urlparse(arg)
        # Expect path like /ORG or /ORG?tab=repositories etc.
        segs = [s for s in parts.path.split('/') if s]
        if not segs:
            raise ValueError("Could not parse org from URL. Try just the org name, e.g. 'lnbits'.")
        return segs[0]
    return arg

def check_date(s: str) -> str:
    # Accept YYYY-MM-DD; raise if malformed
    datetime.strptime(s, "%Y-%m-%d")
    return s

def gh_token():
    tok = os.environ.get("GITHUB_TOKEN")
    if tok:
        return tok
    try:
        import subprocess
        out = subprocess.check_output(["gh","auth","token"], text=True).strip()
        return out or None
    except Exception:
        return None

def http_get(url: str, headers: dict, retry: int = 3):
    for attempt in range(retry):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as r:
                data = r.read()
                return data, r.headers
        except urllib.error.HTTPError as e:
            # Respect secondary rate limiting: 403 + Retry-After
            if e.code in (403, 429):
                ra = e.headers.get("Retry-After")
                if ra:
                    time.sleep(int(ra))
                    continue
            # Bubble up other errors
            raise
        except urllib.error.URLError:
            time.sleep(1)
    raise RuntimeError(f"Failed to GET {url} after retries")

#!/usr/bin/env python3
# ... (same imports and functions as before) ...

def main():
    if len(sys.argv) != 4:
        print("Usage: find_repos_worked_on.py <org_or_org_url> <since YYYY-MM-DD> <until YYYY-MM-DD>", file=sys.stderr)
        sys.exit(2)

    org = parse_org(sys.argv[1])
    since = check_date(sys.argv[2])
    until = check_date(sys.argv[3])

    token = gh_token()
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "find-repos-worked/1.2",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    q = f'org:{org} committer-date:{since}..{until}'
    repos = set()
    fetched = 0
    page = 1

    while True:
        params = {
            "q": q,
            "per_page": str(PER_PAGE),
            "page": str(page),
        }
        url = f"{API}?{urllib.parse.urlencode(params)}"
        body, hdrs = http_get(url, headers)
        obj = json.loads(body.decode("utf-8"))
        items = obj.get("items", [])
        if not items:
            break

        for it in items:
            repo = it.get("repository") or {}
            full = repo.get("full_name")
            if full:
                repos.add(full)

        fetched += len(items)
        total = obj.get("total_count", 0)
        if fetched >= min(MAX_RESULTS, total):
            break
        page += 1
        if not token:
            time.sleep(1)

    # Print formatted links
    for name in sorted(repos, key=str.lower):
        print(f"* https://github.com/{name}/commits?since={since}&until={until}")

if __name__ == "__main__":
    main()