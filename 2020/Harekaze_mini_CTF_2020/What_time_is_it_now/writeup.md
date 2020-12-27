# Writeup

指定のサイトにアクセスすると、現在時刻が表示される。

![](img/2020-12-26-15-25-49.png)

ソースコードを読むと、どうやら`date`コマンドを実行して、その結果を表示しているようだ。`date`の出力フォーマットを`format`パラメータで指定している。

```php
<?php
if (isset($_GET['source'])) {
  highlight_file(__FILE__);
  exit;
}

$format = isset($_REQUEST['format']) ? (string)$_REQUEST['format'] : '%H:%M:%S';
$result = shell_exec("date '+" . escapeshellcmd($format) . "' 2>&1");
?>

// (略)

<h1 class="jumbotron-heading"><span class="text-muted">It's</span> <?= isset($result) ? $result : '?' ?><span class="text-muted">.</span></h1>
```

`format`に実行したいコマンドを入れ、`date '+`.`%Y-%m-%d' ; ls '`.`'`みたいにすれば良さそうだが、`escapeshellcmd`によってほとんどの特殊文字がエスケープされてしまうので不可能。(ただし、対になっている`'`,`"`は可能)

* [PHPマニュアル:escapeshellcmd:シェルのメタ文字をエスケープする](https://php.plus-server.net/function.escapeshellcmd.html)

[GTFOBins](https://gtfobins.github.io/)で`date`コマンドについて調べると、`-f`オプションでファイル読み込みができることが分かった。

ファイル名は決め打ちで、`format`に`' -f /flag'`を与えたところ、`date '+' -f /flag'' 2>&1`が実行され、フラグが表示された。

* http://harekaze2020.317de643c0ae425482fd.japaneast.aksapp.io/what-time-is-it-now/?format=%27%20-f%20/flag%27

<!-- HarekazeCTF{1t's_7pm_1n_t0ky0} -->