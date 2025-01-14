# Writeup

与えられたプログラムのクラス名にあるように、`岡本-内山暗号システム`が使われている。

このシステムでは、`n,g,h`を公開鍵、`r`を`2`から`n-1`までの乱数として、平文`m`を以下のように暗号化する。

![\begin{align*}
c = g^m h^r \mod n
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Ac+%3D+g%5Em+h%5Er+%5Cmod+n%0A%5Cend%7Balign%2A%7D%0A)

ここで、

![\begin{align*}
c_1 * c_2 &= ( g^{m_1} h^{r_1} ) * ( g^{m_2} h^{r_2} ) \mod n \\
&= g^{(m_1+m_2)} h^{(r_1+r_2)} \mod n
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Ac_1+%2A+c_2+%26%3D+%28+g%5E%7Bm_1%7D+h%5E%7Br_1%7D+%29+%2A+%28+g%5E%7Bm_2%7D+h%5E%7Br_2%7D+%29+%5Cmod+n+%5C%5C%0A%26%3D+g%5E%7B%28m_1%2Bm_2%29%7D+h%5E%7B%28r_1%2Br_2%29%7D+%5Cmod+n%0A%5Cend%7Balign%2A%7D%0A)

が成り立つので、暗号文を乗算した結果を復号すると、加算された平文を手に入れることができる。(準同型暗号の性質)

よって、`flag`の暗号文と`0x01`の暗号文を乗算して復号化すれば、`flag + 0x01`の平文を手に入れることができる。`flag`そのままが平文だとチェックで弾かれることを考慮して`0x00`でなく`0x01`を選ぶ。


```py
from pwn import *

io = remote('oucs.cry.wanictf.org','50010')

plaintext = ""
ciphertext = ""
n = 0

# Get n
io.recvuntil('> ')
io.sendline('4')
exec(io.recvline().decode('utf-8')) # n

# Get c1
io.recvuntil('> ')
io.sendline('1')
exec(io.recvline().decode('utf-8'))
flag_encrypt = ciphertext

# Get c2
io.recvuntil('> ')
io.sendline('2')
io.recvuntil('> ')
io.sendline('0x01')
exec(io.recvline().decode('utf-8'))
one_encrypt = ciphertext

# decrypt c1*c2 mod n
io.recvuntil('> ')
io.sendline('3')
io.recvuntil('> ')
io.sendline(str(hex((flag_encrypt * one_encrypt)%n)))
exec(io.recvline().decode('utf-8'))

plaintext = hex(plaintext - 1)
print(bytes.fromhex(plaintext[2:]))
```

[参考]

* [Okamoto–Uchiyama cryptosystem - Wikipedia](https://en.wikipedia.org/wiki/Okamoto%E2%80%93Uchiyama_cryptosystem)

* [準同型暗号 - Wikipedia](https://ja.wikipedia.org/wiki/%E6%BA%96%E5%90%8C%E5%9E%8B%E6%9A%97%E5%8F%B7)

* [高専セキュリティコンテスト2017:Crypto:400ptのwriteup](https://kyumina.hatenablog.com/entry/2018/03/05/020100)

<!-- FLAG{OU_d0es_n0t_repre53nt_Osaka_University_but_Okamoto-Uchiyama} -->