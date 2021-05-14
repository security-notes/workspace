from pwn import *

A = 340282366920938460843936948965011886881
io = remote("umbccd.io","3100")

def send_chain(num:[int]):
    for n in num:
        io.recvuntil('>')
        io.sendline(str(n))
    io.sendline('done')

# chain 1
send_chain([A])

# chain 2
send_chain([A*2, A*3-1, A*4-2, A*5-3])

print(io.recvall().decode('utf-8'))
io.close()