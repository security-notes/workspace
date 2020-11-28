問題ページ： https://sql1.wanictf.org/index.php?year=2011

今まで見たアニメのリストをデータベースに登録したよ。間違えて秘密の情報（FLAG）もデータベースに登録しちゃったけど、たぶん誰にも見られないし大丈夫だよね。

(Hint)

SQL injectionの問題です。

URLの「year=」の後に続く数字(年号)をSQL injectionを起こすような文字列に変更するとFLAGが表示されます。

一部使えない文字もあるのでソースコード(index.php)を参考に考えてみてください。

必要に応じてデータベースのスキーマ(1_schema.sql)も参考にしてください。

(注意)

sql-chall-1.zipは問題を解くために必須の情報ではなく、docker-composeを利用してローカルで問題環境を再現するためのものです。

興味のある方は利用してみてください。

[index.php](https://score.wanictf.org/storage/oshaubxunljhmdwulgubalcphkfghsmz/index.php)

[1_schema.sql](https://score.wanictf.org/storage/fdmeaslfyzjpmjhitqkypmvgirsktnqa/1_schema.sql)

[sql-chall-1.zip](https://score.wanictf.org/storage/xpvdcxybtelbaodfpisxojiczcakdwxa/sql-chall-1.zip)

Writer : nkt