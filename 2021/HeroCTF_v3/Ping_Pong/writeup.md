# Writeup

`PING`,`PONG`という単語が書かれたテキストが与えられる。

`I`を`1`,`O`を`0`と見立てて2進数にし、文字列に変換してみるとフラグになっていた。

```py
import os

binary = ""
with open(os.path.dirname(__file__)+"/output.txt","r") as f:
    text = f.readline()
    while text:
        if "PING" in text:
            binary += "1"
        else :
            binary += "0"
        text = f.readline()
print(bytearray.fromhex(hex(int(binary,2))[2:]).decode())
```

<!-- Hero{p1n6_p0n6_15_fun} -->
