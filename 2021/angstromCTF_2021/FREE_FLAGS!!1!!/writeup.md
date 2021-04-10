# Writeup

```c
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  puts(
      "Congratulations! You are the 1000th CTFer!!! Fill out this short survey to get FREE FLAGS!!!"
      );
  puts("What number am I thinking of???");
  __isoc99_scanf("%d",&local_11c);
  if (local_11c == 0x7a69) {
    puts("What two numbers am I thinking of???");
    __isoc99_scanf("%d %d",&local_120,&local_124);
    if ((local_120 + local_124 == 0x476) && (local_120 * local_124 == 0x49f59)) {
      puts("What animal am I thinking of???");
      __isoc99_scanf(" %256s",local_118);
      sVar2 = strcspn(local_118,"\n");
      local_118[sVar2] = '\0';
      iVar1 = strcmp(local_118,"banana");
      if (iVar1 == 0) {
        puts("Wow!!! Now I can sell your information to the Russian government!!!");
        puts("Oh yeah, here\'s the FREE FLAG:");
        print_flag();
        local_128 = 0;
      }
      else {
        puts("Wrong >:((((");
        local_128 = 1;
      }
    }
    else {
      puts("Wrong >:((((");
      local_128 = 1;
    }
  }
  else {
    puts("Wrong >:((((");
    local_128 = 1;
  }
  if (*(long *)(in_FS_OFFSET + 0x28) == local_10) {
    return local_128;
  }
```

1. `local_11c == 0x7a69` 

2. `local_120 + local_124 == 0x476 && local_120 * local_124 == 0x49f59`

3. `strcmp(local_118,"banana")`

を満たす値を入力していけばよい。

```py
from pwn import *

def solve(b,c):
    a = 1
    b = -b
    x1 = (-b + math.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b**2-4*a*c))/(2*a)
    return [str(int(x1)), str(int(x2))]

io = remote('shell.actf.co', 21703)
# 1
io.recvuntil('What number am I thinking of???')
io.sendline(str(int(0x7a69)))
# 2
io.recvline()
io.sendline(' '.join(solve(0x476,0x49f59)))
# 3
io.recvline()
io.sendline('banana')

io.interactive()
```

<!-- actf{what_do_you_mean_bananas_arent_animals} -->
