# Writeup

実行ファイルが与えられる。

```bash
$ file story2
story2: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=1e3cbcc533556d3e4ce1edb0848a21cef1b10365, for GNU/Linux 3.2.0, not stripped
```

Ghidraで解析する。以下の部分が怪しい。

```c
  while (local_724 < 0x25) {
    *(char *)((long)&local_38 + (long)local_724) =
         (char)local_724 + (char)(*(int *)((long)&local_718 + (long)local_724 * 4) >> 1);
    local_724 = local_724 + 1;
  }
```

```
*(char *)((long)&local_38 + (long)local_724)

↓

001013fa 88 54 05 d0     MOV        byte ptr [RBP + RAX*0x1 + -0x30],DL
```

この命令の後にBreakpointを設定しDLの値を監視していく。

```gdb
b *main+(0x1013fe-0x1011e4)

disp $dl
```

```py
dl = [0x62,0x63,0x61,0x63,0x74,0x66,0x7b,0x74,0x68,0x34,0x74,0x5f,0x30,0x74,0x68,0x33,0x72,0x5f,0x64,0x72,0x34,0x67,0x30,0x6e,0x5f,0x37,0x36,0x66,0x77,0x38,0x6b,0x63,0x31,0x6c,0x61,0x76,0x7d]

for d in dl:
    print(chr(d),end='')
```

<!-- bcactf{th4t_0th3r_dr4g0n_76fw8kc1lav} -->
