# Writeup

画像ファイルが与えられる。

`zsteg`を使って調べたところ、文字列が隠されていた。

```
$ zsteg zstegosaurus.png
b1,r,lsb,xy         .. text: "h15_n@m3_i5nt_g3rard"
b4,rgb,msb,xy       .. text: ["w" repeated 10 times]
```

<!-- bcactf{h15_n@m3_i5nt_g3rard} -->
