# LNbits OpenSats Grant June - August

LNbits will be going V1 in Q4 2024. This would not ave been possible without the support from OpenSats❤️.

## August
#### LNbits core
* feat: add boltz client fundingsource by @dni in https://github.com/lnbits/lnbits/pull/2358
* feat: NWC Funding source #2579  by @riccardobl in https://github.com/lnbits/lnbits/pull/2631
* refactor: add status column to apipayments by @dni in https://github.com/lnbits/lnbits/pull/2537
* chore: bump version to 0.12.11 by @dni in https://github.com/lnbits/lnbits/pull/2601
* bug: removing admin user was not persistent by @dni in https://github.com/lnbits/lnbits/pull/2603
* feat: add `exclude_to` list for btcprice providers by @dni in https://github.com/lnbits/lnbits/pull/2602
* feat: add a copy wallet button by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2613
* Update installation.md by @blackcoffeexbt in https://github.com/lnbits/lnbits/pull/2615
* feat: extra log for tests phases by @dni in https://github.com/lnbits/lnbits/pull/2604
* test: fix flaky regtest by @dni in https://github.com/lnbits/lnbits/pull/2616
* fix: random exceptions in logs in middleware by @dni in https://github.com/lnbits/lnbits/pull/2608
* fix: still flaky regtest by @dni in https://github.com/lnbits/lnbits/pull/2617
* feat: filter response fields for `/api/v1/payments/decode` by @motorina0 in https://github.com/lnbits/lnbits/pull/2612
* fix: skip pending payment check on void by @dni in https://github.com/lnbits/lnbits/pull/2610
* Set a maximium sleep time when retrying to connect to the funding source by @blackcoffeexbt in https://github.com/lnbits/lnbits/pull/2622
* feat: add release flow for release candidates by @dni in https://github.com/lnbits/lnbits/pull/2620
* Invoice creation UI: Replace input mask with pattern and inputmode by @blackcoffeexbt in https://github.com/lnbits/lnbits/pull/2623
* fix: db helpers to be used with timestamps by @dni in https://github.com/lnbits/lnbits/pull/2627
* feat: add typing for tasks by @dni in https://github.com/lnbits/lnbits/pull/2629
* test: refactor to not use paid_invoices stream for real invoice tests by @dni in https://github.com/lnbits/lnbits/pull/2628
* feat: use __all__ to export deps from `__init__.py` by @dni in https://github.com/lnbits/lnbits/pull/2630
* fix: export nwc wallet by @dni in https://github.com/lnbits/lnbits/pull/2632
* fix: add back lnurl wallet by @dni in https://github.com/lnbits/lnbits/pull/2625
* feat: add label to `lnbits-dynamic-fields` by @dni in https://github.com/lnbits/lnbits/pull/2637
* add copy buttons by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2643
* feat: add rate endpoint per currency by @dni in https://github.com/lnbits/lnbits/pull/2641
* show wallet names in dropdown by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2653
* feat: add generic lnurl error response handler by @dni in https://github.com/lnbits/lnbits/pull/2638
* Fix documentation on decode API by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2655
* fix chips on server page by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2654
* feat: log with `console.error` on `notifyApiError` by @dni in https://github.com/lnbits/lnbits/pull/2646
* Fix lnurl fallback by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2656
* feat: vue components lnbits-dynamic-fields validation by @dni in https://github.com/lnbits/lnbits/pull/2645
* feat: frontend gradient option by @arcbtc in https://github.com/lnbits/lnbits/pull/2561
* refactor: move migrate_databases to core helpers by @dni in https://github.com/lnbits/lnbits/pull/2636
* Uncomment LNBITS_ALLOWED_FUNDING_SOURCES by @arcbtc in https://github.com/lnbits/lnbits/pull/2663
* feat: add baseurl to admin ui settings by @dni in https://github.com/lnbits/lnbits/pull/2644
* fix: regeression on index.html by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2665
* fix: update lnurl for backwards compatibility by @dni in https://github.com/lnbits/lnbits/pull/2666
* fix: QR request case by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2668
* Add detailed CSV export option by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2618
#### Boltz ext
* fix: date issues and some new api fields by @dni in https://github.com/lnbits/boltz/pull/40
#### NostrNip05 ext
* Ln address by @motorina0 in https://github.com/lnbits/nostrnip5/pull/13
#### LNURLp ext
* fix: parsing url by @dni in https://github.com/lnbits/lnurlp/pull/62
* fix: nostr zaps by @motorina0 in https://github.com/lnbits/lnurlp/pull/63
#### LNticket ext
* Added extended description by @arcbtc in https://github.com/lnbits/lnticket/pull/10
* feat: code quality by @dni in https://github.com/lnbits/lnticket/pull/11
* fix words not counting by @talvasconcelos in https://github.com/lnbits/lnticket/pull/8
* fix: dont use set_pending by @dni in https://github.com/lnbits/lnticket/pull/12
#### Satspay ext
* Added advanced description by @arcbtc in https://github.com/lnbits/satspay/pull/41
* Fixed video link by @arcbtc in https://github.com/lnbits/satspay/pull/42
* feat: code quality by @dni in https://github.com/lnbits/satspay/pull/43
* fix: show BTC instead of sats for onchain by @motorina0 in https://github.com/lnbits/satspay/pull/47
* fix: custom css was not working by @dni in https://github.com/lnbits/satspay/pull/44
* feat: mempool listener on backend by @dni in https://github.com/lnbits/satspay/pull/46
* fix: make newlines in description possible by @dni in https://github.com/lnbits/satspay/pull/48
* feat: add fiat amount to create charge endpoint by @dni in https://github.com/lnbits/satspay/pull/49
* fix: localhost for websocket by @dni in https://github.com/lnbits/satspay/pull/50
* fix: progress on public and admin page by @dni in https://github.com/lnbits/satspay/pull/51
* fix: charge frontend with zeroconf = false by @dni in https://github.com/lnbits/satspay/pull/53
* fix: add expired tag to charge list by @dni in https://github.com/lnbits/satspay/pull/52
* feat: add check balance endpoint an button for admin by @dni in https://github.com/lnbits/satspay/pull/54
* fix: paid status on charge endpoint and persist paid into db by @dni in https://github.com/lnbits/satspay/pull/55
* feat: fix webhook for woocomerce and pending amount after refresh by @dni in https://github.com/lnbits/satspay/pull/56
* fix: update_charge on postgres failed by @dni in https://github.com/lnbits/satspay/pull/57
* feat: always send webhook on balance update by @dni in https://github.com/lnbits/satspay/pull/58
* feat: make extra more versatile and use satspay config instead of onchainwallet config by @dni in https://github.com/lnbits/satspay/pull/59
* fix: restart websocket handler when mempool endpoint changes by @dni in https://github.com/lnbits/satspay/pull/60
#### myextension ext
* big refactor to extension template by @benarc in https://github.com/lnbits/myextension
#### lnbits-extensions 
* feat: max_lnbits_version for older releases by @dni in https://github.com/lnbits/lnbits-extensions/pull/397
* Reviews:
    - nostrnip05 ext https://github.com/lnbits/lnbits-extensions/pull/398
    - Boltz ext https://github.com/lnbits/lnbits-extensions/pull/396
    - Boltz ext https://github.com/lnbits/lnbits-extensions/pull/394
    - Discordbot ext https://github.com/lnbits/lnbits-extensions/pull/393
