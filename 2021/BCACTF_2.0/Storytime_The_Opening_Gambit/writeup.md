# Writeup

実行ファイルが与えられる。

```bash
$ file story
story: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=ccea544c84172f60a939819e4416fdd108982090, for GNU/Linux 3.2.0, not stripped
```

stringsコマンドでフラグが見つかった。

```bash
$ strings story | grep bcactf
bcactf{w0ol_m4k3s_str1ng_ziv4mk3ca91b}
```

<!-- bcactf{w0ol_m4k3s_str1ng_ziv4mk3ca91b} -->
