# Writeup

プログラムが与えられる。

目的は`self.numbers`に`1337i`というキーを追加することである。

```py
def _secret(self):
    if '1337i' in self.numbers:
        self.request.sendall(b'Congratulations!\n')
        self.request.sendall(f'The flag is {flag}\n'.encode())
```

単に`1. Save a number`を選び、`Imaginary part`に`1337`と入力するだけだと、`{'0 + 1337i': [0, 1337]}`となってしまう。

なので、`3. Import numbers`という機能で追加するしかない。

ECBモードで暗号化されているため、以下のような数字を登録して`4. Export numbers`を選ぶと、

```
{"1 + 1337i": [1, 1337], "2 + 1337i": [2, 1337]}
Exported:
4f28683f2f57729cdda1220188cbb6ec1ae0f99d13681f1a16b282ca8c2f291b23be3d1a5622cb4e9a869d88324d8f678db4341b6d2b363abdc9d13de3042f42

{"3 + 1337i": [3, 1337], "2 + 1337i": [2, 1337]}
Exported:
c098b4c6563e552de7971a2f0daeaa671ae0f99d13681f1a16b282ca8c2f291b23be3d1a5622cb4e9a869d88324d8f678db4341b6d2b363abdc9d13de3042f42
```

前半部分が異なり、後半部分が同じなので、暗号化された後も前半の16バイトだけが異なる値が得られる。

つまり、16バイトずつ区切ったときに次のようになるような暗号文を生成してつなぎ合わせればよい。

```
~~~~~~~~~~~~], "
1337i": [~~~~~~~
~~~~~~~~~~~~~~]}
```

`{"11111111111 + 1337i": [11111111111, 1337]}`

```
{"11111111111 + 
1337i": [111111  // GET!
11111, 1337]}    // GET!

↓

1ae8561ba030b0e6866580c7cdb05508
c2d4a53f38d83a1b4cf782f97a51929d　// GET!
cd5fe366f2cad5f88dcb41586bf94409  // GET!
```

`{"1 + 1i": [1, 1], "1 + 222222i": [1, 222222], "1 + 3i": [1, 3]}`

```
{"1 + 1i": [1, 1
], "1 + 222222i"
: [1, 222222], " // GET!
1 + 3i": [1, 3]}

↓

d29268dd3000f6ee96f01cc762f8cb64 // use
fa5e55fcf3ec1bb203e6d2ba6b2ab798 // use
f70400a70d1b78b43c659ae81015c9e9 // GET!
bb11b201b2f2aee10e80ed5fbe30f90a
8db4341b6d2b363abdc9d13de3042f42
```
つなぎ合わせて、`3. Import numbers`する。

```
1. Save a number
2. Show numbers
3. Import numbers
4. Export numbers
0. Exit
> 3
Exported String> d29268dd3000f6ee96f01cc762f8cb64fa5e55fcf3ec1bb203e6d2ba6b2ab798f70400a70d1b78b43c659ae81015c9e9c2d4a53f38d83a1b4cf782f97a51929dcd5fe366f2cad5f88dcb41586bf94409
Imported.
--------------------------------------------------
1 + 1i: (1, 1)
1 + 222222i: (1, 222222)
1337i: (11111111111, 1337)
--------------------------------------------------
```

`1337i`が登録できたので`5`を押す。

```
> 5
Congratulations!
The flag is ctf4b{yeah_you_are_a_member_of_imaginary_number_club}
```

<!-- ctf4b{yeah_you_are_a_member_of_imaginary_number_club} -->
