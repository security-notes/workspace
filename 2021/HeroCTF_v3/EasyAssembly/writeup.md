# Writeup

asmファイルを読み、`input`と`modified`の値を読み取る。

```
# EasyAssembly.c:17:    int input = getInput();
# EasyAssembly.c:19:    modified = input >> 2;
# EasyAssembly.c:21:    if(modified == 1337404)
```

`modified`は`1337404`で、`input`を2ビット右シフトした値であることがわかる。

よって`input`は`1337404`を2ビット左シフトした`5349616`である。

<!-- Hero{5349616:1337404} -->
