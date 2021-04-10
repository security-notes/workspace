# Writeup

`os.urandom(2)`さえ分かれば復号化できるので、総当たりで調べる。

```py
import os
import zlib
def keystream(key):
    index = 0
    while 1:
        index+=1
        if index >= len(key):
            key += zlib.crc32(key).to_bytes(4,'big')
        yield key[index]
with open(os.path.dirname(__file__)+"/enc","rb") as f:
    cipher = f.read()
    for n in range(256*256):
        plaintext = []
        k = keystream(n.to_bytes(2,'big'))
        for i in cipher:
            plaintext.append(i ^ next(k))
        if b'actf{' in bytes(plaintext) :
            print(bytes(plaintext))
```

<!-- actf{low_entropy_keystream} -->