# Writeup

fileコマンドを使うと、pythonをコンパイルしたファイルであることがわかる。

```bash
$ file snek 
snek: python 3.7 byte-compiled
```

デコンパイルする。

```bash
$ cp snek snek.pyc
$ uncompyle6 snek.pyc
```

```py
# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.18 (default, Mar  8 2021, 13:02:45) 
# [GCC 9.3.0]
# Warning: this version of Python has problems handling the Python 3 "byte" type in constants properly.

# Embedded file name: snek.py
# Compiled at: 2021-04-08 15:24:05
# Size of source mod 2**32: 834 bytes
"""
Written for RITSEC CTF 2021
Author: knif3
Flag: RITSEC{}

TODO: Finish this challenge
"""

class d(object):

    def __init__(self, password):
        self.password = password.encode()
        self.decrypt = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 95, 82, 83, 123, 97, 108, 108, 95, 104, 105, 36, 36, 95, 97, 110, 100, 95, 110, 48, 95, 98, 105, 116, 51, 125]

    def __eq__(self, other):
        if self.password == bytes(self.decrypt):
            print('!flag')
            return True
        return False


x = input('Enter my name: ')
a = d(x)
if a == x:
    print('IS_THIS_THE_FLAG??')
    print('NOPE')
else:
    print('WRONG')
# okay decompiling snek.pyc
```

`decrypt`部分がASCIIコードのようなので、文字列に置き換える。

後半部分にフラグ文字列が出現する。

```py
decrypt = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 95, 82, 83, 123, 97, 108, 108, 95, 104, 105, 36, 36, 95, 97, 110, 100, 95, 110, 48, 95, 98, 105, 116, 51, 125]

print(''.join([chr(d) for d in decrypt]))
```

<!-- RS{all_hi$$_and_n0_bit3} -->