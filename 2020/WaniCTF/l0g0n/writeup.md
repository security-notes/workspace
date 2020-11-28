# writeup

```bash
$ nc l0g0n.wanictf.org 50002
Challenge (hex) > 53fd
Server challenge: b69221d059469d35
Credential (hex) > 5ffa
Authentication Failed... 🥺
```

サーバーサイドのプログラムを読むと、入力する`client_credential`とサーバーで計算する`server_credential`が一致すればよいことがわかる。

```py
client_challenge = input("Challenge (hex) > ")

client_credential = input("Credential (hex) > ")

server_credential = cipher.encrypt(client_challenge)
if client_credential == server_credential:
    print(f"OK! {flag}")
```

肝心の`server_credential`の計算部分だが、計算結果は`plaintext`の長さに依存していることがわかる（★）。そのため、`client_challenge`が1バイトのとき、`server_credential`も1バイトになってしまう。

```py
class AES_CFB8:
    def __init__(self, key):
        self.block_size = 16
        self.cipher = AES.new(key, AES.MODE_ECB)

    def encrypt(self, plaintext: bytes, iv=bytes(16)):
        iv_plaintext = iv + plaintext
        ciphertext = bytearray()

        for i in range(len(plaintext)): # ★
            X = self.cipher.encrypt(iv_plaintext[i : i + self.block_size])[0]
            Y = plaintext[i]
            ciphertext.append(X ^ Y)
        return bytes(ciphertext)
```

つまり、`client_challenge`を1バイトとしたとき、`server_credential`は`\x00`~`\xff`のいずれかになるので、1/256の確率で一致する。

以下を実行してフラグを取得。1/256が引ければ終了。

```py
from pwn import *

conn = remote('l0g0n.wanictf.org',50002)

cnt = 0
while True:
    cnt += 1
    #　client_challenge -> server_credential
    conn.sendline('00') # any 1byte
    conn.recvuntil('>')
    # client_credential
    conn.sendline('50') # any 1byte
    conn.recvuntil('>')

    msg = str(conn.recvline())
    print(cnt,msg)
    if 'OK' in msg: # 1/256
        break

conn.close()
```