#### Content
* LNbits overview videos by @arcbtc https://www.youtube.com/watch?v=b7Ou7XtqtRI, https://www.youtube.com/watch?v=ymq_BXN4lu0, https://www.youtube.com/watch?v=LMs4bFrvy_Y, https://www.youtube.com/watch?v=b1a5XshX5dA


## July

#### LNbits core
* Nice formatting of funding source titles in Server admin by @blackcoffeexbt in https://github.com/lnbits/lnbits/pull/2543
* Fix typo of "LNbits" in list of funding sources. by @blackcoffeexbt in https://github.com/lnbits/lnbits/pull/2546
* fix: npm packages with high severity issue by @dni in https://github.com/lnbits/lnbits/pull/2551
* [feat] Extension details page by @motorina0 in https://github.com/lnbits/lnbits/pull/2544
* chore: prepare for `0.12.9` by @dni in https://github.com/lnbits/lnbits/pull/2555
* feat: improve on extension page layout by @dni in https://github.com/lnbits/lnbits/pull/2558
* bug: carousel and adv desc fix by @arcbtc in https://github.com/lnbits/lnbits/pull/2562
* [feat] add `authenticated_user_id` decorator by @motorina0 in https://github.com/lnbits/lnbits/pull/2566
* [feat] add `default_user_extensions` setting by @motorina0 in https://github.com/lnbits/lnbits/pull/2571
* docs: nginx websocket support for reverse proxy by @dni in https://github.com/lnbits/lnbits/pull/2564
* Fixed ugly adv description card by @arcbtc in https://github.com/lnbits/lnbits/pull/2570
* fix: lib secp256k fails building by @dni in https://github.com/lnbits/lnbits/pull/2572
* fix: always create default wallet for user by @motorina0 in https://github.com/lnbits/lnbits/pull/2580
#### Boltz ext
* fix: could not save settings, db migration remove mempool by @dni in https://github.com/lnbits/boltz/pull/37
* fix: make migration work on odler sqlite versions by @dni in https://github.com/lnbits/boltz/pull/39
#### LNcalender ext
* Delete unavailable dates by @talvasconcelos in https://github.com/lnbits/lncalendar/pull/8
#### Withdraw ext
* chore: change extension name by @talvasconcelos in https://github.com/lnbits/withdraw/pull/32
* Adds extended description by @arcbtc in https://github.com/lnbits/withdraw/pull/33
* Added extended description by @arcbtc in https://github.com/lnbits/withdraw/pull/34
* feat: add linters and ci by @dni in https://github.com/lnbits/withdraw/pull/28
* fix: return 200 status for lnurl errors and fix uniques by @dni in https://github.com/lnbits/withdraw/pull/43
#### LNDHub ext
* refactor: prepare lndhub for next release by @dni in https://github.com/lnbits/lndhub/pull/32
#### Eightball ext 
* Eightball ext created by @arcbtc in https://github.com/lnbits/eightball
#### lnbits-extensions
* ci update by @dni in https://github.com/lnbits/lnbits-extensions/pull/387
* Exension page updates by @dni in https://github.com/lnbits/lnbits-extensions/pull/382, https://github.com/lnbits/lnbits-extensions/pull/379
* Change featured by @dni in https://github.com/lnbits/lnbits-extensions/pull/376
* Remove market ext by @arcbtc in https://github.com/lnbits/lnbits-extensions/pull/355
* Reviews:
    - lndhub ext https://github.com/lnbits/lnbits-extensions/pull/389
    - Withdraw ext https://github.com/lnbits/lnbits-extensions/pull/388
    - Withdraw ext https://github.com/lnbits/lnbits-extensions/pull/385
    - LNcalendar ext https://github.com/lnbits/lnbits-extensions/pull/384
    - Boltz ext https://github.com/lnbits/lnbits-extensions/pull/380, https://github.com/lnbits/lnbits-extensions/pull/378, https://github.com/lnbits/lnbits-extensions/pull/373, https://github.com/lnbits/lnbits-extensions/pull/391
    - Nostrnip05 ext https://github.com/lnbits/lnbits-extensions/pull/372

