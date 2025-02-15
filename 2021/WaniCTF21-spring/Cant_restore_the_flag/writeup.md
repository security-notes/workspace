# Writeup

与えられたプログラムは以下。

```py
from Crypto.Util.number import bytes_to_long

with open("flag.txt", "rb") as f:
    flag = f.read()
flag = bytes_to_long(flag)

assert flag <= 10 ** 103

upper_bound = 300
while True:
    try:
        mod = int(input("Mod > "))
        if mod > upper_bound:
            print("Don't cheat 🤪")
            continue

        result = flag % mod
        print(result)
    except Exception:
        print("Bye 👋")
        break
```

入力した数字での剰余がわかるので、中国人剰余定理を使って元の数字を計算する。

300以下の素数に対しての剰余を貰い、SageMathの`CRT_list`を使って解いた。

* https://doc.sagemath.org/html/en/reference/rings_standard/sage/arith/misc.html

```py
import os
os.environ['PWNLIB_NOTERM'] = 'True' # sage & pwntools

from pwn import *
import re

io = remote('crt.cry.wanictf.org','50000')
P = Primes()

p = 1
rets, primes = [], []
while True:
    p = P.next(p)
    if p > 300:
        break
    io.recvuntil('Mod > ')
    io.sendline(str(p))
    ret = int(re.sub(r'\D','',io.recvline().decode('utf-8')))
    rets.append(ret)
    primes.append(p)

flag = CRT_list(rets,primes)

assert flag <= 10 ** 103

print(bytes.fromhex(hex(flag)[2:]))
```

<!-- FLAG{Ch1n3s3_r3m@1nd3r_7h30r3m__so_u5eful} -->
