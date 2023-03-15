# CSS（Cascading Style Sheets）

### CSSを使う理由
- HTMLでレイアウトまでするととてもHTMLの構造が複雑になるから

### スタイリングの方法
- Inline：HTML要素に直接
- Internal：同じファイルの<style>タグの中で
- External:style.cssなど違うファイルで

### CSSの文法
selector {property: value;}
- selctor:who
- property:what
- value:how

### idとクラスセレクタの使う基準
- class：複数のもの（グループ）に使う。一つの要素に複数指定可能。
- id：一意のものに使う。指定できる名前は１つの要素に１つのみ
※基本的にクラスでもの足りるので。そしてデバッグの手間が増えるから、idは使わない方がいい。

### CSSの代表的なバグ
- ファイルの読み込みに関するミス
- 詳細度（優先度）のミス

### 要素の分類
- インライン
- ブロック
- インラインブロック

### 参考になるサイト情報
- [MDM(CSS)](https://developer.mozilla.org/ja/docs/Web/CSS)
- [default CSS](https://www.w3schools.com/cssref/css_default_values.php)
- [CSSに便利なaddon](https://microsoftedge.microsoft.com/addons/detail/debug-css/chlajdlkaknpjjgodghbapjhogoigegh)
