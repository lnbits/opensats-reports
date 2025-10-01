#!/usr/bin/env bash
# Usage: ./generate_commits.sh "https://github.com/owner/repo" "YYYY-MM-DD" "YYYY-MM-DD"
set -euo pipefail

if ! command -v git >/dev/null 2>&1; then
  echo "git is required" >&2
  exit 1
fi

PYTHON_BIN="${PYTHON_BIN:-python3}"
if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
  echo "python3 is required" >&2
  exit 1
fi

if [ $# -ne 3 ]; then
  echo "Expected 3 args: <repo_url> <since YYYY-MM-DD> <until YYYY-MM-DD>" >&2
  exit 1
fi

REPO_URL="$1"
SINCE="$2"
UNTIL="$3"

WORKDIR="$(mktemp -d -t commits-XXXXXX)"
trap 'rm -rf "$WORKDIR"' EXIT
REPO_DIR="$WORKDIR/repo"

# Partial clone for speed; fallback if not supported
if git clone --quiet --filter=blob:none --no-checkout "$REPO_URL" "$REPO_DIR" 2>/dev/null; then
  :
else
  git clone --quiet "$REPO_URL" "$REPO_DIR"
fi
git -C "$REPO_DIR" fetch --all --tags --quiet

"$PYTHON_BIN" - "$REPO_DIR" "$REPO_URL" "$SINCE" "$UNTIL" <<'PY'
import subprocess, sys, datetime, re
from collections import defaultdict

repo_dir, repo_url, since, until = sys.argv[1:]

def to_https_base(url: str) -> str:
    url = url.strip()
    if url.startswith(("http://","https://")):
        return re.sub(r"\.git$","",url)
    m = re.match(r"git@github\.com:(.+?)(?:\.git)?$", url)
    if m:
        return "https://github.com/" + m.group(1)
    url = re.sub(r"\.git$","",url)
    if not url.startswith("http"):
        url = "https://github.com/" + url.lstrip("/")
    return url

base_url = to_https_base(repo_url)

# Use separate argv tokens for date values (no '='), to avoid parsing quirks.
fmt = "%H%x1f%ad%x1f%an%x1f%s%x1e"
cmd = [
    "git","-C",repo_dir,"log",
    "--since", f"{since} 00:00:00",
    "--until", f"{until} 23:59:59",
    "--date=short",
    f"--pretty=format:{fmt}",
    "--all",
]
out = subprocess.check_output(cmd, text=True, errors="replace")

records = [r for r in out.split("\x1e") if r.strip()]

seen = set()
commits = []
for rec in records:
    parts = rec.split("\x1f")
    if len(parts) != 4:
        continue
    full_hash, date_str, author, subject = parts
    if full_hash in seen:  # simple dedupe
        continue
    seen.add(full_hash)
    commits.append({
        "hash": full_hash,
        "short": full_hash[:8],
        "date": date_str,  # YYYY-MM-DD
        "author": author,
        "subject": subject.strip(),
    })

# Group by (year, month) ascending; keep git order (newest-first) inside month.
grouped = defaultdict(list)
month_keys = set()
for c in commits:
    y, m, _ = map(int, c["date"].split("-"))
    grouped[(y,m)].append(c)
    month_keys.add((y,m))

for (year, month) in sorted(month_keys):
    month_name = datetime.date(year, month, 1).strftime("%B")
    print(f"#### {month_name} {year}\n")
    for c in grouped[(year, month)]:
        link = f'{base_url}/commit/{c["hash"]}'
        print(f'<a href="{link}">{c["short"]}</a> {c["date"]} | {c["author"]} | {c["subject"]}</br>')
    print()
PY
