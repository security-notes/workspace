# Writeup

サーバーで生成された`0~500000` のランダムな値を当てればフラグが得られそう。

間違えたときに、大きいか小さいかの情報が得られるので二分探索で絞り込んでいく。

20回トライでき、`2^20 > 500000` なので確実に特定できる。

以下のプログラムを実行するとフラグが得られる。

```py
from pwn import *

conn = remote('number.wanictf.org',60000)
n_min, n_max = 0, 500000

while True:

    conn.recvuntil('input:')
    mid = (n_min + n_max) // 2
    conn.sendline(str(mid))

    msg = str(conn.recvlines(2))

    if 'small' in msg:
        n_min = mid
    elif 'big' in msg:
        n_max = mid
    else:
        print(msg)
        break
```

<!-- FLAG{b1n@ry_5e@rch_1s_v3ry_f@5t} -->