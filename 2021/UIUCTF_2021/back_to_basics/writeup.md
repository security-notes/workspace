# Writeup

以下のプログラムと暗号文が与えられる。

```py
from Crypto.Util.number import long_to_bytes, bytes_to_long
from gmpy2 import mpz, to_binary
#from secret import flag, key

ALPHABET = bytearray(b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#")

def base_n_encode(bytes_in, base):
	return mpz(bytes_to_long(bytes_in)).digits(base).upper().encode()

def base_n_decode(bytes_in, base):
	bytes_out = to_binary(mpz(bytes_in, base=base))[:1:-1]
	return bytes_out

def encrypt(bytes_in, key):
	out = bytes_in
	for i in key:
            print(i)
            out = base_n_encode(out, ALPHABET.index(i))
	return out

def decrypt(bytes_in, key):
	out = bytes_in
	for i in key:
		out = base_n_decode(out, ALPHABET.index(i))
	return out

"""
flag_enc = encrypt(flag, key)
f = open("flag_enc", "wb")
f.write(flag_enc)
f.close()
"""
```

暗号化は、

1. 文字列を数字に変換

    * `b'flag' ⇒ 1718378855`

2. 数字をN進数に変換 `(key = b'K')`

    * `1718378855 ⇒ b'K0FF0EB' (K=21進数)`

を繰り返し行う。

よって、復号化は逆の手順をやればよい。復号化した結果がN進数の文字列になるかどうかチェックしていく。

以下のプログラムを実行してフラグが得られた。


```py
from Crypto.Util.number import long_to_bytes, bytes_to_long
from gmpy2 import mpz, to_binary

ALPHABET = bytearray(b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#")

def base_n_encode(bytes_in, base):
	return mpz(bytes_to_long(bytes_in)).digits(base).upper().encode()

def base_n_decode(bytes_in, base):
	bytes_out = to_binary(mpz(bytes_in, base=base))[:1:-1]
	return bytes_out

def encrypt(bytes_in, key):
	out = bytes_in
	for i in key:
            print(i)
            out = base_n_encode(out, ALPHABET.index(i))
	return out

def decrypt(bytes_in, key):
	out = bytes_in
	for i in key:
		out = base_n_decode(out, ALPHABET.index(i))
	return out

# encrypt
"""
flag_enc = encrypt(flag, key)
f = open("flag_enc", "wb")
f.write(flag_enc)
f.close()
"""

# decrypt
flag_enc = open("flag_enc", "rb").read()
key = b''
while True:
    for k in ALPHABET:
        bk = long_to_bytes(k)
        try:
            flag_dec = decrypt(flag_enc, bk)
            if '\\x' not in str(flag_dec):
                key += bk
                flag_enc = flag_dec
                break
        except Exception as e:
            # invalid digits
            pass
    if b'uiuctf' in flag_dec:
        print(flag_dec)
        break
```

<!-- uiuctf{r4DixAL} -->
