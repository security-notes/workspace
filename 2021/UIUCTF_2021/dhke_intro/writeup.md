# Writeup

以下のプログラムが与えられる。


```py
import random
from Crypto.Cipher import AES

# generate key
gpList = [ [13, 19], [7, 17], [3, 31], [13, 19], [17, 23], [2, 29] ]
g, p = random.choice(gpList)
a = random.randint(1, p)
b = random.randint(1, p)
k = pow(g, a * b, p)
k = str(k)

# print("Diffie-Hellman key exchange outputs")
# print("Public key: ", g, p)
# print("Jotaro sends: ", aNum)
# print("Dio sends: ", bNum)
# print()

# pad key to 16 bytes (128bit)
key = ""
i = 0
padding = "uiuctf2021uiuctf2021"
while (16 - len(key) != len(k)):
    key = key + padding[i]
    i += 1
key = key + k
key = bytes(key, encoding='ascii')

with open('flag.txt', 'rb') as f:
    flag = f.read()

iv = bytes("kono DIO daaaaaa", encoding = 'ascii')
cipher = AES.new(key, AES.MODE_CFB, iv)
ciphertext = cipher.encrypt(flag)

print(ciphertext.hex())
```

`iv`は固定で、`key`がランダムである。

しかし、`key`の生成に使われている`k`の値を見てみると、

```py
gpList = [ [13, 19], [7, 17], [3, 31], [13, 19], [17, 23], [2, 29] ]
g, p = random.choice(gpList)
a = random.randint(1, p)
b = random.randint(1, p)
k = pow(g, a * b, p)
k = str(k)
```

`mod p`の値が使われているので、`0~30`の値をとることが分かる。

31パターンなら総当たりで良いので、以下を実行してフラグが得られた。

```py
from Crypto.Cipher import AES

for k in range(31):
    k = str(k)

    # pad key to 16 bytes (128bit)
    key = ""
    i = 0
    padding = "uiuctf2021uiuctf2021"
    while (16 - len(key) != len(k)):
        key = key + padding[i]
        i += 1
    key = key + k
    key = bytes(key, encoding='ascii')

    with open('output.txt', 'rb') as f:
        out = bytes.fromhex(f.read().decode())

    iv = bytes("kono DIO daaaaaa", encoding = 'ascii')
    cipher = AES.new(key, AES.MODE_CFB, iv)
    ciphertext = cipher.decrypt(out)

    if b'uiuctf' in ciphertext:
        print(f'{key = }')
        print(f'{ciphertext = }')
```

<!-- uiuctf{omae_ha_mou_shindeiru_b9e5f9} -->