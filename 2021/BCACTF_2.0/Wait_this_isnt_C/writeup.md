# Writeup

実行ファイルが与えられる。

```bash
$ file flag_checker_1
flag_checker_1: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=44db315a94752488b3ace72816fef8393c9db3fd, for GNU/Linux 3.2.0, not stripped
```

Ghidraで解析する。以下、while中のif文に入らないような条件を探る。

```c
  while (local_a < 0x1a) {
    auStack168[(long)local_a + -1] = local_a + auStack168[(long)local_a + -1];
    if (auStack168[(long)local_a + -1] != local_48[(long)local_a + -1]) {
      local_2b0 = "flag_checker_1.f90";
      local_2a8 = 0x2b;
      local_2b8 = 0x80;
      local_2b4 = 6;
      _gfortran_st_write(&local_2b8);
      _gfortran_transfer_character_write(&local_2b8,"Sorry, flag does not match.",0x1b);
      _gfortran_st_write_done(&local_2b8);
      _gfortran_exit_i4(&DAT_00102054);
    }
    local_a = local_a + 1;
  }
  local_2b0 = "flag_checker_1.f90";
  local_2a8 = 0x30;
  local_2b8 = 0x80;
  local_2b4 = 6;
  _gfortran_st_write(&local_2b8);
  _gfortran_transfer_character_write(&local_2b8,"Congrats, that was the flag!",0x1c);
  _gfortran_st_write_done(&local_2b8);
  return;
```

まず、if文の中に入らないようにバイナリエディタを使ってJZをJMPに書き換える。

```
001013c2 74 76           JZ         LAB_0010143a

↓

001013c2 EB 76           JMP        LAB_0010143a
```

値を変えて、レジスタの中身を確認してみたところ、if文に差し掛かった時の`RCX+RAX-RDX`の値が`flag`になっていそうなので1文字ずつ表示する。

```gdb
b *(MAIN__)+0x13bf-0x11b9
disp $rcx+$rax-$rdx
```

```py
flag=[0x62,0x63,0x61,0x63,0x74,0x66,0x7b,0x66,0x30,0x72,0x74,0x72,0x34,0x4e,0x5f,0x69,0x35,0x5f,0x63,0x30,0x6f,0x4f,0x30,0x6c,0x7d]

for f in flag:
    print(chr(f),end='')
```

フラグが得られた。

<!-- bcactf{f0rtr4N_i5_c0oO0l} -->
