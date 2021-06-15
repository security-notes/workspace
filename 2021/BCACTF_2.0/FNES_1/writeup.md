# Writeup

以下のプログラムが与えられる。

```py
#!/usr/bin/env python3
import random
import math
import time
import binascii
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA


with open("flag.txt", "r") as f:
    flag = f.read().strip().encode("ascii")

with open("key.txt", "r") as f:
    key = int(f.read().strip())

target_query = "Open sesame... Flag please!"

print("""
Welcome to your Friendly Neighborhood Encryption Service (FNES)!
If you and a friend both run this service at the same time,
you should be able to send messages to each other!
Here are the steps:
1. Friends A and B connect to the server at the same time (you have about a five second margin)
2. Friend A encodes a message and sends it to Friend B
3. Friend B decodes the message, encodes their reply, and sends it to Friend A
4. Friend A decodes the reply, rinse and repeat
Make sure to not make any mistakes, though, or your keystreams might come out of sync...
PS: For security reasons, there are four characters you aren't allowed to encrypt. Sorry!
""", flush=True)

tempkey = SHA.new(int(key + int(time.time() / 10)).to_bytes(64, 'big')).digest()[0:16]
cipher = ARC4.new(tempkey)

while True:
    print("Would you like to encrypt (E), decrypt (D), or quit (Q)?", flush=True)
    l = input(">>> ").strip().upper()
    if (len(l) > 1):
        print("You inputted more than one character...", flush=True)
    elif (l == "Q"):
        print("We hope you enjoyed!", flush=True)
        exit()
    elif (l == "E"):
        print("What would you like to encrypt?", flush=True)
        I = input(">>> ").strip()
        if (set(I.lower()) & set("flg!")): # You're not allowed to encrypt any of the characters in "flg!"
            print("You're never getting my flag!", flush=True)
            exit()
        else:
            print("Here's your message:", flush=True)
            c = str(binascii.hexlify(cipher.encrypt(str.encode(I))))[2:-1]
            print(c, flush=True)
    elif (l == "D"):
        print("What was the message?", flush=True)
        I = input(">>> ").strip()
        m = str(cipher.decrypt(binascii.unhexlify(I)))[2:-1]
        if (m == target_query):
            print("Passphrase accepted. Here's your flag:", flush=True)
            print(str(flag)[2:-1], flush=True)
            exit()
        else:
            print("Here's the decoded message:", flush=True)
            print(m, flush=True)
```

decryptした結果が`"Open sesame... Flag please!"`となるような暗号文を与えれば良い。

```py
target_query = "Open sesame... Flag please!"

    m = str(cipher.decrypt(binascii.unhexlify(I)))[2:-1]
        if (m == target_query):
            print("Passphrase accepted. Here's your flag:", flush=True)
            print(str(flag)[2:-1], flush=True)
            exit()
```

ただし、`flg!`が入った文字列は暗号化してもらえない。

```py
        print("What would you like to encrypt?", flush=True)
        I = input(">>> ").strip()
        if (set(I.lower()) & set("flg!")): # You're not allowed to encrypt any of the characters in "flg!"
            print("You're never getting my flag!", flush=True)
            exit()
```

また、`key`が分からないので、同じ`tempkey`を使って再現するのは無理そう。

```py
with open("key.txt", "r") as f:
    key = int(f.read().strip())

tempkey = SHA.new(int(key + int(time.time() / 10)).to_bytes(64, 'big')).digest()[0:16]
cipher = ARC4.new(tempkey)
```

平文と暗号文に規則性はないか確かめるために、試しに`\x00\x00....` と `\x01\x01...` を暗号化してみる。

```py
from pwn import *
context.log_level = 'error'

target_query = "Open sesame... Flag please!"

io = remote('crypto.bcactf.com', '49153')
io.recvuntil('Would you like to encrypt (E), decrypt (D), or quit (Q)?')
io.sendline('E')
io.recvuntil('>>> ')
c = '\x00' * len(target_query)
io.sendline(c)
io.recvuntil("Here's your message:\n")
msg = io.recvline().strip().decode('utf-8')
print(msg)

io = remote('crypto.bcactf.com', '49153')
io.recvuntil('Would you like to encrypt (E), decrypt (D), or quit (Q)?')
io.sendline('E')
io.recvuntil('>>> ')
c = '\x01' * len(target_query)
io.sendline(c)
io.recvuntil("Here's your message:\n")
msg = io.recvline().strip().decode('utf-8')
print(msg)
```

上記プログラムを実行したところ、以下の結果が得られた。

```
51d8cc259ef9571e849162d35e4d61b54b12213b77242780d6a3f1
50d9cd249ff8561f859063d25f4c60b44a13203a76252681d7a2f0
```

`C(\x00\x00...)` XOR `0101...` = `C(\x01\x01...)` となることが分かった。

```
51d8cc259ef9571e849162d35e4d61b54b12213b77242780d6a3f1
XOR
010101010101010101010101010101010101010101010101010101
=
50d9cd249ff8561f859063d25f4c60b44a13203a76252681d7a2f0
```

よって、`C(\x00\x00...)` XOR `target_query#hex` を計算すれば `C(target_query)` が得られる。

```py
from pwn import *
context.log_level = 'error'

target_query = "Open sesame... Flag please!"

# 1
io = remote('crypto.bcactf.com', '49153')
io.recvuntil('Would you like to encrypt (E), decrypt (D), or quit (Q)?')
io.sendline('E')
io.recvuntil('>>> ')
c = '\x00' * len(target_query)
io.sendline(c)
io.recvuntil("Here's your message:\n")
msg = io.recvline().strip().decode('utf-8')

# 2
io = remote('crypto.bcactf.com', '49153')
io.recvuntil('Would you like to encrypt (E), decrypt (D), or quit (Q)?')
io.sendline('D')
io.recvuntil('>>> ')
c = xor(bytes.fromhex(msg), target_query.encode('utf-8')).hex()
io.sendline(c)

io.interactive()

io.close()
```

<!-- bcactf{why-would-you-attack-your-FNES????-4x35rcg} -->
