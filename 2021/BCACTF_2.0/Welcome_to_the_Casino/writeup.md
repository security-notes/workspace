# Writeup

netcatすると、ルーレットが始まる。文字がそろえばよさそう。

```bash
$ nc misc.bcactf.com 49156


 /$$                           /$$
| $$                          | $$
| $$       /$$   /$$  /$$$$$$$| $$   /$$ /$$   /$$
| $$      | $$  | $$ /$$_____/| $$  /$$/| $$  | $$
| $$      | $$  | $$| $$      | $$$$$$/ | $$  | $$
| $$      | $$  | $$| $$      | $$_  $$ | $$  | $$
| $$$$$$$$|  $$$$$$/|  $$$$$$$| $$ \  $$|  $$$$$$$
|________/ \______/  \_______/|__/  \__/ \____  $$
                                         /$$  | $$
                                        |  $$$$$$/
                                         \______/
 /$$                   /$$     /$$
| $$                  | $$    | $$
| $$        /$$$$$$  /$$$$$$ /$$$$$$    /$$$$$$
| $$       /$$__  $$|_  $$_/|_  $$_/   /$$__  $$
| $$      | $$  \ $$  | $$    | $$    | $$  \ $$
| $$      | $$  | $$  | $$ /$$| $$ /$$| $$  | $$
| $$$$$$$$|  $$$$$$/  |  $$$$/|  $$$$/|  $$$$$$/
|________/ \______/    \___/   \___/   \______/



Welcome to the Lucky Lotto Slot Machine!
Let's see if you're today's big winner!
Enter the letter "o" to pull the lever...
o

Spinning...
           [[[ q ]]]
           [[[ e ]]]
           [[[ l ]]]

You didn't win anything. Try matching more letters next time!

Come back next time!
```

何回も`nc`する必要がありそうなのでスクリプトを書く。メッセージ受信やルーレットの回転に時間がかかるので並行して接続する。

```py
from pwn import *

PARALLEL = 20

io = [ _ for _ in range(PARALLEL)]
while(True):
    for i in range(PARALLEL):
        io[i] = remote('misc.bcactf.com', '49156')

    for i in range(PARALLEL):
        io[i].recvuntil('Enter the letter "')
        char = io[i].recvn(1).decode('utf-8')
        io[i].recvline()
        io[i].sendline(char)

    for i in range(PARALLEL):
        out = io[i].recvall().decode('utf-8')
        print(out)
        if 'bcactf' in out:
            exit()
```

```
Spinning...
           [[[ f ]]]
           [[[ f ]]]
           [[[ f ]]]
Congratulations! You won the grand prize!
It's a flag!

   .^.
  (( ))
   |#|_______________________________
   |#||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
   |#||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
   |#||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
   |#||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
   |#||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
   |#||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
   |#||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
   |#||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
   |#||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
   |#||$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
   |#|'""""""""""""""""""""""""""""""'
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|

bcactf{y0u_g0t_1ucKy_af23dd97g64n}

Come back next time!
```

<!-- bcactf{y0u_g0t_1ucKy_af23dd97g64n} -->
