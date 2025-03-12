# LNbits OpenSats Grant December 2024 - Febuary 2025

LNbits is almost at v1. This would not have been possible without the support from OpenSats❤️.

## LNbits core
#### Dec 2024
* [feat] install extensions from dir by @motorina0 in https://github.com/lnbits/lnbits/pull/2781
* chore: update to v1.0.0-rc6 by @dni in https://github.com/lnbits/lnbits/pull/2784
* chore: add type to migration by @dni in https://github.com/lnbits/lnbits/pull/2788
* chore: remove ignores from crypto.py by @dni in https://github.com/lnbits/lnbits/pull/2787
* chore: use HTTPStatus for ip middleware by @dni in https://github.com/lnbits/lnbits/pull/2792
* [fix] wallet search on postgres by @motorina0 in https://github.com/lnbits/lnbits/pull/2780
* feat: add failed payments toggle to wallet page by @dni in https://github.com/lnbits/lnbits/pull/2794
* fix: last_payment on userlist was broken by @dni in https://github.com/lnbits/lnbits/pull/2796
* chore: clean up javascript functions and var/let into const by @dni in https://github.com/lnbits/lnbits/pull/2791
* test: update python to 3.10 and 3.11 inside CI by @dni in https://github.com/lnbits/lnbits/pull/2803
* test: update ci from ubuntu-latest to ubuntu-24.04 by @dni in https://github.com/lnbits/lnbits/pull/2809
* chore: update to latest pytest by @dni in https://github.com/lnbits/lnbits/pull/2800
* fix: extension init by @motorina0 in https://github.com/lnbits/lnbits/pull/2815
* fix: error on custom badge by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2814
* test: fix lndrest on regtest by @dni in https://github.com/lnbits/lnbits/pull/2811
* fix: ext upgrade from `lnbits-cli` by @motorina0 in https://github.com/lnbits/lnbits/pull/2822https://github.com/lnbits/lnbits/pull/2834
* fix: wallet.js regression in changing var` to `const` by @dni in https://github.com/lnbits/lnbits/pull/2824
* test: fix jmeter for ci by @dni in https://github.com/lnbits/lnbits/pull/2825
* [feat] custom exchange providers by @motorina0 in https://github.com/lnbits/lnbits/pull/2797
* feat: return the price with the fiat rate by @motorina0 in https://github.com/lnbits/lnbits/pull/2823
* fix: remove queue limit for invoice listners by @dni in https://github.com/lnbits/lnbits/pull/2829
* fix: make startup extension check sync by @dni in https://github.com/lnbits/lnbits/pull/2819
* fix: don't show when custom badge is not set by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2827
* feat: websocket for payments events, remove /payments/sse and longpolling endpoint by @dni in https://github.com/lnbits/lnbits/pull/2704
* [feat] update multiple extensions from the UI by @motorina0 in https://github.com/lnbits/lnbits/pull/2833
* hotfix: the hotfix for the custom badge by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2832
* [feat] introduce `max_lnbits_version` for extensions by @motorina0 in https://github.com/lnbits/lnbits/pull/2834
* make dialogs position at top by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2837
* chore: update to corelightning 24.11 by @dni in https://github.com/lnbits/lnbits/pull/2836
* feat: add negative topups by @dni in https://github.com/lnbits/lnbits/pull/2835
* ci: docker image and test with python3.12 by @dni in https://github.com/lnbits/lnbits/pull/2842
* fix: backwards compatible `get_fiat_rate_satoshis` by @motorina0 in https://github.com/lnbits/lnbits/pull/2853
* fix: set default values for `AuditCountStat` by @motorina0 in https://github.com/lnbits/lnbits/pull/2854
* fix: get_payments where clause does query wrong payments including tests by @dni in https://github.com/lnbits/lnbits/pull/2844
* docs: updated install guide by @arcbtc in https://github.com/lnbits/lnbits/pull/2846
* test: use regtest main again by @dni in https://github.com/lnbits/lnbits/pull/2855
* chore: update to v1.0.0-rc7 by @dni in https://github.com/lnbits/lnbits/pull/2856
* feat: standardises top spacing of page layout by @arcbtc in https://github.com/lnbits/lnbits/pull/2848
* Added top cards by @arcbtc in https://github.com/lnbits/lnbits/pull/2858
* feat: moved search inside the transaction table by @arcbtc in https://github.com/lnbits/lnbits/pull/2859
* Added settings links and link for theme by @arcbtc in https://github.com/lnbits/lnbits/pull/2860
* feat: nodemanager, view and edit channels fees by @dni in https://github.com/lnbits/lnbits/pull/2818

#### Jan 2025
* fix: ci with docker image built (downgrade poetry) by @dni in https://github.com/lnbits/lnbits/pull/2876
* fix: lndrest nodemanager get_channel (flaky ci decoy) by @dni in https://github.com/lnbits/lnbits/pull/2877
* fix: NWC mark and remove subs before sending close request by @riccardobl in https://github.com/lnbits/lnbits/pull/2870
* fix: restore user type badge by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2861
* chore: update to breez-sdk 0.6.6 by @dni in https://github.com/lnbits/lnbits/pull/2878
* chore: update i18n labels by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2871
* fix: cln nodemanager errors on failed transactions by @dni in https://github.com/lnbits/lnbits/pull/2865
* fix: Add timeout to wait_for_connection by @riccardobl in https://github.com/lnbits/lnbits/pull/2885
* fix: lnbits/upgrades where not ignore by @dni in https://github.com/lnbits/lnbits/pull/2889
* v1 feat: Vue Routes by @arcbtc in https://github.com/lnbits/lnbits/pull/2872
* feat: harmonize the UI for payment dialog by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2882
* [feat] access control lists (with access tokens) by @motorina0 in https://github.com/lnbits/lnbits/pull/2864
* fix: for g.user error on public pages by @arcbtc in https://github.com/lnbits/lnbits/pull/2892
* Fix payment table refresh by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2894
* feature: Optional bg image and neon borders by @arcbtc in https://github.com/lnbits/lnbits/pull/2897
* fix: fiat tracking / updating wallet without reloads by @arcbtc in https://github.com/lnbits/lnbits/pull/2891
* fix: multiple ws connections by @motorina0 in https://github.com/lnbits/lnbits/pull/2907
* [feat] Watchdog and notifications by @motorina0 in https://github.com/lnbits/lnbits/pull/2895
* feat: do not allow `user_id_only` login for admins by @motorina0 in https://github.com/lnbits/lnbits/pull/2904
* feature: admin toggle to disable outgoing payments by @arcbtc in https://github.com/lnbits/lnbits/pull/2909
* feature: Default theme for new users by @arcbtc in https://github.com/lnbits/lnbits/pull/2898
* Translate expiry to expirySeconds for Phoenixd by @blackcoffeexbt in https://github.com/lnbits/lnbits/pull/2901
* fix: router force update by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2914
* Add bar spinner by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2915
* fixes wallet ws by @arcbtc in https://github.com/lnbits/lnbits/pull/2912
* Some menu naming changes by @arcbtc in https://github.com/lnbits/lnbits/pull/2911
* fix: convert `BigDecimal` object to `int` (postgres only) by @motorina0 in https://github.com/lnbits/lnbits/pull/2918

#### Feb 2025
* Fix index.html error by @arcbtc in https://github.com/lnbits/lnbits/pull/2923
* Feat: Adds wallet icon/color select by @arcbtc in https://github.com/lnbits/lnbits/pull/2917
* Add a payments page for admin by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2910
* Reset wallet keys by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2929
* Fixes the jinja container for first_install by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2925
* Revamp the UI on Login / Register page by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2919
* UI improvements by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2926
* Feat: Creates .AppImage a̶n̶d̶ .d̶m̶g̶ on release by @arcbtc in https://github.com/lnbits/lnbits/pull/2920
* Fixes claiming LNURL by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2924
* feat: migrate in chunks by @motorina0 in https://github.com/lnbits/lnbits/pull/2936
* Fix login with oauth by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2935
* Fixes switching back to wallet by @arcbtc in https://github.com/lnbits/lnbits/pull/2937
* white theme that doesnt hurt eyes by @arcbtc in https://github.com/lnbits/lnbits/pull/2938
* Fixes setting theme from account by @arcbtc in https://github.com/lnbits/lnbits/pull/2939
* [fix]: small fixes v1 on demo DB by @motorina0 in https://github.com/lnbits/lnbits/pull/2940
* [fix] small fixes for ext upgrades by @motorina0 in https://github.com/lnbits/lnbits/pull/2941
* Adds no-border to fix the install card by @arcbtc in https://github.com/lnbits/lnbits/pull/2950
* Tweak: Updated Poetry install to include headers and make copy/paste easier by @arcbtc in https://github.com/lnbits/lnbits/pull/2948
* Adds extension#<ext name> option to extensions url by @arcbtc in https://github.com/lnbits/lnbits/pull/2947
* Tweak: Removes profile dropdown for public pages by @arcbtc in https://github.com/lnbits/lnbits/pull/2943
* BG image/gradient to light fix by @arcbtc in https://github.com/lnbits/lnbits/pull/2945
* tweak: fun themes by @arcbtc in https://github.com/lnbits/lnbits/pull/2951
* Fix: payments table by @arcbtc in https://github.com/lnbits/lnbits/pull/2952
* Wallet polish by @motorina0 in https://github.com/lnbits/lnbits/pull/2942
* Small fix on public pages by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2953
* Another small one by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2954
* Fix: date grouping for older SQLite versions by @motorina0 in https://github.com/lnbits/lnbits/pull/2955
* Revert "Another small one" by @arcbtc in https://github.com/lnbits/lnbits/pull/2958
* fix: keep upgrades out of codebase by @motorina0 in https://github.com/lnbits/lnbits/pull/2957
* [fix] callback url validation by @motorina0 in https://github.com/lnbits/lnbits/pull/2959
* fix: wallet url by @motorina0 in https://github.com/lnbits/lnbits/pull/2961
* Tweak so long wallet names/balances do not break wallet card/list by @arcbtc in https://github.com/lnbits/lnbits/pull/2964
* Quasarfy drawer scroll by @arcbtc in https://github.com/lnbits/lnbits/pull/2965
* fix: logout on safari by @motorina0 in https://github.com/lnbits/lnbits/pull/2971
* Chart polish by @motorina0 in https://github.com/lnbits/lnbits/pull/2973
* fix: nostr login by @motorina0 in https://github.com/lnbits/lnbits/pull/2975
* add blink logo by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2976
* fix: extract tag from `extra` by @motorina0 in https://github.com/lnbits/lnbits/pull/2977
* adds a blur to the transparent bg by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2978
* Change UI for Pay Invoice Dialog by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2979
* change icon for pending by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2980
* feat: add `normalize_path ` helper by @motorina0 in https://github.com/lnbits/lnbits/pull/2981
* bug: settings fundingtab errors by @dni in https://github.com/lnbits/lnbits/pull/2982
* fix: pay_invoice timeout to prevent blocking by @dni in https://github.com/lnbits/lnbits/pull/2875
* Fake wallet fixes by @arcbtc in https://github.com/lnbits/lnbits/pull/2983
* feat: modernize error page by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2949
* fix: wallet balance format by @arcbtc in https://github.com/lnbits/lnbits/pull/2985
* fix: default hide funding inputs by @arcbtc in https://github.com/lnbits/lnbits/pull/2987
* feat: add python-multipart for uploads by @dni in https://github.com/lnbits/lnbits/pull/2873
* feat: add label for wallet fiat tracking by @dni in https://github.com/lnbits/lnbits/pull/2988
* fix: payments filter by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2989
* tweak: added libfuse2 to guide for fresh vps folks by @arcbtc in https://github.com/lnbits/lnbits/pull/2991
* tweak: just to make it obv port can be changed by @arcbtc in https://github.com/lnbits/lnbits/pull/2992
* tweak: checkout main not needed by @arcbtc in https://github.com/lnbits/lnbits/pull/2993
* [feat]: invoice amount settings by @motorina0 in https://github.com/lnbits/lnbits/pull/2990
* chore: update lnbits version to 1.0.0-rc8 by @dni in https://github.com/lnbits/lnbits/pull/2995
* tweak: embit needs to be declared by @arcbtc in https://github.com/lnbits/lnbits/pull/2996
* Fix a typo in reset password logic by @talvasconcelos in https://github.com/lnbits/lnbits/pull/2998
* [feat] filter payments in wallet by @motorina0 in https://github.com/lnbits/lnbits/pull/2997
* [Fix] Denomination 3 characters by @talvasconcelos in https://github.com/lnbits/lnbits/pull/3001
* [fix]: various issues discovered during testing by @motorina0 in https://github.com/lnbits/lnbits/pull/3002
* fix: paying an invoice does not send a webhook. #2472 by @dni in https://github.com/lnbits/lnbits/pull/2999
* [fix] admin errors by @motorina0 in https://github.com/lnbits/lnbits/pull/3004
* Fix: compare not assign by @talvasconcelos in https://github.com/lnbits/lnbits/pull/3009



#### Extension commits between Dec 2024 - Feb 2025 (mostly preparing for v1)
* https://github.com/lnbits/fossa_extension/commits?since=2024-12-01&until=2025-02-28
* https://github.com/lnbits/nwcprovider/commits?since=2024-12-01&until=2025-02-28
* https://github.com/lnbits/bitcoinswitch_extension/commits?since=2024-12-01&until=2025-02-28
* https://github.com/lnbits/splitpayments/commits?since=2024-12-01&until=2025-02-28
* https://github.com/lnbits/jukebox/commits?since=2024-12-01&until=2025-02-28
* https://github.com/lnbits/boltcards/commits?since=2024-12-01&until=2025-02-28
* https://github.com/lnbits/nostrnip5/commits?since=2024-12-01&until=2025-02-28
* https://github.com/lnbits/example/commits?since=2024-12-01&until=2025-02-28
* https://github.com/lnbits/myextension/commits?since=2024-12-01&until=2025-02-28
* https://github.com/lnbits/copilot/commits?since=2024-12-01&until=2025-02-28
* https://github.com/lnbits/raisenow/commits?since=2024-12-01&until=2025-02-28
* https://github.com/lnbits/where39/commits?since=2024-12-01&until=2025-02-28
* https://github.com/lnbits/offlineshop/commits?since=2024-12-01&until=2025-02-28
* https://github.com/lnbits/lncalendar/commits?since=2024-12-01&until=2025-02-28
* https://github.com/lnbits/livestream/commits?since=2024-12-01&until=2025-02-28
* https://github.com/lnbits/gerty/commits?since=2024-12-01&until=2025-02-28
* https://github.com/lnbits/pay2print/commits?since=2024-12-01&until=2025-02-28
* https://github.com/lnbits/streamalerts/commits?since=2024-12-01&until=2025-02-28
* https://github.com/lnbits/bleskomat/commits?since=2024-12-01&until=2025-02-28
* https://github.com/lnbits/scrub/commits?since=2024-12-01&until=2025-02-28
* https://github.com/lnbits/nostrclient/commits?since=2024-12-01&until=2025-02-28
* https://github.com/lnbits/withdraw/commits?since=2024-12-01&until=2025-02-28
* https://github.com/lnbits/invoices/commits?since=2024-12-01&until=2025-02-28

#### New extension
https://github.com/lnbits/sellcoins

#### Content
* 5 years of contributions https://www.youtube.com/watch?v=LCPt4bkHT7g
* v1 overview https://www.youtube.com/watch?v=LCPt4bkHT7g
* LNbits install tut by @arcbtc https://github.com/lnbits/appimage_phoenixd_install, https://www.youtube.com/watch?v=ljqXSxXnYxc
* LNbits server notification demo https://www.youtube.com/watch?v=5eFATj2vFP8
* Where39 demo https://www.youtube.com/watch?v=p8aIhwqFtTQ

#### General expenses
* DNI general expenses in El Sal for workshops & assisting Planb
