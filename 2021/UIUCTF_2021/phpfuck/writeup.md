# Writeup

http://phpfuck.chal.uiuc.tf にアクセスする。

`show_source(__FILE__)`と`phpinfo()`が実行されている。

```php
<?php
// Flag is inside ./flag.php :)
($x=str_replace("`","",strval($_REQUEST["x"])))&&strlen(count_chars($x,3))<=5?print(eval("return $x;")):show_source(__FILE__)&&phpinfo();
```

`./flag.php`があると書いてあるので、http://phpfuck.chal.uiuc.tf/flag.php にアクセスしてソースコードを見るとフラグが書かれていた。

```
<? /* uiuctf{pl3as3_n0_m0rE_pHpee} */ ?>
No flag for you!
```

<!-- uiuctf{pl3as3_n0_m0rE_pHpee} -->
