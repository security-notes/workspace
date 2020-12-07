# Writeup

**Enigma**で暗号化された文字列が出力されるので、これらをヒントに復号化すればよい。

Enigmaの初期設定に使われる値がすべてランダムなので、まともに総当たりしても解けない。

rotors: 8\*8\*8 通り  
reflector: 4 通り  
ring_settings: 26\*26\*26 通り  
plugboard: ? 通り  
initial_value: 26\*26\*26 通り  

Enigma暗号には、平文と暗号文で同じ位置に同じアルファベットが登場しないという特徴がある。

* https://ja.wikipedia.org/wiki/エニグマ_(暗号機)#ある種の不完全性_(noncrashing)

よって暗号文をたくさん生成し、各位置において登場しないアルファベットを絞り込んでいけばよい。

```py
from string import ascii_uppercase as UC

cipherlist = []
with open('./output.txt') as f:
    while True:
        cipher = f.readline()
        if len(cipher) < 1:
            break
        cipherlist.append(cipher[0:-1]) # exclude \n

for i in range(17):
    string = [char[i] for char in cipherlist]
    diff = set(UC)-set(string)
    print(list(diff)[0],end='')
```

フラグの文字列が出力される。形式は`pbctf{UPPERCASEPLAINTEXT}`である。

<!-- pbctf{FATALFLAWINENIGMA} -->

