# Writeup

SQLインジェクションをしてフラグを入手する。ただし、使えるクエリ文字列には制限がある。特殊記号の前に`\`が付与される。

```php
//preg_replaceで危険な記号を処理する。
$pattern = '/([^a-zA-Z0-9])/';
$replace = '\\\$0';
$year = preg_replace($pattern, $replace, $year);

//クエリを作成する。
$query = "SELECT * FROM anime WHERE years = $year";
```

クエリパラメータに`years`を与える。すると、`SELECT * FROM anime WHERE years = years`が実行されてすべての`anime`カラムが取得できる。

* https://sql2.wanictf.org/index.php?year=years

<!-- FLAG{5ql_ch4r_cf_ca87b27723} -->

(特殊文字を使うという固定観念に縛られて、思いのほか結構悩んだ。)