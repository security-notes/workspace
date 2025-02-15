# Writeup

RSA暗号の問題。以下のPythonプログラムが与えられる。

```py
from Crypto.Util.number import *
from random import getrandbits
from os import urandom
from flag import flag


def gen_primes(bits, e):
    q = getStrongPrime(bits)
    p = q
    while True:
        p = p-8 # p-8
        phi = (p - 1) * (q - 1)
        if isPrime(p) and GCD(phi, e) != 1:
            break
    return p, q

flag = flag.encode("utf-8") + urandom(64)
flag = bytes_to_long(flag)

e = 17
p, q = gen_primes(512, e)
n = p * q

print("n =", n)
print("e =", e)
print("c =", pow(flag, e, n))
```

`n = q * (q-8k)`となる。512bitの`q`に比べれば`-8k`は非常に小さい値なので、`q`と`q-8k`は近い値であることが分かる。

よって、フェルマー法を用いて`n`を素因数分解する。

* [Fermat's factorization method](https://facthacks.cr.yp.to/fermat.html)

あとは`pow(e,-1,(p-1)(q-1))`で秘密鍵が求められそうだが、`GCD(e,(p-1)(q-1)) != 1`となっているので上手くいかない。

以下のサイトの解法を使う。

* [p - 1 ≡ 0 (mod e) のときの RSA 復号方法](https://y011d4.netlify.app/20201026-not-coprime-e-phi/)

```py
# sage
from Crypto.Util.number import *

def fermatfactor(N):
       if N <= 0: return [N]
       if is_even(N): return [2,N/2]
       a = ceil(sqrt(N))
       while not is_square(a^2-N):
         a = a + 1
       b = sqrt(a^2-N)
       return [a - b,a + b]

if __name__ == '__main__':
    n = 169221770188000341507764005330769042705223611712308424479120192596136318818708135716157255550936563268500310852894489839470320516645317338473018150885997977008925839939560590924435380239519554475266121835753044660177349444503693993991253475530436734034224314165897550185719665717183285653938232013807360458249
    e = 17
    c = 100233131931360278332734341652304555814094487252151131735286074616555402795190797647001889669472290770925839013131356212574455274690422113278015571750653365512998669453161955302008599029919101244702933443124944274359143831492874463245444294673660944786888148517110942002726017336219552279179125115273728023902
    [p,q] = fermatfactor(n)
    
    _lambda = (p-1)*(q-1) // GCD(p-1, q-1)
    assert _lambda % e == 0 or _lambda // e % e != 0
    L = pow(2, _lambda // e, n)
    assert L > 1
    d = pow(e, -1, _lambda // e)
    assert e * d % (_lambda // e) == 1

    for i in range(e):
        tmp_flag = long_to_bytes(pow(c, d, n) * pow(L, i, n) % n)
        if b"ctf4b" in tmp_flag:
            print(tmp_flag)
```

<!-- ctf4b{4r3_y0u_up5id3_d0wn?_Fr0m_6310w?_0r_60th?} -->
