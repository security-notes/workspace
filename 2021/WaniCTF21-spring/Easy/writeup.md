# Writeup

与えられたプログラムは以下。

```py
with open("flag.txt") as f:
    flag = f.read().strip()


A = REDACTED
B = REDACTED

plaintext_space = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_{}"

assert all(x in plaintext_space for x in flag)


def encrypt(plaintext: str, a: int, b: int) -> str:
    ciphertext = ""
    for x in plaintext:
        if "A" <= x <= "Z":
            x = ord(x) - ord("A")
            x = (a * x + b) % 26
            x = chr(x + ord("A"))
        ciphertext += x

    return ciphertext


if __name__ == "__main__":
    ciphertext = encrypt(flag, a=A, b=B)
    print(ciphertext)
```

`encrypt`関数で、plaintextを1文字ずつ別の文字に変換している。

まず、変換の計算に必要な`a`,`b`の値を知る必要があるが、計算途中に`mod 26`されているので、`0 ≦ a,b < 26`の範囲で全探索すればよい。

フラグの先頭`FLAG{`を`encrypt`にいれて、`HLIM{`になるような`a,b`を見つける。

`mod 26`の計算から、`plaintext`のアルファベットと`ciphertext`のアルファベットは1対1対応になるので、最低でも26回`ciphertext`を`encrypt`し続ければどこかで`plaintext`に戻る。

```py
import itertools

def encrypt(plaintext: str, a: int, b: int) -> str:
    ciphertext = ""
    for x in plaintext:
        if "A" <= x <= "Z":
            x = ord(x) - ord("A")
            x = (a * x + b) % 26
            x = chr(x + ord("A"))
        ciphertext += x

    return ciphertext

if __name__ == "__main__":
    ciphertext = "HLIM{OCLSAQCZASPYFZASRILLCVMC}"

    for i,j in itertools.product(range(26),range(26)):
        c = encrypt("FLAG{", a=i, b=j)
        if c == "HLIM{":
            break

    for _ in range(26):
        ciphertext = encrypt(ciphertext,a=i, b=j)
        if "FLAG{" in ciphertext:
            print(ciphertext)
            break
```

<!-- FLAG{WELCOMETOCRYPTOCHALLENGE} -->
