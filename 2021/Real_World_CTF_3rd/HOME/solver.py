from pwn import *
io = remote('home.realworldctf.com',1337)
msg = io.recvall()
print(msg.decode('ascii'))
io.close()