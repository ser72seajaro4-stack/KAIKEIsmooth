# 対応アプリ一覧

全133アプリ（2026年10月30日時点）。App Storeのアプリ番号とGoogle Playのパッケージ名は、各ストアの掲載ページで確認しました。

URLスキームは2026年10月30日のテスト結果（docs/scheme-test-result-20261030.txt）で決めています。テストで開けた（○）ものはそのURLスキームで起動し、開けなかった（×）ものはURLスキームを使わずストア（App Store／Google Play）のページを開きます。

URLスキームで起動：29件 ／ ストアを開く：104件

## 決済（20）

| アプリ名 | App Store | Google Play | URLスキーム | テスト結果 | 備考 |
| --- | --- | --- | --- | --- | --- |
| PayPay | [id1435783608](https://apps.apple.com/jp/app/id1435783608) | [jp.ne.paypay.android.app](https://play.google.com/store/apps/details?id=jp.ne.paypay.android.app) | `paypay://user/showcode` | URLスキームで起動：元の根拠：支払いコード画面を開く paypay://user/showcode は個人ブログ（2021年） |  |
| 楽天ペイ | [id1139755229](https://apps.apple.com/jp/app/id1139755229) | [jp.co.rakuten.pay](https://play.google.com/store/apps/details?id=jp.co.rakuten.pay) | `rakutenpaysdk://` | URLスキームで起動：元の根拠：elepay開発者ドキュメント（rakutenpaysdk） | 楽天ポイントカード・楽天Edy（iPhone）もこのアプリ |
| d払い | [id1328132872](https://apps.apple.com/jp/app/id1328132872) | [com.nttdocomo.keitai.payment](https://play.google.com/store/apps/details?id=com.nttdocomo.keitai.payment) | `dpayment://` | URLスキームで起動 |  |
| au PAY | [id862800897](https://apps.apple.com/jp/app/id862800897) | [jp.auone.wallet](https://play.google.com/store/apps/details?id=jp.auone.wallet) | `auwallet://` | URLスキームで起動：元の根拠：elepay開発者ドキュメント（auwallet） |  |
| メルカリ（メルペイ） | [id667861049](https://apps.apple.com/jp/app/id667861049) | [com.kouzoh.mercari](https://play.google.com/store/apps/details?id=com.kouzoh.mercari) | `https://link.jp.mercari.com/70tO/on4uqvcb` | URLスキームで起動：元の根拠：メルペイ公式サイトのアプリリンク |  |
| ファミペイ | [id1138196572](https://apps.apple.com/jp/app/id1138196572) | [jp.co.family.familymart_app](https://play.google.com/store/apps/details?id=jp.co.family.familymart_app) | `familymart-app:` | URLスキームで起動 |  |
| AEON Pay | [id1100564842](https://apps.apple.com/jp/app/id1100564842) | [jp.co.aeon.credit.android.wallet](https://play.google.com/store/apps/details?id=jp.co.aeon.credit.android.wallet) | なし（ストアを開く） | ストアを開く：試した候補：aeonpay:// / aeonwallet:// |  |
| ゆうちょPay | [id1453364627](https://apps.apple.com/jp/app/id1453364627) | [jp.japanpost.jp_bank.YuchoPayapp](https://play.google.com/store/apps/details?id=jp.japanpost.jp_bank.YuchoPayapp) | なし（ストアを開く） | ストアを開く：試した候補：yuchopay:// | 支払いサービスは2026年12月20日で終了予定 |
| J-Coin Pay | [id1447086572](https://apps.apple.com/jp/app/id1447086572) | [jp.co.bluelab.jcoin.user](https://play.google.com/store/apps/details?id=jp.co.bluelab.jcoin.user) | なし（ストアを開く） | ストアを開く：試した候補：https://j-coinpay.onelink.me/yZpl/JCoinPay / jcoinpay:// / jcoin:// |  |
| Wesmo! | [id6505085493](https://apps.apple.com/jp/app/id6505085493) | [jp.co.westjr.wesmo](https://play.google.com/store/apps/details?id=jp.co.westjr.wesmo) | `https://wesmo-app.onelink.me/eT4U/k4g5v52y` | URLスキームで起動：元の根拠：Wesmo!公式サイトのアプリリンク（AppsFlyer OneLink） | JR西日本 |
| majica（ドン・キホーテ） | [id1001883210](https://apps.apple.com/jp/app/id1001883210) | [com.donki.majica](https://play.google.com/store/apps/details?id=com.donki.majica) | なし（ストアを開く） | ストアを開く：試した候補：https://ppih.onelink.me/ZpUt/a81d78c7 / majica:// |  |
| WAON | [id1471075782](https://apps.apple.com/jp/app/id1471075782) | [waon.app](https://play.google.com/store/apps/details?id=waon.app) | なし（ストアを開く） | ストアを開く：試した候補：waon:// |  |
| nanaco | [id1540014396](https://apps.apple.com/jp/app/id1540014396) | [jp.nanaco.android](https://play.google.com/store/apps/details?id=jp.nanaco.android) | なし（ストアを開く） | ストアを開く：試した候補：nanaco:// |  |
| 楽天Edy | 配信なし | [jp.edy.edyapp](https://play.google.com/store/apps/details?id=jp.edy.edyapp) | なし（ストアを開く） | ストアを開く：試した候補：edy:// / rakutenedy:// | iPhoneは楽天ペイアプリで利用 |
| Kyash | [id1084264883](https://apps.apple.com/jp/app/id1084264883) | [co.kyash](https://play.google.com/store/apps/details?id=co.kyash) | なし（ストアを開く） | ストアを開く：試した候補：kyash:// |  |
| バンドルカード | [id1113352415](https://apps.apple.com/jp/app/id1113352415) | [jp.kanmu.vandle.android](https://play.google.com/store/apps/details?id=jp.kanmu.vandle.android) | `https://vandle.go.link/28rYy` | URLスキームで起動：元の根拠：バンドルカード公式サイトのアプリリンク（Adjust） |  |
| Paidy | [id1220373112](https://apps.apple.com/jp/app/id1220373112) | [com.paidy.paidy](https://play.google.com/store/apps/details?id=com.paidy.paidy) | `https://paidy.onelink.me/eV85/PCfooter` | URLスキームで起動：元の根拠：Paidy公式サイトのアプリリンク（App Store用） |  |
| PayPal | [id283646709](https://apps.apple.com/jp/app/id283646709) | [com.paypal.android.p2pmobile](https://play.google.com/store/apps/details?id=com.paypal.android.p2pmobile) | なし（ストアを開く） | ストアを開く：試した候補：paypal:// |  |
| Apple Wallet | [id1160481993](https://apps.apple.com/jp/app/id1160481993) | 配信なし | `shoebox://` | URLスキームで起動：元の根拠：Apple開発者フォーラム・GitHubの一覧（非公式） | iPhoneのみ |
| Google ウォレット | 配信なし | [com.google.android.apps.walletnfcrel](https://play.google.com/store/apps/details?id=com.google.android.apps.walletnfcrel) | なし（ストアを開く） | ストアを開く：試した候補：googlewallet:// | Androidのみ |

## 交通系（6）

| アプリ名 | App Store | Google Play | URLスキーム | テスト結果 | 備考 |
| --- | --- | --- | --- | --- | --- |
| Suica（モバイルSuica） | [id1156875272](https://apps.apple.com/jp/app/id1156875272) | [com.mobilesuica.msb.android](https://play.google.com/store/apps/details?id=com.mobilesuica.msb.android) | なし（ストアを開く） | ストアを開く：試した候補：mobilesuica:// / suica:// |  |
| PASMO（モバイルPASMO） | [id1489151487](https://apps.apple.com/jp/app/id1489151487) | [com.mobilepasmo.android](https://play.google.com/store/apps/details?id=com.mobilepasmo.android) | なし（ストアを開く） | ストアを開く：試した候補：mobilepasmo:// / pasmo:// |  |
| モバイルICOCA | 配信なし | [jp.co.westjr.android.icocaapp](https://play.google.com/store/apps/details?id=jp.co.westjr.android.icocaapp) | なし（ストアを開く） | ストアを開く：試した候補：mobileicoca:// / icoca:// | Androidのみ（iPhoneはApple PayのICOCA） |
| JRE POINT | [id1081293054](https://apps.apple.com/jp/app/id1081293054) | [jp.co.jreast.jrepoint](https://play.google.com/store/apps/details?id=jp.co.jreast.jrepoint) | なし（ストアを開く） | ストアを開く：試した候補：jrepoint:// / jre-point:// | JR東日本 |
| WESTER（WESTERポイント） | [id1528917792](https://apps.apple.com/jp/app/id1528917792) | [jp.co.westjr.wester](https://play.google.com/store/apps/details?id=jp.co.westjr.wester) | なし（ストアを開く） | ストアを開く：試した候補：wester:// | JR西日本 |
| TOKAI STATION POINT | [id6449078524](https://apps.apple.com/jp/app/id6449078524) | [jp.co.jr_central.tokaistationpoint](https://play.google.com/store/apps/details?id=jp.co.jr_central.tokaistationpoint) | `tospo://` | URLスキームで起動 | JR東海 |

## 共通ポイント・マイル（10）

| アプリ名 | App Store | Google Play | URLスキーム | テスト結果 | 備考 |
| --- | --- | --- | --- | --- | --- |
| 楽天ポイントクラブ | [id641501350](https://apps.apple.com/jp/app/id641501350) | [jp.co.rakuten.pointclub.android](https://play.google.com/store/apps/details?id=jp.co.rakuten.pointclub.android) | なし（ストアを開く） | ストアを開く：試した候補：rakutenpointclub:// / pointclub:// |  |
| dポイントクラブ | [id821434357](https://apps.apple.com/jp/app/id821434357) | [com.nttdocomo.android.dpoint](https://play.google.com/store/apps/details?id=com.nttdocomo.android.dpoint) | なし（ストアを開く） | ストアを開く：試した候補：dpoint://top / dpoint:// |  |
| Ponta | [id1036066384](https://apps.apple.com/jp/app/id1036066384) | [jp.ponta.myponta](https://play.google.com/store/apps/details?id=jp.ponta.myponta) | なし（ストアを開く） | ストアを開く：試した候補：ponta:// / myponta:// |  |
| Vポイント | [id468976361](https://apps.apple.com/jp/app/id468976361) | [jp.co.ccc.Tsite](https://play.google.com/store/apps/details?id=jp.co.ccc.Tsite) | なし（ストアを開く） | ストアを開く：試した候補：https://tpoint-app.onelink.me/RxPQ/vulagz8y / tpoint:// / vpoint:// / tsite:// | 旧Tポイント |
| iAEON（WAON POINT） | [id1565489157](https://apps.apple.com/jp/app/id1565489157) | [jp.co.aeonst.app.myaeon](https://play.google.com/store/apps/details?id=jp.co.aeonst.app.myaeon) | なし（ストアを開く） | ストアを開く：試した候補：iaeon:// / myaeon:// |  |
| ANAマイレージクラブ | [id1091951820](https://apps.apple.com/jp/app/id1091951820) | [jp.co.ana.anamile](https://play.google.com/store/apps/details?id=jp.co.ana.anamile) | `https://ana-mileage-club.go.link/home/?adj_t=1f7gdjvi` | URLスキームで起動：元の根拠：ANA公式サイトのアプリリンク（Adjust）から追跡用の値を除いたもの |  |
| JAL | [id351785536](https://apps.apple.com/jp/app/id351785536) | [jp.co.jal.dom](https://play.google.com/store/apps/details?id=jp.co.jal.dom) | なし（ストアを開く） | ストアを開く：試した候補：jalapp:// / jal:// |  |
| JALマイレージバンク | [id1444599693](https://apps.apple.com/jp/app/id1444599693) | [com.jalglobalwallet.jgw](https://play.google.com/store/apps/details?id=com.jalglobalwallet.jgw) | なし（ストアを開く） | ストアを開く：試した候補：jmb:// / jalglobalwallet:// |  |
| Coke ON | [id1088184021](https://apps.apple.com/jp/app/id1088184021) | [com.coke.cokeon](https://play.google.com/store/apps/details?id=com.coke.cokeon) | なし（ストアを開く） | ストアを開く：試した候補：cokeon:// |  |
| ジハンピ | [id6667104573](https://apps.apple.com/jp/app/id6667104573) | [jp.jihanpi](https://play.google.com/store/apps/details?id=jp.jihanpi) | なし（ストアを開く） | ストアを開く：URLスキームなし（追加時に指定） | サントリーの自販機アプリ |

## コンビニ（4）

| アプリ名 | App Store | Google Play | URLスキーム | テスト結果 | 備考 |
| --- | --- | --- | --- | --- | --- |
| セブン‐イレブン | [id1039171609](https://apps.apple.com/jp/app/id1039171609) | [jp.co.sej.app](https://play.google.com/store/apps/details?id=jp.co.sej.app) | `https://sej-app.onelink.me/UUyB/69d3ef96` | URLスキームで起動：元の根拠：セブン‐イレブン公式サイトのアプリリンク（AppsFlyer OneLink） |  |
| ローソン | [id515191813](https://apps.apple.com/jp/app/id515191813) | [jp.co.lawson.android](https://play.google.com/store/apps/details?id=jp.co.lawson.android) | `lawson://` | URLスキームで起動 |  |
| ミニストップ | [id1572745532](https://apps.apple.com/jp/app/id1572745532) | [jp.co.ministop.officialapp](https://play.google.com/store/apps/details?id=jp.co.ministop.officialapp) | `ministop://` | URLスキームで起動：元の根拠：ミニストップ公式サイトの「アプリを開く」リンク |  |
| NewDays | [id1505966916](https://apps.apple.com/jp/app/id1505966916) | [jp.j_retail](https://play.google.com/store/apps/details?id=jp.j_retail) | なし（ストアを開く） | ストアを開く：試した候補：newdays:// / jretail:// | JR東日本の駅のコンビニ |

## スーパー（9）

| アプリ名 | App Store | Google Play | URLスキーム | テスト結果 | 備考 |
| --- | --- | --- | --- | --- | --- |
| イオンお買物 | [id634744681](https://apps.apple.com/jp/app/id634744681) | [jp.aeonretail.aeon_okaimono](https://play.google.com/store/apps/details?id=jp.aeonretail.aeon_okaimono) | なし（ストアを開く） | ストアを開く：試した候補：aeonokaimono:// / aeon:// |  |
| イオンモール | [id1451676515](https://apps.apple.com/jp/app/id1451676515) | [com.aeonmall.shopping_app](https://play.google.com/store/apps/details?id=com.aeonmall.shopping_app) | なし（ストアを開く） | ストアを開く：試した候補：aeonmall:// |  |
| イトーヨーカドー | [id490936137](https://apps.apple.com/jp/app/id490936137) | [co.jp.itoyokado.chirashi.android](https://play.google.com/store/apps/details?id=co.jp.itoyokado.chirashi.android) | なし（ストアを開く） | ストアを開く：試した候補：itoyokado:// |  |
| 西友 | [id6480396970](https://apps.apple.com/jp/app/id6480396970) | [jp.co.rakuten.netsuper.seiyu](https://play.google.com/store/apps/details?id=jp.co.rakuten.netsuper.seiyu) | なし（ストアを開く） | ストアを開く：試した候補：seiyu:// |  |
| ライフ | [id1427288237](https://apps.apple.com/jp/app/id1427288237) | [jp.co.lifecorp.android.app](https://play.google.com/store/apps/details?id=jp.co.lifecorp.android.app) | なし（ストアを開く） | ストアを開く：試した候補：lifecorp:// / lifeapp:// |  |
| ヤオコー | [id1113941774](https://apps.apple.com/jp/app/id1113941774) | [com.yaoko_net.app](https://play.google.com/store/apps/details?id=com.yaoko_net.app) | なし（ストアを開く） | ストアを開く：試した候補：yaoko:// |  |
| マルエツ | [id592652031](https://apps.apple.com/jp/app/id592652031) | [com.maruetsu.maruetsu_app](https://play.google.com/store/apps/details?id=com.maruetsu.maruetsu_app) | なし（ストアを開く） | ストアを開く：試した候補：maruetsu:// |  |
| ナリタヤ | [id1632606660](https://apps.apple.com/jp/app/id1632606660) | [jp.co.naritayanet.app](https://play.google.com/store/apps/details?id=jp.co.naritayanet.app) | なし（ストアを開く） | ストアを開く：URLスキームなし（追加時に指定） |  |
| 酒のやまや | [id6444199421](https://apps.apple.com/jp/app/id6444199421) | [jp.co.yamaya.yamayapay](https://play.google.com/store/apps/details?id=jp.co.yamaya.yamayapay) | なし（ストアを開く） | ストアを開く：URLスキームなし（追加時に指定） |  |

## ドラッグストア（10）

| アプリ名 | App Store | Google Play | URLスキーム | テスト結果 | 備考 |
| --- | --- | --- | --- | --- | --- |
| マツキヨココカラ | [id6451037644](https://apps.apple.com/jp/app/id6451037644) | [jp.co.matsukiyococokara.app](https://play.google.com/store/apps/details?id=jp.co.matsukiyococokara.app) | なし（ストアを開く） | ストアを開く：試した候補：matsukiyococokara:// / matsukiyo:// |  |
| ウエルシア | [id1095620617](https://apps.apple.com/jp/app/id1095620617) | [jp.co.welcia_yakkyoku.tapps](https://play.google.com/store/apps/details?id=jp.co.welcia_yakkyoku.tapps) | `https://m.e-welcia.com/app/applink/app.html` | URLスキームで起動：元の根拠：ウエルシア公式サイトのアプリリンク |  |
| スギ薬局 | [id853001943](https://apps.apple.com/jp/app/id853001943) | [jp.sugi.sugitomo](https://play.google.com/store/apps/details?id=jp.sugi.sugitomo) | なし（ストアを開く） | ストアを開く：試した候補：sugitomo:// / sugi:// |  |
| ツルハドラッグ | [id1483880235](https://apps.apple.com/jp/app/id1483880235) | [jp.co.tsuruhahd.tsuruhadrug](https://play.google.com/store/apps/details?id=jp.co.tsuruhahd.tsuruhadrug) | なし（ストアを開く） | ストアを開く：試した候補：tsuruhadrug:// / tsuruha:// |  |
| ドラッグイレブン | [id1580679160](https://apps.apple.com/jp/app/id1580679160) | [jp.co.tsuruhahd.drugeleven](https://play.google.com/store/apps/details?id=jp.co.tsuruhahd.drugeleven) | なし（ストアを開く） | ストアを開く：試した候補：drugeleven:// |  |
| ウェルネス | [id1483877486](https://apps.apple.com/jp/app/id1483877486) | [jp.co.tsuruhahd.wellnessdrug](https://play.google.com/store/apps/details?id=jp.co.tsuruhahd.wellnessdrug) | なし（ストアを開く） | ストアを開く：試した候補：wellnessdrug:// |  |
| サンドラッグ | [id953327495](https://apps.apple.com/jp/app/id953327495) | [jp.co.sundrug.android.app](https://play.google.com/store/apps/details?id=jp.co.sundrug.android.app) | なし（ストアを開く） | ストアを開く：試した候補：sundrug:// |  |
| セイムス（SEIMS） | [id1452763620](https://apps.apple.com/jp/app/id1452763620) | [jp.co.fujiyakuhin.seims](https://play.google.com/store/apps/details?id=jp.co.fujiyakuhin.seims) | なし（ストアを開く） | ストアを開く：試した候補：seims:// |  |
| クスリのアオキ | [id1464657112](https://apps.apple.com/jp/app/id1464657112) | [jp.co.kusuriaoki.android.public](https://play.google.com/store/apps/details?id=jp.co.kusuriaoki.android.public) | なし（ストアを開く） | ストアを開く：試した候補：kusuriaoki:// |  |
| クリエイトSD | [id1439769531](https://apps.apple.com/jp/app/id1439769531) | [com.vxtenpoapp.chain.tac01000](https://play.google.com/store/apps/details?id=com.vxtenpoapp.chain.tac01000) | なし（ストアを開く） | ストアを開く：試した候補：createsd:// |  |

## 飲食店（38）

| アプリ名 | App Store | Google Play | URLスキーム | テスト結果 | 備考 |
| --- | --- | --- | --- | --- | --- |
| すかいらーく（ガスト・バーミヤン等） | [id906930478](https://apps.apple.com/jp/app/id906930478) | [jp.co.skylark.app.gusto](https://play.google.com/store/apps/details?id=jp.co.skylark.app.gusto) | なし（ストアを開く） | ストアを開く：試した候補：skylark:// / gusto:// | バーミヤン・ガスト・しゃぶ葉など |
| マクドナルド | [id413618155](https://apps.apple.com/jp/app/id413618155) | [jp.co.mcdonalds.android](https://play.google.com/store/apps/details?id=jp.co.mcdonalds.android) | `mcdonaldsjp://` | URLスキームで起動：元の根拠：マクドナルド公式サイトのアプリリンクに mcdonaldsjp://order が入っている |  |
| スターバックス | [id1113037275](https://apps.apple.com/jp/app/id1113037275) | [com.starbucks.jp](https://play.google.com/store/apps/details?id=com.starbucks.jp) | なし（ストアを開く） | ストアを開く：試した候補：starbucksjp:// / starbucks:// |  |
| モスバーガー | [id390411817](https://apps.apple.com/jp/app/id390411817) | [jp.co.mos.MosBurger](https://play.google.com/store/apps/details?id=jp.co.mos.MosBurger) | `https://mosapp.go.link/5z3oU` | URLスキームで起動：元の根拠：モスバーガー公式サイトのアプリリンク（Adjust） |  |
| ケンタッキー | [id519131315](https://apps.apple.com/jp/app/id519131315) | [jp.dreambrain.adiorama](https://play.google.com/store/apps/details?id=jp.dreambrain.adiorama) | `kfcjapan://` | URLスキームで起動 |  |
| バーガーキング | [id1456118550](https://apps.apple.com/jp/app/id1456118550) | [jp.co.burgerkingjapan](https://play.google.com/store/apps/details?id=jp.co.burgerkingjapan) | なし（ストアを開く） | ストアを開く：試した候補：burgerkingjapan:// / burgerking:// |  |
| ミスタードーナツ | [id955641819](https://apps.apple.com/jp/app/id955641819) | [jp.co.duskin.misdocardapps](https://play.google.com/store/apps/details?id=jp.co.duskin.misdocardapps) | なし（ストアを開く） | ストアを開く：試した候補：misdo:// / misterdonut:// |  |
| サーティワン（31Club） | [id910133705](https://apps.apple.com/jp/app/id910133705) | [jp.co.br31ice.android.thirtyoneclub](https://play.google.com/store/apps/details?id=jp.co.br31ice.android.thirtyoneclub) | なし（ストアを開く） | ストアを開く：試した候補：thirtyoneclub:// / br31:// |  |
| コメダ珈琲店 | [id1667214457](https://apps.apple.com/jp/app/id1667214457) | [jp.co.komeda.ua.android](https://play.google.com/store/apps/details?id=jp.co.komeda.ua.android) | なし（ストアを開く） | ストアを開く：試した候補：komeda:// |  |
| ドトール（DVC） | [id1445398358](https://apps.apple.com/jp/app/id1445398358) | [jp.co.doutor.dvc](https://play.google.com/store/apps/details?id=jp.co.doutor.dvc) | なし（ストアを開く） | ストアを開く：試した候補：doutor:// / dvc:// |  |
| タリーズ | [id1517333828](https://apps.apple.com/jp/app/id1517333828) | [jp.co.tullys.app](https://play.google.com/store/apps/details?id=jp.co.tullys.app) | なし（ストアを開く） | ストアを開く：試した候補：tullys:// |  |
| プロント | [id1387756178](https://apps.apple.com/jp/app/id1387756178) | [li.yapp.app610DFF23](https://play.google.com/store/apps/details?id=li.yapp.app610DFF23) | なし（ストアを開く） | ストアを開く：試した候補：pronto:// |  |
| 吉野家 | [id1131084339](https://apps.apple.com/jp/app/id1131084339) | [com.yoshinoya.android.yoshinoya_official](https://play.google.com/store/apps/details?id=com.yoshinoya.android.yoshinoya_official) | なし（ストアを開く） | ストアを開く：試した候補：yoshinoya:// |  |
| すき家 | [id1452441389](https://apps.apple.com/jp/app/id1452441389) | [jp.co.zensho.sukiyamoap](https://play.google.com/store/apps/details?id=jp.co.zensho.sukiyamoap) | なし（ストアを開く） | ストアを開く：試した候補：sukiya:// |  |
| 松屋 | [id662011115](https://apps.apple.com/jp/app/id662011115) | [jp.co.matsuyafoods.officialapp.dis](https://play.google.com/store/apps/details?id=jp.co.matsuyafoods.officialapp.dis) | `matsuya://` | URLスキームで起動 |  |
| なか卯 | [id1489893366](https://apps.apple.com/jp/app/id1489893366) | [jp.co.zensho.nakau](https://play.google.com/store/apps/details?id=jp.co.zensho.nakau) | なし（ストアを開く） | ストアを開く：試した候補：nakau:// |  |
| くら寿司 | [id942355925](https://apps.apple.com/jp/app/id942355925) | [jp.co.kura_corpo](https://play.google.com/store/apps/details?id=jp.co.kura_corpo) | なし（ストアを開く） | ストアを開く：試した候補：kurasushi:// / kura:// |  |
| スシロー | [id551682016](https://apps.apple.com/jp/app/id551682016) | [jp.co.akindo_sushiro.sushiroapp](https://play.google.com/store/apps/details?id=jp.co.akindo_sushiro.sushiroapp) | なし（ストアを開く） | ストアを開く：試した候補：https://sushiro.onelink.me/16ns/54b6bfa6 / sushiro:// |  |
| はま寿司 | [id1523009390](https://apps.apple.com/jp/app/id1523009390) | [com.hamazushi.hamanavi](https://play.google.com/store/apps/details?id=com.hamazushi.hamanavi) | `hamazushi://` | URLスキームで起動 |  |
| かっぱ寿司 | [id1207944667](https://apps.apple.com/jp/app/id1207944667) | [jp.kappasushi.app](https://play.google.com/store/apps/details?id=jp.kappasushi.app) | なし（ストアを開く） | ストアを開く：試した候補：kappasushi:// |  |
| 丸亀製麺 | [id587248280](https://apps.apple.com/jp/app/id587248280) | [com.toridoll.marugame.android](https://play.google.com/store/apps/details?id=com.toridoll.marugame.android) | なし（ストアを開く） | ストアを開く：試した候補：marugame:// |  |
| CoCo壱番屋 | [id611124786](https://apps.apple.com/jp/app/id611124786) | [com.cocoichiapp.app](https://play.google.com/store/apps/details?id=com.cocoichiapp.app) | なし（ストアを開く） | ストアを開く：試した候補：cocoichi:// |  |
| 餃子の王将 | [id1350345771](https://apps.apple.com/jp/app/id1350345771) | [jp.co.ohsho.app](https://play.google.com/store/apps/details?id=jp.co.ohsho.app) | なし（ストアを開く） | ストアを開く：試した候補：ohsho:// |  |
| 大阪王将 | [id1526408310](https://apps.apple.com/jp/app/id1526408310) | [jp.osakaohsho.eatandapp](https://play.google.com/store/apps/details?id=jp.osakaohsho.eatandapp) | なし（ストアを開く） | ストアを開く：試した候補：osakaohsho:// |  |
| 大戸屋 | [id1477602455](https://apps.apple.com/jp/app/id1477602455) | [li.yapp.app750BCBF7](https://play.google.com/store/apps/details?id=li.yapp.app750BCBF7) | なし（ストアを開く） | ストアを開く：試した候補：ootoya:// |  |
| やよい軒 | [id1435578241](https://apps.apple.com/jp/app/id1435578241) | [jp.co.yayoiken.app](https://play.google.com/store/apps/details?id=jp.co.yayoiken.app) | なし（ストアを開く） | ストアを開く：試した候補：yayoiken:// |  |
| びっくりドンキー | [id6498982583](https://apps.apple.com/jp/app/id6498982583) | [com.bikkuridonkeyRenewal](https://play.google.com/store/apps/details?id=com.bikkuridonkeyRenewal) | なし（ストアを開く） | ストアを開く：試した候補：bikkuridonkey:// |  |
| ココス | [id1333019957](https://apps.apple.com/jp/app/id1333019957) | [jp.cocoweb](https://play.google.com/store/apps/details?id=jp.cocoweb) | なし（ストアを開く） | ストアを開く：試した候補：cocoweb:// / cocos:// |  |
| ほっともっと | [id1497475671](https://apps.apple.com/jp/app/id1497475671) | [li.yapp.appADFA6026](https://play.google.com/store/apps/details?id=li.yapp.appADFA6026) | なし（ストアを開く） | ストアを開く：試した候補：hottomotto:// |  |
| シャトレーゼ | [id844024333](https://apps.apple.com/jp/app/id844024333) | [jp.co.chateraise.android.members](https://play.google.com/store/apps/details?id=jp.co.chateraise.android.members) | なし（ストアを開く） | ストアを開く：試した候補：chateraise:// |  |
| ビアードパパ | [id1671711621](https://apps.apple.com/jp/app/id1671711621) | [itogo_beardpapaapp_android.itogo.jp.beardpapaapp_app](https://play.google.com/store/apps/details?id=itogo_beardpapaapp_android.itogo.jp.beardpapaapp_app) | なし（ストアを開く） | ストアを開く：試した候補：beardpapa:// |  |
| Rocket Now | [id6739188587](https://apps.apple.com/jp/app/id6739188587) | [com.cpone.customer](https://play.google.com/store/apps/details?id=com.cpone.customer) | なし（ストアを開く） | ストアを開く：URLスキームなし（追加時に指定） | フードデリバリー |
| Uber Eats | [id1058959277](https://apps.apple.com/jp/app/id1058959277) | [com.ubercab.eats](https://play.google.com/store/apps/details?id=com.ubercab.eats) | なし（ストアを開く） | ストアを開く：URLスキームなし（追加時に指定） | フードデリバリー |
| ゼッテリア | [id6478645600](https://apps.apple.com/jp/app/id6478645600) | [jp.co.zensho.zet](https://play.google.com/store/apps/details?id=jp.co.zensho.zet) | なし（ストアを開く） | ストアを開く：URLスキームなし（追加時に指定） |  |
| 築地銀だこ | [id6596748968](https://apps.apple.com/jp/app/id6596748968) | [com.syn_inc.gindaco](https://play.google.com/store/apps/details?id=com.syn_inc.gindaco) | なし（ストアを開く） | ストアを開く：URLスキームなし（追加時に指定） |  |
| 天丼てんや | [id1627185131](https://apps.apple.com/jp/app/id1627185131) | [com.newuplink.chain.tac905994](https://play.google.com/store/apps/details?id=com.newuplink.chain.tac905994) | なし（ストアを開く） | ストアを開く：URLスキームなし（追加時に指定） |  |
| とんかつ専門店かつや | [id6473354781](https://apps.apple.com/jp/app/id6473354781) | [li.yapp.appE3F5CA73](https://play.google.com/store/apps/details?id=li.yapp.appE3F5CA73) | なし（ストアを開く） | ストアを開く：URLスキームなし（追加時に指定） |  |
| ラーメン山岡家 | [id6466559589](https://apps.apple.com/jp/app/id6466559589) | [li.yapp.appCC40B910](https://play.google.com/store/apps/details?id=li.yapp.appCC40B910) | なし（ストアを開く） | ストアを開く：URLスキームなし（追加時に指定） |  |

## 買い物・家電（27）

| アプリ名 | App Store | Google Play | URLスキーム | テスト結果 | 備考 |
| --- | --- | --- | --- | --- | --- |
| ユニクロ | [id460989014](https://apps.apple.com/jp/app/id460989014) | [com.uniqlo.ja.catalogue](https://play.google.com/store/apps/details?id=com.uniqlo.ja.catalogue) | `uniqlo://` | URLスキームで起動：元の根拠：ユニクロ公式サイトのアプリリンク（AppsFlyer OneLink） |  |
| GU | [id504542019](https://apps.apple.com/jp/app/id504542019) | [com.osharemaker](https://play.google.com/store/apps/details?id=com.osharemaker) | `https://gu-japan.onelink.me/8JY3/d70a43e8` | URLスキームで起動：元の根拠：GU公式サイトのアプリリンク（AppsFlyer OneLink） |  |
| 無印良品 | [id631993791](https://apps.apple.com/jp/app/id631993791) | [net.muji.passport.android](https://play.google.com/store/apps/details?id=net.muji.passport.android) | `mujipassport://` | URLスキームで起動 |  |
| ニトリ | [id814928018](https://apps.apple.com/jp/app/id814928018) | [jp.co.nitori](https://play.google.com/store/apps/details?id=jp.co.nitori) | なし（ストアを開く） | ストアを開く：試した候補：nitori:// |  |
| しまむら | [id732775964](https://apps.apple.com/jp/app/id732775964) | [biz.shopup.shimamura](https://play.google.com/store/apps/details?id=biz.shopup.shimamura) | なし（ストアを開く） | ストアを開く：試した候補：shimamura:// |  |
| ABC-MART | [id1299642230](https://apps.apple.com/jp/app/id1299642230) | [mobi.abcmart.app](https://play.google.com/store/apps/details?id=mobi.abcmart.app) | なし（ストアを開く） | ストアを開く：試した候補：abcmart:// |  |
| ロフト | [id930782276](https://apps.apple.com/jp/app/id930782276) | [jp.co.loft.fanapp](https://play.google.com/store/apps/details?id=jp.co.loft.fanapp) | なし（ストアを開く） | ストアを開く：試した候補：loft:// |  |
| ハンズ | [id934694176](https://apps.apple.com/jp/app/id934694176) | [net.hands.handsapp](https://play.google.com/store/apps/details?id=net.hands.handsapp) | なし（ストアを開く） | ストアを開く：試した候補：handsclub:// / hands:// |  |
| ブックオフ | [id1369113760](https://apps.apple.com/jp/app/id1369113760) | [jp.co.bookoff.bookoffapp](https://play.google.com/store/apps/details?id=jp.co.bookoff.bookoffapp) | なし（ストアを開く） | ストアを開く：試した候補：bookoff:// |  |
| ヨドバシ | [id549050663](https://apps.apple.com/jp/app/id549050663) | [com.yodobashi.iShop](https://play.google.com/store/apps/details?id=com.yodobashi.iShop) | `yodobashi://` | URLスキームで起動 |  |
| ビックカメラ | [id518593576](https://apps.apple.com/jp/app/id518593576) | [com.biccamera.android.mobile](https://play.google.com/store/apps/details?id=com.biccamera.android.mobile) | なし（ストアを開く） | ストアを開く：試した候補：biccamera:// |  |
| ヤマダデジタル | [id364504659](https://apps.apple.com/jp/app/id364504659) | [jp.co.unisys.android.yamadamobile](https://play.google.com/store/apps/details?id=jp.co.unisys.android.yamadamobile) | `ymd://` | URLスキームで起動：元の根拠：2012年のURLスキーム一覧（YAMADAモバイル） |  |
| エディオン | [id434823849](https://apps.apple.com/jp/app/id434823849) | [com.edion.members](https://play.google.com/store/apps/details?id=com.edion.members) | なし（ストアを開く） | ストアを開く：試した候補：edion:// |  |
| ケーズデンキ | [id968245112](https://apps.apple.com/jp/app/id968245112) | [com.ksdenki](https://play.google.com/store/apps/details?id=com.ksdenki) | なし（ストアを開く） | ストアを開く：試した候補：ksdenki:// |  |
| カインズ | [id966865570](https://apps.apple.com/jp/app/id966865570) | [com.cainz.cainz](https://play.google.com/store/apps/details?id=com.cainz.cainz) | なし（ストアを開く） | ストアを開く：試した候補：cainz:// |  |
| コメリ | [id823464130](https://apps.apple.com/jp/app/id823464130) | [com.komeri.komeriapl](https://play.google.com/store/apps/details?id=com.komeri.komeriapl) | なし（ストアを開く） | ストアを開く：試した候補：komeri:// |  |
| DCM | [id1072655144](https://apps.apple.com/jp/app/id1072655144) | [jp.co.dcm_hldgs](https://play.google.com/store/apps/details?id=jp.co.dcm_hldgs) | なし（ストアを開く） | ストアを開く：試した候補：dcm:// |  |
| ムラサキスポーツ | [id1386508876](https://apps.apple.com/jp/app/id1386508876) | [jp.co.murasakisportsapp](https://play.google.com/store/apps/details?id=jp.co.murasakisportsapp) | `murasakisports://` | URLスキームで起動：2026/10/30 利用者が確認したURLスキーム |  |
| 快活CLUB | [id958083643](https://apps.apple.com/jp/app/id958083643) | [jp.kaikatsu.official](https://play.google.com/store/apps/details?id=jp.kaikatsu.official) | `jpkaikatsuofficial://` | URLスキームで起動：2026/10/30 利用者が確認したURLスキーム |  |
| CHARGESPOT | [id1272481966](https://apps.apple.com/jp/app/id1272481966) | [com.chachastation.app](https://play.google.com/store/apps/details?id=com.chachastation.app) | なし（ストアを開く） | ストアを開く：URLスキームなし（追加時に指定） | モバイルバッテリーのレンタル |
| 東京靴流通センター | [id1349142968](https://apps.apple.com/jp/app/id1349142968) | [li.yapp.appB76130B0](https://play.google.com/store/apps/details?id=li.yapp.appB76130B0) | なし（ストアを開く） | ストアを開く：URLスキームなし（追加時に指定） |  |
| 三井ショッピングパーク | [id921446819](https://apps.apple.com/jp/app/id921446819) | [jp.co.mf_shogyo.mitsui_shopping_park](https://play.google.com/store/apps/details?id=jp.co.mf_shogyo.mitsui_shopping_park) | なし（ストアを開く） | ストアを開く：URLスキームなし（追加時に指定） | ららぽーと・三井アウトレットパークなど |
| ゲオ | [id590190880](https://apps.apple.com/jp/app/id590190880) | [jp.co.geoonline.app](https://play.google.com/store/apps/details?id=jp.co.geoonline.app) | なし（ストアを開く） | ストアを開く：URLスキームなし（追加時に指定） |  |
| ハードオフ | [id1358188035](https://apps.apple.com/jp/app/id1358188035) | [jp.co.hardoff.renk.app.official.prd](https://play.google.com/store/apps/details?id=jp.co.hardoff.renk.app.official.prd) | なし（ストアを開く） | ストアを開く：URLスキームなし（追加時に指定） |  |
| 眼鏡市場 | [id1536503941](https://apps.apple.com/jp/app/id1536503941) | [jp.meganeichiba.mobile](https://play.google.com/store/apps/details?id=jp.meganeichiba.mobile) | なし（ストアを開く） | ストアを開く：URLスキームなし（追加時に指定） |  |
| ラウンドワン | [id432455516](https://apps.apple.com/jp/app/id432455516) | [com.Round1](https://play.google.com/store/apps/details?id=com.Round1) | なし（ストアを開く） | ストアを開く：URLスキームなし（追加時に指定） |  |
| #C-pla（シープラ） | [id6450071897](https://apps.apple.com/jp/app/id6450071897) | [li.yapp.appAF4B724D](https://play.google.com/store/apps/details?id=li.yapp.appAF4B724D) | なし（ストアを開く） | ストアを開く：URLスキームなし（追加時に指定） | カプセルトイ専門店 |

## カラオケ（6）

| アプリ名 | App Store | Google Play | URLスキーム | テスト結果 | 備考 |
| --- | --- | --- | --- | --- | --- |
| カラオケまねきねこ | [id1434510930](https://apps.apple.com/jp/app/id1434510930) | [jp.co.koshidaka.manekinekoapp](https://play.google.com/store/apps/details?id=jp.co.koshidaka.manekinekoapp) | なし（ストアを開く） | ストアを開く：試した候補：manekineko:// |  |
| カラオケマック | [id1457474843](https://apps.apple.com/jp/app/id1457474843) | [com.karaokemac](https://play.google.com/store/apps/details?id=com.karaokemac) | なし（ストアを開く） | ストアを開く：URLスキームなし（追加時に指定） |  |
| カラオケ館 | [id1341634219](https://apps.apple.com/jp/app/id1341634219) | [jp.karaokekan.karakan.karakan](https://play.google.com/store/apps/details?id=jp.karaokekan.karakan.karakan) | なし（ストアを開く） | ストアを開く：URLスキームなし（追加時に指定） |  |
| ビッグエコー | [id1289531868](https://apps.apple.com/jp/app/id1289531868) | [jp.co.dkkaraoke.app.bigecho](https://play.google.com/store/apps/details?id=jp.co.dkkaraoke.app.bigecho) | なし（ストアを開く） | ストアを開く：URLスキームなし（追加時に指定） |  |
| 歌広場 | [id858157888](https://apps.apple.com/jp/app/id858157888) | 配信なし | なし（ストアを開く） | ストアを開く：URLスキームなし（追加時に指定） | iPhoneのみ（Android版は配信停止中） |
| カラオケBanBan | [id6717609264](https://apps.apple.com/jp/app/id6717609264) | [com.karaoke_banban.app](https://play.google.com/store/apps/details?id=com.karaoke_banban.app) | なし（ストアを開く） | ストアを開く：URLスキームなし（追加時に指定） |  |

## ガソリンスタンド（3）

| アプリ名 | App Store | Google Play | URLスキーム | テスト結果 | 備考 |
| --- | --- | --- | --- | --- | --- |
| ENEOS | [id1612229796](https://apps.apple.com/jp/app/id1612229796) | [com.eneos.ssapp](https://play.google.com/store/apps/details?id=com.eneos.ssapp) | なし（ストアを開く） | ストアを開く：試した候補：eneos:// |  |
| 出光（idemitsuアプリ） | [id1434377869](https://apps.apple.com/jp/app/id1434377869) | [jp.showa_shell_dmp.shellpass](https://play.google.com/store/apps/details?id=jp.showa_shell_dmp.shellpass) | `idemitsu://` | URLスキームで起動 |  |
| コスモ石油 | [id994587658](https://apps.apple.com/jp/app/id994587658) | [jp.co.cosmo_oil](https://play.google.com/store/apps/details?id=jp.co.cosmo_oil) | なし（ストアを開く） | ストアを開く：試した候補：cosmo:// / cosmooil:// |  |
