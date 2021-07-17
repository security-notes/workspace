# Writeup

[secure.mc.ax](https://secure.mc.ax/) にアクセスするとログイン画面が表示される。

与えられたソースコードを読むと、UsernameとPasswordはBase64でエンコードされていることが分かる。

```js
db.exec(`INSERT INTO users (username, password) VALUES (
    '${btoa('admin')}',
    '${btoa(crypto.randomUUID)}'
)`);
```

試しに`admin : admin`でログインすると以下のように表示される。

![](img/2021-07-10-17-09-25.png)

入力フォームからのリクエストでは、`A-Za-z0-9+/=`の文字列しか使用できない。

しかし、実際にBase64に変換しているのはフロントエンドのJavaScript部分なので、POSTリクエストを書き換えて SQL injection を行うことができる。

![](img/2021-07-10-17-16-56.png)

![](img/2021-07-10-17-03-42.png)

<!-- flag{50m37h1n6_50m37h1n6_cl13n7_n07_600d} -->
