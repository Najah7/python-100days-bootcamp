# Low about Scraping
- Linkedin vs HiQの裁判が大きな判断の基準に
- プライベート使用など非営利の場合はOKだという考え方が一般的。営利目的の場合はグレーゾーン。
- 認証後に見れるデータのスクレピングはイリーガル（Instagram、Twitterなど、認証した人のみしか見れないもの。）

※Webサイトの情報だけでなく、YouTubeの動画なども同様

# CAPTCHA or reCAPTCHA
ロボットではないか確認するやつ。スクレーピング対策で使われる。

# Ethics
法律も大事だが、結局のところ倫理的な視点が大事だよ
- Public API First：勝手にPublic APIの情報を拡散するものを作ったり使ったりするのは良くない。本来(公式)のWeb APIを使うべき。
- Respect the Web Owner：robots.txtというエンドポントでスクレーピングしないでほしいエンドポントやリクエストの間隔を明示している場合もある。ownerの指示には従って
- Limit your Rate：スクレーピングの間隔などを考えて、負荷を与えないようにする。