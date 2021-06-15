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