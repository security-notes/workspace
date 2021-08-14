# Writeup

以下のプログラムが与えられる。

```py
from random import getrandbits
from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long

def keygen(): # normal rsa key generation
  primes = []
  e = 3
  for _ in range(2):
    while True:
      p = getPrime(1024)
      if (p - 1) % 3:
        break
    primes.append(p)
  return e, primes[0] * primes[1]

def pad(m, n): # pkcs#1 v1.5
  ms = long_to_bytes(m)
  ns = long_to_bytes(n)
  if len(ms) >= len(ns) - 11:
    return -1
  padlength = len(ns) - len(ms) - 3
  ps = long_to_bytes(getrandbits(padlength * 8)).rjust(padlength, b"\x00")
  return int.from_bytes(b"\x00\x02" + ps + b"\x00" + ms, "big")

def encrypt(m, e, n): # standard rsa
  res = pad(m, n)
  if res != -1:
    print(f"c: {pow(m, e, n)}")
  else:
    print("error :(", "message too long")

menu = """
[1] enc()
[2] enc(flag)
[3] quit
"""[1:]

e, n = keygen()
print(f"e: {e}")
print(f"n: {n}")
while True:
  try:
    print(menu)
    opt = input("opt: ")
    if opt == "1":
      encrypt(int(input("msg: ")), e, n)
    elif opt == "2":
      encrypt(bytes_to_long(open("/challenge/flag.txt", "rb").read()), e, n)
    elif opt == "3":
      print("bye")
      exit(0)
    else:
      print("idk")
  except Exception as e:
    print("error :(", e)
```

中身は`e=3`のRSA暗号である。`pad`関数は暗号化に使われていないため、無視してもよい。

おそらく暗号文が長いため、3乗根を取るだけではうまくいかない。

接続しなおせば、`n`が異なる`c`が複数個分かるるため、Håstad's Broadcast Attackを使って平文
を求める。

```py
# sage
from pwn import *
import re
from Crypto.Util.number import *

e, n, c = 3, [], []

for _ in range(3):
    io = remote('193.57.159.27', 28572)
    io.recvline() # e
    n.append(int(re.search(r'n: (\d+)' , str(io.recvline())).group(1)))

    io.recvuntil('opt: ')
    io.sendline('2')
    c.append(int(re.search(r'c: (\d+)' , str(io.recvline())).group(1)))
    io.close()

x = CRT_list(c,n)

print(long_to_bytes(x^(1/e)))
```

<!-- rarctf{https://cdn.discordapp.com/attachments/751845431063085160/866641917714235392/unknown.png_8538853c64} -->
