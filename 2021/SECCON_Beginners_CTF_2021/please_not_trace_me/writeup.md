# Writeup

実行ファイルが与えられる。Ghidraで解析してみる。

switch文での分岐があり、変数`local_48`が怪しいので、以下の順番で実行されるように書き換える。

![](img/2021-05-22-23-40-49.png)

switch文は`jmp rax`なので、`rax`を飛ばしたいアドレスにすればよい。

```
# 0x1011ff = main addr from Ghidra

switch
b *(main+(0x10126e-0x1011ff))
// jmp rax

1. malloc
set $rax=*(main+(0x101494-0x1011ff))

2. generate_key
set $rax=*(main+(0x101270-0x1011ff))

3. rc4
set $rax=*(main+(0x101289-0x1011ff))
```

`R8`にフラグがあった。

![](img/2021-05-22-23-39-31.png)

<!-- ctf4b{d1d_y0u_d3crypt_rc4?} -->
