# Writeup

0,1と書かれたCSVファイルが与えられるので、つなぎ合わせて文字列に変換する。

```py
import os

f = open(os.path.dirname(__file__)+'/mis-binary/binary.csv').read()
f = f.replace("\n","")
print(bytes.fromhex(hex(int(f,2))[2:]))
```

<!-- FLAG{the_basic_knowledge_of_communication} -->