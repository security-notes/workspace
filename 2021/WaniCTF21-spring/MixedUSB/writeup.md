# Writeup

与えられたファイルを`file`コマンドで調べてみる。

```
$ file MixedUSB.img 
MixedUSB.img: DOS/MBR boot sector
```

試しに`strings`を`grep`してみるとフラグがあった。

```
$ strings MixedUSB.img | grep FLAG
FLAG{mixed_file_allocation_table}
```

<!-- FLAG{mixed_file_allocation_table} -->
