# Writeup

暗号化のプログラムを読む。

```py
key = "REDACTED"
flag = "FAKE{this_is_fake_flag}"

assert len(key) == len(flag) == 57
assert flag.startswith("FLAG{") and flag.endswith("}")
assert key[0:3] * 19 == key # (1)


def encrypt(s1, s2):
    assert len(s1) == len(s2)

    result = ""
    for c1, c2 in zip(s1, s2):
        result += chr(ord(c1) ^ ord(c2)) #(2)
    return result


ciphertext = encrypt(flag, key)
print(ciphertext, end="")
```

(2) より、`flag`と`key`に対して1文字ずつXORを計算していることが分かる。そして、(1) より、`key`は3文字の繰り返しであることも分かる。

XORは同じものを2回演算すると元に戻る性質があるので、`ciphertext`の先頭3文字と`plaintext`の先頭3文字`FLA`をXOR演算して`key`を求めることができる。

`key`が求まったら、`key`を19回繰り返したものと`ciphertext`をXOR演算して`plaintext`を求めることができる。

以下のプログラムを実行してフラグを取得。

```py
# ファイル読み込み
with open('./output.txt') as f:
    ciphertext = f.read()

# s1,s2に対してXOR演算を行う
def decrypt(s1, s2):
    assert len(s1) == len(s2)

    result = ""
    for c1, c2 in zip(s1, s2):
        result += chr(ord(c1) ^ ord(c2))
    return result

# 先頭3文字のXORをとってKeyを計算
key = decrypt(ciphertext[0:3],'FLA')

# Keyの繰り返しと暗号文のXORを計算
plaintext = decrypt(key*19,ciphertext)

print(plaintext)
```