## June
#### LNbits Core
* [feat] Extension details page by @motorina0 in https://github.com/lnbits/lnbits/pull/2544
* [fix]: npm packages with high severity issue by @dni in https://github.com/lnbits/lnbits/pull/2551
* [feat] Nice formatting of funding source titles in Server admin by @blackcoffeexbt in https://github.com/lnbits/lnbits/pull/2543
* [fix] typo of "LNbits" in list of funding sources. by @blackcoffeexbt in https://github.com/lnbits/lnbits/pull/2546
* [chore] prepare for `0.12.9` by @dni in https://github.com/lnbits/lnbits/pull/2555
#### Boltz ext
* Added extended description by @arcbtc in https://github.com/lnbits/boltz/pull/31
* feat: codequality, linters and ci by @dni in https://github.com/lnbits/boltz/pull/32
* chore: change to new slogan by @dni in https://github.com/lnbits/boltz/pull/34
* feat: Small UI fixes by @dni in https://github.com/lnbits/boltz/pull/33
* fix: autoswap service fee by @dni in https://github.com/lnbits/boltz/pull/35
#### NostrNip05 ext
* Added advanced description by @arcbtc in https://github.com/lnbits/nostrnip5/pull/5
#### Content 
* Extension building tutorial by @arcbtc https://www.youtube.com/watch?v=zHXLvvjClHI
* Poweruser videos by @arcbtc https://www.youtube.com/watch?v=oiXMADI1nmM, https://www.youtube.com/watch?v=a6bimcQC2pw, https://www.youtube.com/watch?v=5eFATj2vFP8, https://www.youtube.com/watch?v=46aHKk8cLfg
#### General expenses
* Ben Arc, DNI, Vlad Stand trip to BTCPrague
## Additional
General daily support for repo issues in LNbits, extensions, hardware, as well as support in the telegram groups https://t.me/lnbits, https://t.me/makerbits, https://t.me/nostrmarkets
