# Writeup

ページにアクセスすると、チェックボックスとボタンがある。

![](img/2021-05-15-03-52-18.png)

チェックを入れてボタンを押すと`Not authorized`と表示される。

通信を見てみると、POSTで`auth`というパラメーターを送信していることが分かった。

![](img/2021-05-15-03-54-53.png)

ページのソースをよく見ると`<input hidden name="auth" value="0">`と書いてあるので`value="1"`にしてボタンを押したところ、フラグが表示された。

```html
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    }
    fieldset{
    border: 1px solid;
    width: 400px;
    margin:auto;
    }
    </style>
</head>
<body>
    <form action='flag' method='post'>
        <fieldset>
            <input type="checkbox" name="flag" value="1">
            I want flag!<br>
            <input hidden name="auth" value="0">
            <input type='submit' name='Submit' value='Submit' />
        </fieldset>
    </form>
</body>
</html>
```

![](img/2021-05-15-03-56-54.png)

<!-- dctf{w3b_c4n_b3_fun_r1ght?} -->
