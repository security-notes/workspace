# Writeup

テキストが与えられる。

テキストのパターンを調べると、以下の2つのテキストから構成されていることが分かった。

```
9mTfc:..Zt9mTZ_:IIcu9mTN[9km7D
9mTfc:..Zt9mTZ_:K0o09mTN[9km7D
9mTfc:..Zt9mTZ_:Jj8< (最後のみ)
```

`IIcu...`を`0`,`K0o0...`を`1`として変換してみる。

`} = 0x7d = 0b01111101`だとすると、最後は`1`になるはずなので、`Jj8<`も`1`に変換する。

```py
from Crypto.Util.number import *

c = open('round-the-bases','r').read()
c = c.split('7D')

b = ''
for d in c:
    if 'IIcu' in d:
        b += '0'
    else:
        b += '1'

print(long_to_bytes(int(b,2)))
```

<!-- flag{w0w_th4t_w4s_4ll_wr4pp3d_up} -->
