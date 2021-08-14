# Writeup

以下のプログラムが与えられる。

```py
from Crypto.Util.number import getPrime, bytes_to_long

flag = bytes_to_long(open("/challenge/flag.txt", "rb").read())

def genkey():
    e = 0x10001
    p, q = getPrime(256), getPrime(256)
    if p <= q:
      p, q = q, p
    n = p * q
    pubkey = (e, n)
    privkey = (p, q)
    return pubkey, privkey

def encrypt(m, pubkey):
    e, n = pubkey
    c = pow(m, e, n)
    return c

pubkey, privkey = genkey()
c = encrypt(flag, pubkey)

hint = pubkey[1] % (privkey[1] - 1)
print('pubkey:', pubkey)
print('hint:', hint)
print('c:', c)
```

RSA暗号の問題で、`e,n,c` と `hint = n % (q-1)` が既知である。

```
pubkey: (65537, 8233844853736079846340942338892377350084205826692932262262169655906024996611709932668810597429977504654174681615645717480946467295158630669046073907212183)
hint: 41162916934005887239397941494469703620898846542249479175280452807025539991659
c: 2668213429910053210439086430709560263484415254994522634947359490234264025445117346305280609718185533536116506975101248392127837369553056944962889943997393
```

`hint = n % (q-1), p > q`より、

```
hint = p * q % (q-1)
hint = p % (q-1)
hint + i * (q-1) = p
p > q, p < 2q より、i = 1
q(hint + (q-1)) = n
q^2 + (hint - 1)q - n = 0
```

が成り立つ。`q`についての二次方程式を解けばよい。

```py
# sage
from Crypto.Util.number import *

e = 65537
n = 8233844853736079846340942338892377350084205826692932262262169655906024996611709932668810597429977504654174681615645717480946467295158630669046073907212183
hint = 41162916934005887239397941494469703620898846542249479175280452807025539991659
c = 2668213429910053210439086430709560263484415254994522634947359490234264025445117346305280609718185533536116506975101248392127837369553056944962889943997393

x = var('x')
s = solve(x^2 + (hint - 1)*x - n == 0, x)
q = int(s[0].right())
p = n // q
assert p*q == n and p >= q

d = power_mod(e, -1, (p-1)*(q-1))
m = power_mod(c, d, n)
print(long_to_bytes(m))
```

<!-- rarctf{g3n3r1c_m4th5_equ4t10n_th1ng_ch4ll3ng3_5a174f54e6} -->
