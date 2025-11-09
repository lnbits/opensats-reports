# LNbits  >_OpenSats Grant September 2025 - October 2025

For the final few months of our OpenSats grant, we switched from Poetry to UV, resulting in faster builds and a fixed Nix Flake. We also created a beautiful, cutting-edge Nostr Remote Signer; added card tap-to-pay payments to TPoS (which, combined with the TPoS ATM feature, unlocks OTC bitcoin selling for merchants); built an incredible Extension Builder that lets users create an LNbits extension in under 30 minutes; and delivered a tonne of other features, fixes, and updates.

Thank you from all of us LNbits devs and users ❤️

## Educational stuff

 <span title="NOSTR REMOTE SIGNER"><a href="https://www.youtube.com/watch?v=5Ej9pRJvTZU"><img width="170" src="https://img.youtube.com/vi/5Ej9pRJvTZU/mqdefault.jpg"></a></span> <span title="EXTENSION BUILDER"><a href="https://www.youtube.com/watch?v=aRTRYcNwqj0"><img width="170" src="https://img.youtube.com/vi/aRTRYcNwqj0/mqdefault.jpg"></a></span>   <span title="Scrum Extension"><a href="https://www.youtube.com/watch?v=3S-jMYSds1A"><img width="170" src="https://img.youtube.com/vi/3S-jMYSds1A/mqdefault.jpg"></a></span> <span title="TPoS Update"><a href="https://www.youtube.com/watch?v=8w4-VQ3WFrk"><img width="170" src="https://img.youtube.com/vi/8w4-VQ3WFrk/mqdefault.jpg"></a></span>

## LNbits core

#### September 2025

