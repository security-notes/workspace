# Writeup

非常に長いテキストファイルが与えられる。

CyberChefに入れてみたところ、Base64で繰り返しエンコードされているものらしい。

Base64デコードを繰り返し行うプログラムを書く。

```py
import base64
import os

text = open(os.path.dirname(__file__)+"/cipher.txt").read()
cnt = 1

while True:
    text = base64.b64decode(text)
    if b'dctf{' in text:
        print(cnt, text)
        break
    cnt += 1
```

42回目のBase64デコードでフラグが得られた。

<!-- dctf{Th1s_l00ks_4_lot_sm4ll3r_th4n_1t_d1d} -->
