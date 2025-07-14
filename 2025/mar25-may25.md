# LNbits  >_OpenSats Grant March 2025 - May 2025

Post-V1 and beyond 🚀

👇 Some new videos thanks to >_OpenSats.

<span title="Remote signer"><a href="https://www.youtube.com/watch?v=16T_Psc8Qn4"><img width="300" src="https://github.com/user-attachments/assets/3ff9b24a-439c-4077-a223-3ea62e4845bf"></a></span>   <span title="R"><a href="https://www.youtube.com/watch?v=e8VXjp83sdc"><img width="300" src="https://github.com/user-attachments/assets/bbaa4bf3-efa4-4b56-bce8-bec9a2336c09"></a>   <a href="https://www.youtube.com/watch?v=QDwNgHz8v7M"><img width="300" src="https://github.com/user-attachments/assets/cf4bb01e-2df9-411b-8060-2c91e6f7df74"></a>

Post-V1 is an exciting time for us - core is stable - so we get to work through the backlog of features and give all the extensions a little TLC.

All possible thanks to OpwenSats. Thank you from all of us, devs & users in LNbitsLand ❤️

## LNbits core

https://github.com/lnbits/lnbits/commit/77906bc8 2025-05-30 | dni ⚡ | feat: more verbose aes decrypt function (#3177)
63e72871 2025-05-30 | Vlad Stan | fix: accept soft deleted wallets (#3179)
27fd5101 2025-05-29 | blackcoffeexbt | Add funding sources comparison table (#3183)
e6de66e1 2025-05-27 | Vlad Stan | fix: handle node absent in 1ml.com (#3180)
4071925f 2025-05-27 | dni ⚡ | feat: mask unexcepted error and add a exception id (#3178)
3c4d186d 2025-05-27 | dni ⚡ | feat: add urlsafe enc to lnbits-cli (#3173)
56aebb9d 2025-05-27 | Vlad Stan | feat: better service fee payment memo (#3176)
beee24bd 2025-05-27 | Vlad Stan | [feat] ui support for high number of wallets and payments (#3174)
375b95c0 2025-05-26 | Vlad Stan | fix: allow ports for domains (#3171)
5345ccaf 2025-05-20 | Tiago Vasconcelos | [Fix] QR readability  (#3163)
efc52333 2025-05-20 | Arc | fix: frontend scroll area on admin settings (#3162)
e4d09c6d 2025-05-20 | Arc | docs: passing vars to appimage (#3164)
7d0545da 2025-05-20 | Vlad Stan | [fix] timezone for payment list (#3165)
00fccf51 2025-05-20 | Sat | feat: Add Strike Wallet Integration (#3150)
34b8490a 2025-05-20 | dni ⚡ | test: conftest smaller funding amounts (#3167)
cbbba5c4 2025-05-20 | dni ⚡ | fix: regtest nodemanager lndrest issue (#3166)
4a0ef7fa 2025-05-19 | dni ⚡ | feat: add ssl proxy settings to docker and .env.example (#3161)
cd8804da 2025-05-13 | dni ⚡ | chore: update to version v1.1.0 (#3157)
39e4fa72 2025-05-13 | Vlad Stan | test: additional cases for internal payments (#3155)
3b350858 2025-05-13 | dni ⚡ | refactor: untangle lnd's macaroon encryption with AESCipher class (#3152)
7bea5918 2025-05-13 | Arc | feat: dont reset superuser on delete settings endpoint (#3065)
f74fcea3 2025-05-13 | Vlad Stan | fix: safe json conversion (#3148)
ceb82033 2025-05-13 | dni ⚡ | refactor: render variables for jinja, components and window vars (#3014)
7b29223e 2025-05-13 | Sat | feat: add verify_preimage utility function (#3153)
bd19d788 2025-05-11 | Se7enZ | build: add POETRY_INSTALL_ARGS build argument to Dockerfile (#3149)
8458b4d8 2025-05-05 | Tiago Vasconcelos | fix: do not ask for NFC if not needed (#3145)
f92ae8ba 2025-05-05 | Vlad Stan | doc: add time unit to payment_wait_time (#3144)
3529f915 2025-05-05 | Vlad Stan | fix: better differentiation between UNAUTHORIZED and FORBIDDEN (#3139)
6a9089fd 2025-05-05 | dni ⚡ | fix: lnd/lndrest failed canceled/expired invoices (#3143)
5818c3c2 2025-05-04 | tlindi | [doc] Update installation.md to match v1.0.x requirements (#3107)
a38de94e 2025-05-02 | dni ⚡ | chore: update to v1.0.1 (#3137)
b4801ce0 2025-05-02 | tlindi | Update fi.js Password reset request (+fix "more") (#3138)
51bf344d 2025-05-02 | PatMulligan | [FIX] Fix database compatibility issue in search query builder for payments filter (#3090)
32cbf16d 2025-04-30 | Vlad Stan | fix: _bcrypt.__about__.__version__ log warning (#3136)
c4d0540e 2025-04-30 | dni ⚡ | feat: preimages for incoming payments, fundingsource saves preimage on create_invoice  (#3085)
f8b36440 2025-04-29 | Vlad Stan | fix: auto redirect to home page when 401 (#3131)
c2fb45d6 2025-04-29 | dni ⚡ | docs: add notes about freeBSD install (#3124)
e339bb61 2025-04-29 | Vlad Stan | [feat] fetch all payments for user (#3132)
2dee26b7 2025-04-29 | Vlad Stan | fix: set explicit max_age for cookies (#3133)
d774c7a7 2025-04-28 | dni ⚡ | security: update package h11 (#3127)
6c2b312c 2025-04-28 | Vlad Stan | fix: webhook call on invoice pay (#3119)
56c8783d 2025-04-28 | iwarp | fix: Normalize fee_reserve amount value  (#3125)
ffecd03c 2025-04-25 | dni ⚡ | refactor: fundingsource Invoice-, PaymentResponses (#3089)
94d5f377 2025-04-24 | Vlad Stan | fix: mask for fiat amount (#3118)
d89bd740 2025-04-17 | Vlad Stan | fix: use UTC for fromNow() (#3105)
b48489ef 2025-04-17 | iwarp | fix: Explicitly convert lndrest fee_msat to int (#3116)
e686ecda 2025-04-14 | Vlad Stan | feat: i18n reset password message (#3106)
23b4c2cc 2025-04-14 | Vlad Stan | [fix] offset naive dates error (#3104)
1bb29cf0 2025-04-12 | Tiago Vasconcelos | bug: add the defaults else it fails (#3099)
57148484 2025-04-10 | dni ⚡ | feat: install lnbits.sh bash script (#2684) (#3101)
f87e5d43 2025-04-10 | dni ⚡ | chore: update LNbits to version v1.0.0 (#3100)
a0502f16 2025-04-10 | Tiago Vasconcelos | [Fix] - Bug on switching wallets and payment details (#3094)
f6c8a308 2025-04-09 | Vlad Stan | feat: create new user from the command line (#3098)
6df3933c 2025-04-03 | dni ⚡ | ci: trigger release on rc's > 9 (#3088)
ffef085f 2025-04-03 | dni ⚡ | chore: update to v1.0.0-rc10 (#3087)
913991c7 2025-04-03 | tlindi | Update fi.js-1.0.0-rc10-tobe (#3086)
6f611461 2025-04-02 | dni ⚡ | fix: FakeWallet, bolt11 payment_secret is not the preimage (#3084)
681385e2 2025-04-02 | Tiago Vasconcelos | fix dialog consistency (#3082)
883d52c3 2025-04-02 | dni ⚡ | fix: phoenixd uses sat instead of msat for pay_invoice (#3083)
10584618 2025-04-02 | Vlad Stan | fix: include node balance in server status (#3079)
3a7a8885 2025-04-02 | Vlad Stan | fix: missing label (#3081)
6834b5e0 2025-04-01 | Vlad Stan | feat: do not allow regular admins to edit super user (#3077)
10093bb4 2025-04-01 | Vlad Stan | feat: show wallet payments on search (#3076)
1323a200 2025-04-01 | dni ⚡ | feat: cleanup on library dir creation and upload endpoints (#3069)
bafb4ddf 2025-03-31 | Vlad Stan | fix: allow admin to view payments in deleted wallets (#3074)
aa050eaf 2025-03-31 | Vlad Stan | fix: make parallel calls for exchages (#3073)
0c76efa2 2025-03-31 | Arc | Add ws link to curl examples (#3063)
681730a4 2025-03-31 | PatMulligan | [CHORE] add responsive text scaling with clamp() for wallet balance display (#3071)
63adcb67 2025-03-27 | Arc | Adds image library for admins (#3066)
35f78211 2025-03-27 | dni ⚡ | fix: make swagger understand the access token HTTPBearer (#3068)
b185d958 2025-03-23 | Vlad Stan | fix: add default extensions when a user is created (#3061)
30a8d88a 2025-03-22 | Arc | Remove LNbits UI elements (#3064)
f7e98419 2025-03-21 | Arc | Revert "tweak: fix for ws payment" (#3060)
eb09e95e 2025-03-20 | Arc | tweak: fix for ws payment (#3057)
a883e2c7 2025-03-18 | Tiago Vasconcelos | hide 'Runs On' scroll if title is not LNbits (#3053)
e06abb52 2025-03-18 | Tiago Vasconcelos | [Fix] default to sats if wallet not fakewallet (#3055)
9f64b534 2025-03-18 | tlindi | Dev update fi.js again (#3052)
a6bbddce 2025-03-14 | Arc | tweak: use image that works for fav and qr as default (#3051)
adb9d246 2025-03-12 | Tiago Vasconcelos | [Fix] Set default chart text color (#3048)
dc85f269 2025-03-12 | Tiago Vasconcelos | fix: qr scanner button was missing the method (#3046)
14153b4a 2025-03-12 | Tiago Vasconcelos | [Fix] Remove references and warnings for BETA (#3047)
b8a5f394 2025-03-12 | Vlad Stan | [fix] limit the size of the invoice description to 640 characters (#3045)
475ae573 2025-03-12 | dni ⚡ | chore: update to v1.0.0-rc9 (#3043)
d7f0f4da 2025-03-12 | PatMulligan | create backwards compatibility for <=v1.0 (#3041)
f7b3444b 2025-03-12 | Tiago Vasconcelos | fix: unfuck the swap mess (#3023)
28e32a54 2025-03-12 | Arc | tweak: use qr code image for favicon as well (#3031)
1833adc0 2025-03-12 | Arc | Tweak: moved custom denomination to fakewallet funding source (#3030)
b759ec74 2025-03-12 | dependabot[bot] | chore(deps): bump axios from 1.7.7 to 1.8.2 (#3042)
2661d12f 2025-03-12 | Arc | tweak: fixes service fee badge (#3029)
ed419f27 2025-03-12 | dependabot[bot] | chore(deps): bump vue-i18n from 10.0.5 to 10.0.6 (#3022)
c3efd481 2025-03-11 | dni ⚡ | chore: use latest 1.X poetry version (#3039)
4a28c22d 2025-03-10 | Arc | tweak: fix 'test email' btn (#3026)
0d0eb36d 2025-03-10 | Arc | tweak:  fix funding source hide (#3027)
2aa73bfe 2025-03-10 | Arc | tweak: punchy bitcoin theme (#3028)
ebd08019 2025-03-10 | Vlad Stan | feat: return payment status in the websocket response (#3025)
41abe63f 2025-03-07 | Tiago Vasconcelos | hide text on small screen (#3021)
f61471b0 2025-03-05 | dni ⚡ | feat: add test email and improve on email notifications (#3018)
9bd037b6 2025-03-04 | Vlad Stan | [fix] settings cleanup (#3013)
a4ca88b6 2025-03-04 | Arc | tweak: dont show full id on wallet select box (#3017)
f2b9aafc 2025-03-04 | Arc | Tweak: Changed naming for password area (#3016)
ec77a00f 2025-03-03 | Vlad Stan | feat: only check the current page (#3015)
991e0db5 2025-03-03 | Arc | Feat: email notifications (#3007)
fe9b62e8 2025-03-03 | Tiago Vasconcelos | Fix: don't show register if new users not allowed (#3010)
c5964436 2025-03-03 | dni ⚡ | fix: python versions were defined incorrectly and remove 3.9 (#3006)

#### Extension commits between Dec 2024 - Feb 2025 (mostly preparing for v1)
* https://github.com/lnbits/fossa_extension/commits?since=2025-03-01&until=2025-05-28
* https://github.com/lnbits/nwcprovider/commits?since=2025-03-01&until=2025-05-28
* https://github.com/lnbits/bitcoinswitch_extension/commits?since=2025-03-01&until=2025-05-28
* https://github.com/lnbits/splitpayments/commits?since=2025-03-01&until=2025-05-28
* https://github.com/lnbits/jukebox/commits?since=2025-03-01&until=2025-05-28
* https://github.com/lnbits/boltcards/commits?since=2025-03-01&until=2025-05-28
* https://github.com/lnbits/nostrnip5/commits?since=2025-03-01&until=2025-05-28
* https://github.com/lnbits/example/commits?since=2025-03-01&until=2025-05-28
* https://github.com/lnbits/myextension/commits?since=2025-03-01&until=2025-05-28
* https://github.com/lnbits/copilot/commits?since=2025-03-01&until=2025-05-28
* https://github.com/lnbits/raisenow/commits?since=2025-03-01&until=2025-05-28
* https://github.com/lnbits/where39/commits?since=2025-03-01&until=2025-05-28
* https://github.com/lnbits/offlineshop/commits?since=2025-03-01&until=2025-05-28
* https://github.com/lnbits/lncalendar/commits?since=2025-03-01&until=2025-05-28
* https://github.com/lnbits/livestream/commits?since=2025-03-01&until=2025-05-28
* https://github.com/lnbits/gerty/commits?since=2025-03-01&until=2025-05-28
* https://github.com/lnbits/pay2print/commits?since=2025-03-01&until=2025-05-28
* https://github.com/lnbits/streamalerts/commits?since=2025-03-01&until=2025-05-28
* https://github.com/lnbits/bleskomat/commits?since=2025-03-01&until=2025-05-28
* https://github.com/lnbits/scrub/commits?since=2025-03-01&until=2025-05-28
* https://github.com/lnbits/nostrclient/commits?since=2025-03-01&until=2025-05-28
* https://github.com/lnbits/withdraw/commits?since=2025-03-01&until=2025-05-28
* https://github.com/lnbits/invoices/commits?since=2025-03-01&until=2025-05-28

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
