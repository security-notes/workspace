# Writeup

ELF実行ファイルが与えられるのでGhidraを使ってリバースエンジニアリングする。

フラグの取得に関係ありそうな関数は次のようになっている。

```c
undefined8 main(void)
{
  int iVar1;
  uint uVar2;
  time_t tVar3;
  
  tVar3 = time((time_t *)0x0);
  srand((uint)tVar3);
  iVar1 = rand();
  uVar2 = iVar1 % 5 + 8;
  printf("%d\n",(ulong)uVar2);
  process(uVar2);
  return 0;
}

undefined8 process(int param_1)
{
  long lVar1;
  bool bVar2;
  long lVar3;
  long in_FS_OFFSET;
  int local_24;
  long local_20;
  
  lVar1 = *(long *)(in_FS_OFFSET + 0x28);
  bVar2 = true;
  local_24 = 1;
  while (local_24 <= param_1) {
    lVar3 = triangle(param_1,local_24,local_24);
    __isoc99_scanf();
    if (lVar3 != local_20) {
      bVar2 = false;
    }
    local_24 = local_24 + 1;
  }
  if (bVar2) {
    system("cat flag.txt");
  }
  else {
    puts("Better luck next time.");
  }
  if (lVar1 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}

long triangle(int param_1,int param_2)
{
  long lVar1;
  long lVar2;
  
  if (param_1 < param_2) {
    lVar1 = 0;
  }
  else {
    if ((param_1 == 1) && (param_2 == 1)) {
      lVar1 = 1;
    }
    else {
      if (param_2 == 1) {
        lVar1 = triangle(param_1 + -1,param_1 + -1,param_1 + -1);
      }
      else {
        lVar2 = triangle(param_1,param_2 + -1,param_2 + -1);
        lVar1 = triangle(param_1 + -1,param_2 + -1,param_2 + -1);
        lVar1 = lVar1 + lVar2;
      }
    }
  }
  return lVar1;
}
```

`triangle`が少し複雑なので、同じ処理を行うプログラムをPythonで書き直して計算させてみる。

```py
from pwn import *

def main(uVar2:int):
    process(uVar2)

def process(param_1:int):
    local_24 = 1
    while local_24 <= param_1:
        lVar3 = triangle(param_1, local_24)
        print(lVar3)
        io.sendline(str(lVar3))
        local_24 += 1

def triangle(param_1:int, param_2:int):
    if param_1 < param_2:
        ret = 0
    else:
        if param_1 == 1 and param_2 == 1:
            ret = 1
        else:
            if param_2 == 1:
                ret = triangle(param_1 -1, param_1 -1)
            else:
                ret2 = triangle(param_1, param_2 -1)
                ret1 = triangle(param_1 -1, param_2 -1)
                ret = ret1 + ret2
    return ret

if __name__ == "__main__":
    io = remote('dctf-chall-bell.westeurope.azurecontainer.io','5311')
    var = int(io.recvline())
    print(var)

    main(var)
    
    print(io.recvall())
    io.close()
```

```
[x] Opening connection to dctf-chall-bell.westeurope.azurecontainer.io on port 5311
[x] Opening connection to dctf-chall-bell.westeurope.azurecontainer.io on port 5311: Trying 51.105.148.136
[+] Opening connection to dctf-chall-bell.westeurope.azurecontainer.io on port 5311: Done
11
115975
137122
162409
192713
229114
272947
325869
389946
467767
562595
678570
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 35B
[+] Receiving all data: Done (35B)
[*] Closed connection to dctf-chall-bell.westeurope.azurecontainer.io port 5311
b'dctf{f1rst_step_t0wards_b3ll_l4bs}\n'
```

<!-- dctf{f1rst_step_t0wards_b3ll_l4bs} -->
