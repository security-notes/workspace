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