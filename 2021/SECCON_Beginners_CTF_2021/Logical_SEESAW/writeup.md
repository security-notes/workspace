# Writeup

以下のPythonプログラムが与えられる。

```py
from Crypto.Util.number import *
from random import random, getrandbits
from flag import flag

flag = bytes_to_long(flag.encode("utf-8"))
length = flag.bit_length()
key = getrandbits(length)
while not length == key.bit_length():
    key = getrandbits(length)

flag = list(bin(flag)[2:])
key = list(bin(key)[2:])

cipher_L = []

for _ in range(16):
    cipher = flag[:]
    m = 0.5
    
    for i in range(length):
        n = random()
        if n > m:
            cipher[i] = str(eval(cipher[i] + "&" + key[i]))
            
    cipher_L.append("".join(cipher))


print("cipher =", cipher_L)
```

`flag`をバイナリに変換し、1ビットごとにランダムで`and`を取った結果が`cipher`になる。

```
例：
flag = [0, 1, 1, 0]

random1 = [1, 0, 1, 0]
cipher1 = [0, 0, 1, 0]

random2 = [0, 1, 0, 1]
cipher2 = [0, 1, 0, 0]
```

ランダムに`and`を取っても、`flag`のビットが`0`ならば必ず`cipher`のビットも`0`になることを利用すればよい。

`cipher`の`n`ビット目を見てすべて`0`ならば、`flag`の`n`ビット目は`0`だと確定する。

```py
from Crypto.Util.number import long_to_bytes

cipher = ...(省略)

plain = ''
for l in range(len(cipher[0])):
    check = ''
    for i in range(len(cipher)):
        check += str(cipher[i][l])
    if check == '0'*len(cipher):
        plain += '0'
    else:
        plain += '1'
print(long_to_bytes(int(plain,2)))
```

<!-- ctf4b{Sh3_54w_4_SEESAW,_5h3_54id_50} -->