<a href="https://github.com/lnbits/lnbits/commit/
e51e2bad508423bd5b74ff9ac5223e6004932062">
e51e2ba</a> 2025-09-30 | Vlad Stan | feat: handle subscription callback</br>
<a href="https://github.com/lnbits/lnbits/commit/
857dc6634ffee427d4eddae55525b174a5e30c88">
857dc66</a> 2025-09-30 | Vlad Stan | feat: basic subscription models</br>
<a href="https://github.com/lnbits/lnbits/commit/
6a550dbc12fff348fcf1477bd3a1e837d4f04451">
6a550db</a> 2025-09-30 | Vlad Stan | feat: basic subscription call</br>
<a href="https://github.com/lnbits/lnbits/commit/
79e40000743e81bd48ab4a1a3bfc3e0b337021a9">
79e4000</a> 2025-09-30 | Vlad Stan | beat: basic subscription call</br>
<a href="https://github.com/lnbits/lnbits/commit/
1f46545dea734ec5ae2a96c12d15a9f9c1fa69fa">
1f46545</a> 2025-09-26 | Arc | Reapply "Merge remote-tracking branch 'origin/dev' into stripe_recurring"</br>
<a href="https://github.com/lnbits/lnbits/commit/
37d2a695a70235eab0920e6a09fdb9656d2dc679">
37d2a69</a> 2025-09-26 | Arc | Revert "Merge remote-tracking branch 'origin/dev' into stripe_recurring"</br>
<a href="https://github.com/lnbits/lnbits/commit/
63458ced1ee3bbee627e8f3048abd67bea1534b1">
63458ce</a> 2025-09-26 | Arc | Merge remote-tracking branch 'origin/dev' into stripe_recurring</br>
<a href="https://github.com/lnbits/lnbits/commit/
cb3e340a7859481ea7b0ccc3278014cc4d1223a4">
cb3e340</a> 2025-09-26 | Arc | mypy fix</br>
<a href="https://github.com/lnbits/lnbits/commit/
7c887027546a7f84aa90cfadde11663935467396">
7c88702</a> 2025-09-26 | Arc | docs: updated nix install (#3361)</br>
<a href="https://github.com/lnbits/lnbits/commit/
4f9a5090c2116d6177b06734b8964e98dcee5364">
4f9a509</a> 2025-09-25 | Vlad Stan | [feat] Extension Builder (#3339)</br>
<a href="https://github.com/lnbits/lnbits/commit/
ae24f7e43c9463d709d9a59ea1899f4db4561d00">
ae24f7e</a> 2025-09-25 | arcbtc | Merge branch 'or_stripe' into stripe_recurring</br>
<a href="https://github.com/lnbits/lnbits/commit/
609808f6a23d9fffc89e47e6345dddcd92207b70">
609808f</a> 2025-09-25 | arcbtc | added helper for getting subscription id</br>
<a href="https://github.com/lnbits/lnbits/commit/
c760e6f63df927ee243aa2b2955141d78c09f48b">
c760e6f</a> 2025-09-25 | arcbtc | added a helper to get the subscription id</br>
<a href="https://github.com/lnbits/lnbits/commit/
991ac4d7fe1ffc2a7554ab32bfa18e9f08b187c6">
991ac4d</a> 2025-09-16 | Arc | make</br>
<a href="https://github.com/lnbits/lnbits/commit/
c1c622524ebeb27e5d9a8c231efe6f3a6dc53610">
c1c6225</a> 2025-09-16 | Arc | Working</br>
<a href="https://github.com/lnbits/lnbits/commit/
ccc784c8fca2859b42aa38ff3f4f565def0b7dc7">
ccc784c</a> 2025-09-15 | arcbtc | recuuring payments</br>
<a href="https://github.com/lnbits/lnbits/commit/
7c72766bbd1957cb73b6a916c62bcc67ecfd2376">
7c72766</a> 2025-09-16 | Arc | make</br>
<a href="https://github.com/lnbits/lnbits/commit/
416d17099648a298bebac8be87e5a554f44214f4">
416d170</a> 2025-09-16 | Arc | Working</br>
<a href="https://github.com/lnbits/lnbits/commit/
94ebc22dcc0750f80a8b92eecbf94a1df9ec808f">
94ebc22</a> 2025-09-15 | arcbtc | recuuring payments</br>
<a href="https://github.com/lnbits/lnbits/commit/
769d3a07e85704091c5814851860abd1b5c5f593">
769d3a0</a> 2025-09-15 | arcbtc | hacky hijack</br>
<a href="https://github.com/lnbits/lnbits/commit/
b3dfb0384e583733b79dcee93c16b0fde6f481cc">
b3dfb03</a> 2025-09-15 | arcbtc | Fake Wallet Ark, for playing with ark internally</br>
<a href="https://github.com/lnbits/lnbits/commit/
c054e47913e23130da61f7c286050a7d8cb8a405">
c054e47</a> 2025-09-13 | Arc | Updated to uv (#3360)</br>
<a href="https://github.com/lnbits/lnbits/commit/
92d3269a85bc26e87385f1a856025c940935516e">
92d3269</a> 2025-09-12 | dni ⚡ | chore: update to v1.3.0-rc8 (#3359)</br>
<a href="https://github.com/lnbits/lnbits/commit/
ad8ff48d629179e985fe8aa8b407336f567d1648">
ad8ff48</a> 2025-09-12 | dni ⚡ | chore: ci docker boltz temporary checkout lnbits rc</br>
<a href="https://github.com/lnbits/lnbits/commit/
60f50a71a29d069ac004f5315c44599c913ca715">
60f50a7</a> 2025-09-12 | Arc | feat: Adds stripe tap to pay flow for TPoS running on Android PoS/phone devices (#3334)</br>
<a href="https://github.com/lnbits/lnbits/commit/
c3252ce4dc6a510ce2db9a34fd25d9379db2f892">
c3252ce</a> 2025-09-12 | dni ⚡ | chore: update to version v1.3.0-rc7 (#3356)</br>
<a href="https://github.com/lnbits/lnbits/commit/
c312d70e63fc11435e02f0d5a2a2aa8294ba9e0d">
c312d70</a> 2025-09-12 | dni ⚡ | fix: properly check outgoing payments in phoenixd (#3355)</br>
<a href="https://github.com/lnbits/lnbits/commit/
36fc911b8812b9fa9373cb4cd3db3a69c906aa37">
36fc911</a> 2025-09-10 | dni ⚡ | fix: js error on qrcode component (#3354)</br>
<a href="https://github.com/lnbits/lnbits/commit/
672a5b3a4dd77f3c603597550d31cb0bba3646fa">
672a5b3</a> 2025-09-10 | dni ⚡ | fix: pay with nfc endpoint + add perform_withdraw (#3352)</br>
<a href="https://github.com/lnbits/lnbits/commit/
c0b33560bb12f102c61c1f89ead44bdb17ab637a">
c0b3356</a> 2025-09-10 | Vlad Stan | feat: add `search` label (#3353)</br>
<a href="https://github.com/lnbits/lnbits/commit/
15b6b1d512e32b10a3a77da5c7993304f0ab87b4">
15b6b1d</a> 2025-09-04 | dni ⚡ | fix: also replace http:// urls in <lnbits-qrcode-lnurl> (#3346)</br>
<a href="https://github.com/lnbits/lnbits/commit/
67c92a79cff432b2092a48f1591c890880f6d7bc">
67c92a7</a> 2025-09-03 | dni ⚡ | chore: update lnurl to v0.8.2 (#3347)</br>
<a href="https://github.com/lnbits/lnbits/commit/
86ce0c1b9a7f9a0577af1b12d94e42c3399ab850">
86ce0c1</a> 2025-09-03 | Vlad Stan | feat: improve prompt</br>
<a href="https://github.com/lnbits/lnbits/commit/
59ba2a47c2f44c48339f008509aa83e30be591a0">
59ba2a4</a> 2025-09-03 | Vlad Stan | doc: document settings with copilot</br>
<a href="https://github.com/lnbits/lnbits/commit/
0d4751d6e005ba423423961e832c13620ccb795f">
0d4751d</a> 2025-09-03 | dni ⚡ | fix: catch error response for lnurl pay (#3344)</br>
<a href="https://github.com/lnbits/lnbits/commit/
213bde61a8fc75e46f9229a462bde8bb0565276c">
213bde6</a> 2025-09-02 | dni ⚡ | CI: add poetry lock file check job and update poetry lock (#3343)</br>
<a href="https://github.com/lnbits/lnbits/commit/
59553a6e1ea6152a389e826bdeffe39b6947618a">
59553a6</a> 2025-09-02 | dni ⚡ | chore: update to v1.3.0-rc6 (#3342)</br>
<a href="https://github.com/lnbits/lnbits/commit/
2375f7bcf8bde2cd6fbf28cec46e4e94fc11ac29">
2375f7b</a> 2025-09-02 | dni ⚡ | feat: add copy, download and write NFC to qrcode components (#3335)</br>
<a href="https://github.com/lnbits/lnbits/commit/
5021570f68aff5a601fcf04d0ae214fc06351f09">
5021570</a> 2025-09-02 | dni ⚡ | feat: add `has_connection`, `listen` and `receive_queue` to websocket_manager (#3330)</br>
<a href="https://github.com/lnbits/lnbits/commit/
0d91d5b5be69cf9c0e789433fbfdb532717765ea">
0d91d5b</a> 2025-09-02 | dni ⚡ | chore: update to lnurl v0.8.1 (#3341)</br>
<a href="https://github.com/lnbits/lnbits/commit/
49f02a5b77f991281672525f7a951611a696e7f1">
49f02a5</a> 2025-09-01 | Vlad Stan | chore: ignore `.venv` dir (#3338)</br>

#### October 2025

<a href="https://github.com/lnbits/lnbits/commit/d6c42b19c5263c7002c5635d550dbdee1c48daa7">d6c42b19</a> 2025-10-31 | dni ⚡ | bundle</br>
<a href="https://github.com/lnbits/lnbits/commit/
62558da4a377c7be2ba853e2dfd025215bb222ef">
62558da</a> 2025-10-31 | dni ⚡ | refactor: move /account into vue component</br>
<a href="https://github.com/lnbits/lnbits/commit/
8e91de26cae939658f9b35cf7c673efd069f8ba5">
8e91de2</a> 2025-10-31 | dni ⚡ | bundle</br>
<a href="https://github.com/lnbits/lnbits/commit/
2e015bc2b475fcc2da18a23d902c0597210e641b">
2e015bc</a> 2025-10-31 | dni ⚡ | refactor: move /admin into vue component</br>
<a href="https://github.com/lnbits/lnbits/commit/
26ea0bab4908d7c9e17e78b672af2d3ae80fbc9f">
26ea0ba</a> 2025-10-31 | dni ⚡ | bundle</br>
<a href="https://github.com/lnbits/lnbits/commit/
c1e018a3461e9b2b87e56ed62a85e4e241c62990">
c1e018a</a> 2025-10-31 | dni ⚡ | refactor: move /users into vue component</br>
<a href="https://github.com/lnbits/lnbits/commit/
8ad24a8bc9aecdf86e095266ad03d185b7c8510b">
8ad24a8</a> 2025-10-31 | dni ⚡ | bundle</br>
<a href="https://github.com/lnbits/lnbits/commit/
e1851d384210e74f3c0639783020b85be3b44a4b">
e1851d3</a> 2025-10-31 | dni ⚡ | refactor: move /wallets into vue component</br>
<a href="https://github.com/lnbits/lnbits/commit/
4d9cd06bbf73bffb0d3212267bd12050c61189fc">
4d9cd06</a> 2025-10-31 | dni ⚡ | bundle</br>
<a href="https://github.com/lnbits/lnbits/commit/
aefb3dd08479177e10dbd98b04c2841394ecdfd6">
aefb3dd</a> 2025-10-31 | dni ⚡ | throw 503 when not enabled</br>
<a href="https://github.com/lnbits/lnbits/commit/
c085eb89d8b533cfe1af7da207372c580f62f343">
c085eb8</a> 2025-10-17 | dni ⚡ | audit</br>
<a href="https://github.com/lnbits/lnbits/commit/
fd780262890849a5e6de9d47dcea72ec44f5d8a9">
fd78026</a> 2025-10-31 | dni ⚡ | move into pages vue</br>
<a href="https://github.com/lnbits/lnbits/commit/
6df07e039da6afde4401fa6470cd407b61ddb003">
6df07e0</a> 2025-10-31 | dni ⚡ | bundle</br>
<a href="https://github.com/lnbits/lnbits/commit/
f381b4155a124cc9596b8c567a7a79d4503f62e3">
f381b41</a> 2025-10-16 | dni ⚡ | move includes into components</br>
<a href="https://github.com/lnbits/lnbits/commit/
7863f9ba4cd1d3ef0156fd24860b4f802d25ed50">
7863f9b</a> 2025-10-16 | dni ⚡ | feat: move `/node` into vue component</br>
<a href="https://github.com/lnbits/lnbits/commit/
dd27b190f38cf349144896cddf1fd469c70adfa0">
dd27b19</a> 2025-10-31 | dni ⚡ | refactor: move `/payments` into vue component (#3414)</br>
<a href="https://github.com/lnbits/lnbits/commit/
e3535e3965b387ec2aa408219fa2b0b248270766">
e3535e3</a> 2025-10-30 | Tiago Vasconcelos | chore: bundle</br>
<a href="https://github.com/lnbits/lnbits/commit/
f405d6834ac7dafdd545333ef63198a3acb24b67">
f405d68</a> 2025-10-30 | Tiago Vasconcelos | logs cleanup and notifications set</br>
<a href="https://github.com/lnbits/lnbits/commit/
93bcd25ab7570cb50a3948d9df5565429652a515">
93bcd25</a> 2025-10-30 | Tiago Vasconcelos | add connection lost notification</br>
<a href="https://github.com/lnbits/lnbits/commit/
9d288e6a98d7e1114961500ed207279d977aef75">
9d288e6</a> 2025-10-30 | Tiago Vasconcelos | connection warning i18n</br>
<a href="https://github.com/lnbits/lnbits/commit/
b71382aa1e4a22b7dd15390b6e7973f9fe0bd8f4">
b71382a</a> 2025-10-30 | Tiago Vasconcelos | add notification badge</br>
<a href="https://github.com/lnbits/lnbits/commit/
241f1f81a85589ec842b7c697c59e774ccd7fc1a">
241f1f8</a> 2025-10-30 | Tiago Vasconcelos | fix websocket connection</br>
<a href="https://github.com/lnbits/lnbits/commit/
2856803ca700b7a634af92bf135ec5a4004a82a6">
2856803</a> 2025-10-30 | dni ⚡ | fix: handle all lnurl exceptions on lnurlscan endpoint (#3451)</br>
<a href="https://github.com/lnbits/lnbits/commit/
ca8264b1f52c93c6f706a4f4364adde3fc000f94">
ca8264b</a> 2025-10-30 | dni ⚡ | feat: remove nfc not supported (#3453)</br>
<a href="https://github.com/lnbits/lnbits/commit/
39ca9da87027f026baf977f4abed3812e00b1f67">
39ca9da</a> 2025-10-30 | dni ⚡ | feat: NWC use coincurve instead of secp (#3455)</br>
<a href="https://github.com/lnbits/lnbits/commit/
2b603bdc4863fad0d46f7ac7c396aee2a18bbe47">
2b603bd</a> 2025-10-29 | dni ⚡ | fix: add dependency-groups get rid of warning (#3454)</br>
<a href="https://github.com/lnbits/lnbits/commit/
057902144825564e470dc650c7b1a7ef80f7c626">
0579021</a> 2025-10-29 | Vlad Stan | chore: revert some</br>
<a href="https://github.com/lnbits/lnbits/commit/
a82d2d209138cf15b5a6bd290ce03156665f32ab">
a82d2d2</a> 2025-10-29 | Vlad Stan | feat: show invite notifications</br>
<a href="https://github.com/lnbits/lnbits/commit/
60366a420daabb96cba539f6bb45c205b41955e4">
60366a4</a> 2025-10-29 | Vlad Stan | refactor: extract logic to services</br>
<a href="https://github.com/lnbits/lnbits/commit/
eaa97d7347cd2a44ce4c11585e320a88c353d4ea">
eaa97d7</a> 2025-10-29 | Vlad Stan | refactor: rename `user_id_hash` to `request_id`</br>
<a href="https://github.com/lnbits/lnbits/commit/
4a2e5f876258fdb954a93c7a9216108bd6c199a8">
4a2e5f8</a> 2025-10-29 | Vlad Stan | feat: handle invitations</br>
<a href="https://github.com/lnbits/lnbits/commit/
b4189a12e9f2f160c21ed8ce6e2bd4bbff0a8870">
b4189a1</a> 2025-10-27 | Vlad Stan | feat: better ownership check</br>
<a href="https://github.com/lnbits/lnbits/commit/
bffe610cd6d9207740a1cbf248adeb6ae654cd19">
bffe610</a> 2025-10-27 | Vlad Stan | fix: update share permision</br>
<a href="https://github.com/lnbits/lnbits/commit/
248fcc06abf6fe49ad992e24bc81e6221f342e13">
248fcc0</a> 2025-10-27 | dni ⚡ | fix: release ci, pass upload_url from task to task (#3449)</br>
<a href="https://github.com/lnbits/lnbits/commit/
d6bbe8e58936e763ced2009fa9bf3676e3edb7a9">
d6bbe8e</a> 2025-10-27 | Vlad Stan | refactor: simplify some functions</br>
<a href="https://github.com/lnbits/lnbits/commit/
e49f07d8fd9ee9721b756b9f2f507345f2184ead">
e49f07d</a> 2025-10-27 | Vlad Stan | feat: add more check for wallets</br>
<a href="https://github.com/lnbits/lnbits/commit/
278214a3bb1cbcf58cabfb8054635809a3d7fea1">
278214a</a> 2025-10-27 | Vlad Stan | fix: approve share</br>
<a href="https://github.com/lnbits/lnbits/commit/
4485eca400c8c6f9c51e4d5f5c2128fa9f2bf1c6">
4485eca</a> 2025-10-27 | Vlad Stan | feat: add share icon to wallet</br>
<a href="https://github.com/lnbits/lnbits/commit/
66e2f78f4ea1918289a5d51c62e875ed574c5638">
66e2f78</a> 2025-10-24 | Vlad Stan | feat: all add wallets now have type</br>
<a href="https://github.com/lnbits/lnbits/commit/
87f25ea7156df87f3886e4e87ba55dbc1084ba11">
87f25ea</a> 2025-10-24 | Vlad Stan | fix: LND GRPC macaroon fields (#3444)</br>
<a href="https://github.com/lnbits/lnbits/commit/
282b08c3b3f3d8280c5c0acb2a06aca6b886812f">
282b08c</a> 2025-10-24 | Vlad Stan | refactor: simplify source wallet logic</br>
<a href="https://github.com/lnbits/lnbits/commit/
99979a026835cdd743d43824e9ec4786030cb9a8">
99979a0</a> 2025-10-24 | Vlad Stan | refactor: query string</br>
<a href="https://github.com/lnbits/lnbits/commit/
e0fcde38dfad5815c6b3df410e9feb5260403564">
e0fcde3</a> 2025-10-24 | Vlad Stan | refactor: re-order functions</br>
<a href="https://github.com/lnbits/lnbits/commit/
9da1a6fa588989d280e03c26a2ce804a64fa3d2c">
9da1a6f</a> 2025-10-24 | Vlad Stan | fix: permissions</br>
<a href="https://github.com/lnbits/lnbits/commit/
ef178238cf85827c7f67a191bc2b3d2fe3164e3d">
ef17823</a> 2025-10-24 | Vlad Stan | refactor: simplify logic</br>
<a href="https://github.com/lnbits/lnbits/commit/
d349612e80314d3b032c2bea7469310e2abb0e9d">
d349612</a> 2025-10-23 | Vlad Stan | refactor: rename class</br>
<a href="https://github.com/lnbits/lnbits/commit/
c7bb7c843c9c51bff57bf44b0d83093f4d6cc0e9">
c7bb7c8</a> 2025-10-23 | Vlad Stan | fix: api test</br>
<a href="https://github.com/lnbits/lnbits/commit/
2c5680c6355bec4317c8bcee6a895db7ad01b680">
2c5680c</a> 2025-10-23 | Vlad Stan | fix: unit test</br>
<a href="https://github.com/lnbits/lnbits/commit/
f5ca49fc192ed1d3482759ce1f65aa60063b987a">
f5ca49f</a> 2025-10-23 | Vlad Stan | fix: item grouping</br>
<a href="https://github.com/lnbits/lnbits/commit/
aa2cbfa6e2ffdeaffa8d5af1a42bec497537767d">
aa2cbfa</a> 2025-10-23 | Vlad Stan | chore: roll back</br>
<a href="https://github.com/lnbits/lnbits/commit/
fbdfc7f57ab2162779b5f99ca26a617152c6f776">
fbdfc7f</a> 2025-10-23 | Vlad Stan | fix: permissions</br>
<a href="https://github.com/lnbits/lnbits/commit/
af7bc409fedf9533356e3597a99f780a7583cbdb">
af7bc40</a> 2025-10-23 | Vlad Stan | fix: limit notifications for shared wallets</br>
<a href="https://github.com/lnbits/lnbits/commit/
a6a257ef968b82ff19624153bcc1e0fd230e4268">
a6a257e</a> 2025-10-23 | Vlad Stan | refactor: wrap condition</br>
<a href="https://github.com/lnbits/lnbits/commit/
b441ae1f7164195efd759abb830510b993d2dcb8">
b441ae1</a> 2025-10-23 | Vlad Stan | fix: check share approve</br>
<a href="https://github.com/lnbits/lnbits/commit/
9fd9b0a33be404c02e62d7bf56f2cd8b7d179f61">
9fd9b0a</a> 2025-10-23 | Vlad Stan | fix: rebase</br>
<a href="https://github.com/lnbits/lnbits/commit/
96c2d2101a5d25b059838d01063189e69bbdea3d">
96c2d21</a> 2025-10-23 | Vlad Stan | fix: wallet type check</br>
<a href="https://github.com/lnbits/lnbits/commit/
8f6820b90400a7eaa413fb0e06c2b3d786ace291">
8f6820b</a> 2025-10-23 | Vlad Stan | feat: improve error message</br>
<a href="https://github.com/lnbits/lnbits/commit/
5750e67ccee694d18dafa9cb8d2ff99552719bae">
5750e67</a> 2025-10-23 | Vlad Stan | refactor: extract `_wallet_shre.html`</br>
<a href="https://github.com/lnbits/lnbits/commit/
81fdea4dc1e8aa6710459aecfe1914985ce4340c">
81fdea4</a> 2025-10-23 | Vlad Stan | feat: better icons</br>
<a href="https://github.com/lnbits/lnbits/commit/
b5ec186dcaf558010bdd172f28e43913075ea744">
b5ec186</a> 2025-10-23 | Vlad Stan | feat: better UI</br>
<a href="https://github.com/lnbits/lnbits/commit/
eb2970a351acf3f21f5fa3794ae1c9f797e94dcc">
eb2970a</a> 2025-10-23 | Vlad Stan | feat: improve the UI</br>
<a href="https://github.com/lnbits/lnbits/commit/
8c06db7f66d287ef6dfc9a964c315e04980d5777">
8c06db7</a> 2025-10-22 | Vlad Stan | feat: manage permssions</br>
<a href="https://github.com/lnbits/lnbits/commit/
cac11f33594ca4bdbea5b0ff758da78f0cb231c9">
cac11f3</a> 2025-10-21 | Vlad Stan | feat: show granted permissions</br>
<a href="https://github.com/lnbits/lnbits/commit/
81587815d89eca9cb6cd37843e8ff2728170a376">
8158781</a> 2025-10-21 | Vlad Stan | feat: create shared wallet</br>
<a href="https://github.com/lnbits/lnbits/commit/
6dfca09fabd72b701b8c6f8c1f40a2610f857b78">
6dfca09</a> 2025-10-20 | Vlad Stan | feat: notify mirrored wallet</br>
<a href="https://github.com/lnbits/lnbits/commit/
59a65a8e49c8cdb3e1adde456e4d9ab376a3c056">
59a65a8</a> 2025-10-20 | Vlad Stan | chore: clean-up logs</br>
<a href="https://github.com/lnbits/lnbits/commit/
681f9ce50cb3ec7be4c8612c4d41068bd1d728d5">
681f9ce</a> 2025-10-20 | Vlad Stan | feat: move logic to crud level</br>
<a href="https://github.com/lnbits/lnbits/commit/
b3887cf0d856f5ec6d1aa1fc2b20f64892ca3903">
b3887cf</a> 2025-10-18 | Vlad Stan | feat: experimenting</br>
<a href="https://github.com/lnbits/lnbits/commit/
7f9e8633b381acb3f326be8f21729419d5ef2b15">
7f9e863</a> 2025-10-17 | Vlad Stan | feat: try stuff</br>
<a href="https://github.com/lnbits/lnbits/commit/
361012445b3cd927a448a74967e53c2167798fca">
3610124</a> 2025-10-17 | Vlad Stan | refactor: rename function</br>
<a href="https://github.com/lnbits/lnbits/commit/
eff26eceeb5fac43aeef7e89d212cef84a6acfe4">
eff26ec</a> 2025-10-17 | Vlad Stan | fix: enum</br>
<a href="https://github.com/lnbits/lnbits/commit/
afe08ab30292f0f36bf9979400336490ff47f139">
afe08ab</a> 2025-10-17 | Vlad Stan | feat: first draft of shared wallets</br>
<a href="https://github.com/lnbits/lnbits/commit/
b9de754598efece12bb97470ed970e2017ef040a">
b9de754</a> 2025-10-21 | Vlad Stan | fix: exclude (soft) deleted wallets when creating an invoice (#3439)</br>
<a href="https://github.com/lnbits/lnbits/commit/
8ed06e600e78492088265ee3641bc1f82754fdd8">
8ed06e6</a> 2025-10-17 | Tiago Vasconcelos | chore: bundle</br>
<a href="https://github.com/lnbits/lnbits/commit/
a3545bd02a06d91335f822428813d04dd8917ccf">
a3545bd</a> 2025-10-17 | Tiago Vasconcelos | prevent dialog on unmount</br>
<a href="https://github.com/lnbits/lnbits/commit/
c0dd35388092bfd96793f5bbb4726b6b5fc7b435">
c0dd353</a> 2025-10-16 | Tiago Vasconcelos | fix final notify and clean up</br>
<a href="https://github.com/lnbits/lnbits/commit/
ae8b37a69cadb546831b201a908d6be9b8073ef3">
ae8b37a</a> 2025-10-16 | Tiago Vasconcelos | missing one final piece.... notification</br>
<a href="https://github.com/lnbits/lnbits/commit/
810afcd3d43c58ca4ccabbfa00bdaf8f8325bc7a">
810afcd</a> 2025-10-16 | Tiago Vasconcelos | before refactor</br>
<a href="https://github.com/lnbits/lnbits/commit/
bf3412bc6ed6ee5e8456ae3918030b8dee4aa586">
bf3412b</a> 2025-10-16 | Tiago Vasconcelos | cleanup</br>
<a href="https://github.com/lnbits/lnbits/commit/
89e14ff1ff7feb83fedc287df00e83156b349f4d">
89e14ff</a> 2025-10-15 | Tiago Vasconcelos | tough nut to crack</br>
<a href="https://github.com/lnbits/lnbits/commit/
8cd09fc38d891a884454ce10377d3bb54afb1906">
8cd09fc</a> 2025-10-15 | Tiago Vasconcelos | fix typo in console log</br>
<a href="https://github.com/lnbits/lnbits/commit/
e7dea27cbb291934bdd4056ed9f6bed62e2a2570">
e7dea27</a> 2025-10-14 | dni ⚡ | remove mounted and init events on created, was run 3 times</br>
<a href="https://github.com/lnbits/lnbits/commit/
e105877d32c91e3a75e36b21beb4f5ddf3115a27">
e105877</a> 2025-10-14 | Tiago Vasconcelos | remove log</br>
<a href="https://github.com/lnbits/lnbits/commit/
536dee01ba08086dab3a6ee317a86d9f03e337ef">
536dee0</a> 2025-10-14 | Tiago Vasconcelos | fix infinite reconnect</br>
<a href="https://github.com/lnbits/lnbits/commit/
1a57cc33ab8d422e4b4fd24525d9ea6d40418748">
1a57cc3</a> 2025-10-14 | Tiago Vasconcelos | error handling and proper return</br>
<a href="https://github.com/lnbits/lnbits/commit/
ca57df9e1ecb990f1b738960b0bfdc61a2969f9e">
ca57df9</a> 2025-10-13 | Tiago Vasconcelos | fix websocket scope</br>
<a href="https://github.com/lnbits/lnbits/commit/
55c5ab3a6d3a67fedd5021ad0e52e3628c7a2c14">
55c5ab3</a> 2025-10-17 | dni ⚡ | feat: ci appimage have manual triggers (#3424)</br>
<a href="https://github.com/lnbits/lnbits/commit/
bd07a319abf1368723649d99add449607fcb2342">
bd07a31</a> 2025-10-17 | dni ⚡ | fix: appimage ci workflow (#3423)</br>
<a href="https://github.com/lnbits/lnbits/commit/
6b732a2a6a640a52c4f305f840613fea17969fca">
6b732a2</a> 2025-10-17 | dni ⚡ | chore: update to v1.3.1 (#3422)</br>
<a href="https://github.com/lnbits/lnbits/commit/
25c8dd18e07e9a5278b783319ef2ddecc2a355ff">
25c8dd1</a> 2025-10-17 | DoktorShift | docs: update admin ui readme.md (#3402)</br>
<a href="https://github.com/lnbits/lnbits/commit/
2b1b5cadaad7d69ece84f2d980efc0cc1ca97658">
2b1b5ca</a> 2025-10-17 | dni ⚡ | chore: dead cose in core/tasks.py (#3421)</br>
<a href="https://github.com/lnbits/lnbits/commit/
6b4182042237086fb7ebc4d6e2b84486cb792e2f">
6b41820</a> 2025-10-17 | Vlad Stan | refactor: re-order methods based on name</br>
<a href="https://github.com/lnbits/lnbits/commit/
7116353431010532467a068b0dcca6f9a75626a2">
7116353</a> 2025-10-17 | Vlad Stan | feat: edit wallet name by admin (#3417)</br>
<a href="https://github.com/lnbits/lnbits/commit/
de6827af5857e3b310e211e486cd8ce8147e8ebe">
de6827a</a> 2025-10-17 | Vlad Stan | feat: add  and initialize the `payment_request` field for `Payment` (#3389)</br>
<a href="https://github.com/lnbits/lnbits/commit/
40c065708a465694a0a27b8edd0b47ce70d2bce6">
40c0657</a> 2025-10-17 | Vlad Stan | [feat] add case insensitive search for users (#3413)</br>
<a href="https://github.com/lnbits/lnbits/commit/
bdc481f6ff31bfbcd77d555947dc9692183d00c0">
bdc481f</a> 2025-10-16 | Arc | Merge branch 'dev' into dependabot/pip/cryptography-44.0.1</br>
<a href="https://github.com/lnbits/lnbits/commit/
bf06def9b7f0abda1c2f8c43f6885a2fda4257e0">
bf06def</a> 2025-10-17 | Vlad Stan | [feat] Stripe subscription (#3369)</br>
<a href="https://github.com/lnbits/lnbits/commit/
182894fd9338094b743efb5c3bde31584bb737a2">
182894f</a> 2025-10-16 | Tiago Vasconcelos | bug: frontend, add some margin to bottom (#3405)</br>
<a href="https://github.com/lnbits/lnbits/commit/
d0cf374cda0d5a192e5107349dd7a61c7264eb6f">
d0cf374</a> 2025-10-16 | Tiago Vasconcelos | feat: add UI funding source retries (#3407)</br>
<a href="https://github.com/lnbits/lnbits/commit/
1e0dab32c34d0086e36ac1b051f8c820e591d5cb">
1e0dab3</a> 2025-10-17 | dni ⚡ | ci: add appimage to release flow (#3412)</br>
<a href="https://github.com/lnbits/lnbits/commit/
34c9e218bb32e504c2870bff92d54a7378967653">
34c9e21</a> 2025-10-16 | dni ⚡ | chore: update boltz docker image to latest (#3418)</br>
<a href="https://github.com/lnbits/lnbits/commit/
02b851a488223e8d4a8f8089af2f47b67ea19a38">
02b851a</a> 2025-10-16 | dni ⚡ | bundle</br>
<a href="https://github.com/lnbits/lnbits/commit/
5ae6464da7dac80f9c9fae36eeaa4a68ce17c1f3">
5ae6464</a> 2025-10-16 | dni ⚡ | feat: add verify preimage form to wallet page</br>
<a href="https://github.com/lnbits/lnbits/commit/
9cc6a964334f2d4ddbb7c7da926d8f96ab50d9c7">
9cc6a96</a> 2025-10-15 | dni ⚡ | chore: update version to v1.3.0 (#3411)</br>
<a href="https://github.com/lnbits/lnbits/commit/
912edc0ea2c78f2e159acde5f1515fa7b7fe6c5b">
912edc0</a> 2025-10-15 | Vlad Stan | Merge branch 'stripe_subscription' into test_stripe_subscriptions</br>
<a href="https://github.com/lnbits/lnbits/commit/
0c15a614a862e37a620a873b366e528bd3fb34b1">
0c15a61</a> 2025-10-15 | Vlad Stan | feat: unsubscribe</br>
<a href="https://github.com/lnbits/lnbits/commit/
e5ff928c3c0f8a8f9e6391c96d1ebb4bc7f7eab6">
e5ff928</a> 2025-10-15 | Vlad Stan | feat: allow query param for qrcode (#3390)</br>
<a href="https://github.com/lnbits/lnbits/commit/
f31ffba06c1f5f135101386e8cf59317d429398b">
f31ffba</a> 2025-10-15 | dni ⚡ | ci: lock boltz client to latest working version (#3367)</br>
<a href="https://github.com/lnbits/lnbits/commit/
1163e44265e9acc2b5577b02482999ed4287db59">
1163e44</a> 2025-10-15 | Tiago Vasconcelos | fix: overlapping input (#3404)</br>
<a href="https://github.com/lnbits/lnbits/commit/
a55399794e311fd450ccdcdce9ae425c6c1eec63">
a553997</a> 2025-10-14 | Tiago Vasconcelos | WIP tests</br>
<a href="https://github.com/lnbits/lnbits/commit/
10fc88f777286f8e6cfc58c4fd16a123f77bd2de">
10fc88f</a> 2025-10-14 | Tiago Vasconcelos | harden service worker</br>
<a href="https://github.com/lnbits/lnbits/commit/
266b16834b4a81273af34551977bd22e1fa13af7">
266b168</a> 2025-10-10 | Arc | fix nix install doc (#3401)</br>
<a href="https://github.com/lnbits/lnbits/commit/
ad606b251721f8c8fcd49e87d8954d7756ca2e4f">
ad606b2</a> 2025-10-10 | Arc | Fix: Glibc error by pegging ubuntu version, appimage include extras like breez_sdk (#3397)</br>
<a href="https://github.com/lnbits/lnbits/commit/
1ec28079d965d3c6595ce51aae3b038e977ad75e">
1ec2807</a> 2025-10-10 | Arc | docs: jq needed for AppImage install (#3399)</br>
<a href="https://github.com/lnbits/lnbits/commit/
aeaddc1dc6dc9837faaad5bdc8ae903a0b363b49">
aeaddc1</a> 2025-10-09 | Vlad Stan | fix: donate link</br>
<a href="https://github.com/lnbits/lnbits/commit/
f8069c531d89221b12cca28ffbde6b16aaa533a8">
f8069c5</a> 2025-10-08 | Arc | Update installation.md</br>
<a href="https://github.com/lnbits/lnbits/commit/
52f614df1c86f12f5ae6277c6b9d1f9812cd1953">
52f614d</a> 2025-10-08 | Arc | Update installation.md</br>
<a href="https://github.com/lnbits/lnbits/commit/
a9374d509c510f47ca4919d11a1ef59b7b972efa">
a9374d5</a> 2025-10-08 | Vlad Stan | fix: hide payment details for failed payments (#3393)</br>
<a href="https://github.com/lnbits/lnbits/commit/
1ef7c57ade4fb01a1b65589199f055955b44c63b">
1ef7c57</a> 2025-10-08 | Vlad Stan | feat: add  and initialize the `payment_request` field for `Payment` (#3396)</br>
<a href="https://github.com/lnbits/lnbits/commit/
43af32093035ce9173f28c675aecf80508c1dc12">
43af320</a> 2025-10-08 | Vlad Stan | Qrcode enpoint allow quert param (#3395)</br>
<a href="https://github.com/lnbits/lnbits/commit/
4d79d47694d7c59d5cbbe8d5c70b89b232802cb7">
4d79d47</a> 2025-10-08 | Vlad Stan | Stripe subscription (#3394)</br>
<a href="https://github.com/lnbits/lnbits/commit/
938418a93324fceefbcf06304cb5aeb7c29d024a">
938418a</a> 2025-10-08 | Vlad Stan | feat: create subscription based on wallet key</br>
<a href="https://github.com/lnbits/lnbits/commit/
215caca81bb117fa1788ae4f9b19ada7fca570b5">
215caca</a> 2025-10-01 | Vlad Stan | feat: use the status flow</br>
<a href="https://github.com/lnbits/lnbits/commit/
bc10c6e22c98696711540d3934cde155b0e6570f">
bc10c6e</a> 2025-10-01 | Vlad Stan | feat: add types</br>
<a href="https://github.com/lnbits/lnbits/commit/
05c5a27157e367571d0f4ffcaaa76c46c7d564dd">
05c5a27</a> 2025-10-01 | Vlad Stan | feat: limit tag and extra to admins</br>
<a href="https://github.com/lnbits/lnbits/commit/
765521ad3d4dd1671e418865ba4e8b53bafbbbda">
765521a</a> 2025-10-01 | Vlad Stan | refactor: raise early</br>
<a href="https://github.com/lnbits/lnbits/commit/
41ad82add069e5c97a9c2eac2cf895e6f5f17736">
41ad82a</a> 2025-10-01 | Vlad Stan | chore: clean-up</br>
<a href="https://github.com/lnbits/lnbits/commit/
55ace1d961e67bb95a9fceb27ef28b3f69b44bab">
55ace1d</a> 2025-10-01 | Vlad Stan | fix: remove extra call. found meta</br>
<a href="https://github.com/lnbits/lnbits/commit/
bd79916b4d57d2c5fc8ae8f2fa7a612868b1b532">
bd79916</a> 2025-10-01 | Vlad Stan | chore: remove temp data from extra</br>
<a href="https://github.com/lnbits/lnbits/commit/
91cd0fdbbf0a0938950dc641f8f0edf557689e8f">
91cd0fd</a> 2025-10-01 | Vlad Stan | chore: clean-up</br>
<a href="https://github.com/lnbits/lnbits/commit/
057efc5b7e90787e908c1ac0d34ecf0f03c8ba36">
057efc5</a> 2025-10-01 | Vlad Stan | refactor: use consistent namings</br>
<a href="https://github.com/lnbits/lnbits/commit/
3e72788fc85b153ae7b1671f989ebe6aa77bc2d4">
3e72788</a> 2025-10-07 | Vlad Stan | chore: clean prin statement (#3391)</br>
<a href="https://github.com/lnbits/lnbits/commit/
f48d24aca8e63536683485a1174190c83656c4ff">
f48d24a</a> 2025-10-06 | Vlad Stan | feat:  show badge if an extension has paid releases (#3385)</br>
<a href="https://github.com/lnbits/lnbits/commit/
015262c9b367d817c698c4b047e4a5e2885200ea">
015262c</a> 2025-10-06 | Arc | chore: qr button tweak (quasar classes should always be used) (#3351)</br>

## Extension commits between September 2025 - October 2025
* https://github.com/lnbits/bitcoinswitch_extension/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/boltcards/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/boltz/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/coinflip/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/copilot/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/dashboard/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/eightball/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/events/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/extension_builder_stub/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/fossa_extension/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/invoices/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/jukebox/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/legend-regtest-enviroment/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/livestream/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/lnaddress/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/lnbits-extensions/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/lndhub/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/lnpos_extension/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/lnurl/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/lnurlp/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/myextension/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/nostr-clients-resources/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/nostr-signing-device/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/nostrclient/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/nostriotdashboard/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/nostrmarket/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/nostrrelay/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/nsec-remote-signer/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/numberlottery/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/offlineshop/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/paidreviews/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/pay2print/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/paywall/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/recurring/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/satsdice/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/satspot/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/scrub/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/scrum/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/sellcoins/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/tipjar/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/tpos/commits?since=2025-09-01&until=2025-11-01
* https://github.com/lnbits/withdraw/commits?since=2025-09-01&until=2025-11-01


## New extensions
* https://github.com/lnbits/dashboard
* https://github.com/lnbits/nostriotdashboard
* https://github.com/lnbits/paidreviews
* https://github.com/lnbits/recurring
* https://github.com/lnbits/scrum

## New Hardware
* https://github.com/lnbits/nsec-remote-signer
* https://github.com/lnbits/TPoS-Stripe-Tap-to-Pay-Wrapper/commits?since=2025-09-01&until=2025-11-01


