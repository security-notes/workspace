# Writeup

サブスクライブした topic の内容を表示する仕組みになっている。

![](img/2020-11-22-12-56-09.png)

さすがに `nkt/flag` ではダメだった。

![](img/2020-11-22-12-57-17.png)

すべてをサブスクライブに指定したいので、MQTTのワイルドカードについて調べると、`#`を使えばよいことが分かった。

[参考]

* http://devcenter.magellanic-clouds.com/learning/mqtt-spec.html

`#`をサブスクライブするとフラグが取得できた。

`top/secret/himitu/daiji/mitara/dame/zettai/flag` にあるらしい。

![](img/2020-11-22-13-06-22.png)

<!-- FLAG{mq77_w1ld_c4rd!!!!_af5e29cb23} -->