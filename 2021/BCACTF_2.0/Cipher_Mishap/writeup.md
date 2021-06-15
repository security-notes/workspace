# Writeup

以下のテキストが与えられる。

```
126-Y, 113-N, 122-N, 130-N, 117-N, 107-N, 137, 114-N, 127-Y, 137, 113-Y, 104-N, 131-N, 110-N, 137, 105-Y, 110-N, 110-N, 121-Y, 137, 131-Y, 114-N, 112-N, 110-N, 121-N, 110-N, 125-N, 110-N, 137, 114-Y, 121-N, 126-N, 127-N, 110-N, 104-N, 107-N
```

`0 ~ 7`の数字しか出現しないので8進数とみて変換する。

`-Y`がCaps Lockの有効、`-N`が無効を表しているとすると、大文字と小文字が区別される。

```
Vkrxog_lW_Kdyh_EhhQ_Yljhqhuh_Lqvwhdg
```

さらにROTしてみたところ、ROT23で意味の通る英文になった。

```
Should_iT_Have_BeeN_Vigenere_Instead
```

solverは以下の通りである。

```py
import string

UPPER = string.ascii_uppercase * 2

l = open('text.txt','r').read().replace('\n','').split(', ')

plain = ''
for s in l:
    ss = s.split('-')
    c = chr(int(ss[0],8))
    if(len(ss) == 2):
        c = UPPER[UPPER.find(c) + 23] # ROT23
        if(ss[1] == 'Y'):
            plain += c
        else:
            plain += c.lower()
    else:
        plain += c

print(plain)
```

<!-- bcactf{Should_iT_Have_BeeN_Vigenere_Instead} -->
