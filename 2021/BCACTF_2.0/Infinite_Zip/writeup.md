# Writeup

zipファイルが与えられる。

試しに解凍してみると、さらにzipファイルが出てきた。unzipを何度も繰り返す必要がある。

以下のコマンドで再帰的に解凍していったところ、画像ファイルが手に入った。

```bash
$ while [ "`find . -type f -name '*.zip' | wc -l`" -gt 0 ]; do find -type f -name "*.zip" -exec unzip -- '{}' \; -exec rm -- '{}' \;; done
```

![](./extract/flag.png)

```
bcactf{n0_f14g_4_u}
```

と思ったら、これはダミーでstringsコマンドで本当のフラグが得られる。

```bash
$ strings flag.png | grep bcactf
    <rdf:li>bcactf{z1p_1n51d3_4_z1p_4_3v3r}</rdf:li>
```

<!-- bcactf{z1p_1n51d3_4_z1p_4_3v3r} -->
