# Writeup

[ルール30 - Wikipedia](https://ja.wikipedia.org/wiki/%E3%83%AB%E3%83%BC%E3%83%AB30) の初期状態と整数`n`が与えられるので、`n`番目の状態を求める。

ルールとして、両端はつなげて変換することになっている。

```
例)
100000100000001 (初期状態) 0th state

11000001000000011 (両端を補完する)

010001110000011 (3ビットずつ取り出しルールに従って変換) 1st state

10100011100000110 (両端を補完する)

011011001000110 (3ビットずつ取り出しルールに従って変換) 2nd state

...
```

そのままのアルゴリズムだとO(n)であり`GetPrime(1024)`番目を計算するには工夫が必要である。

何回か調べたところ46番目の変換と1501番目の変換結果が毎回同じになるという法則があったので、それを利用して計算量を小さくする。

```py
from pwn import *

rule = {'111':'0', '110':'0', '101':'0', '100':'1', 
        '011':'1', '010':'1', '001':'1', '000':'0'}

def rule30(state, gen):
    # Found Gen(46) = Gen(1501)
    if gen > 1500:
        gen = gen % 1455
    for _ in range(gen):
        next_state = ""
        state = state[-1] + state + state[0]
        for i in range(15):
            next_state += rule[state[i:i+3]]
        state = next_state
    return state

io = remote('automaton.mis.wanictf.org','50020')
io.recvuntil('(press enter key to continue)')
io.sendline()
for _ in range(3):
    io.recvuntil('= ')
    init = io.recvline().decode('utf-8').replace('\n','')
    io.recvuntil('= ')
    gen = int(io.recvline().decode('utf-8'))
    print(rule30(init,gen))
    io.recvuntil('> ')
    io.sendline(rule30(init,gen))
    print(io.recvline())
print(io.recvline())
io.close()
```

<!-- FLAG{W3_4w4rd_y0u_d0c70r473_1n_Fu7ur3_S1gh7} -->
