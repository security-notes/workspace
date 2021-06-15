from pwn import *
context.log_level = 'error'

target_query = "Open sesame... Flag please!"

# 1
io = remote('crypto.bcactf.com', '49153')
io.recvuntil('Would you like to encrypt (E), decrypt (D), or quit (Q)?')
io.sendline('E')
io.recvuntil('>>> ')
c = '\x00' * len(target_query)
io.sendline(c)
io.recvuntil("Here's your message:\n")
msg = io.recvline().strip().decode('utf-8')

# 2
io = remote('crypto.bcactf.com', '49153')
io.recvuntil('Would you like to encrypt (E), decrypt (D), or quit (Q)?')
io.sendline('D')
io.recvuntil('>>> ')
c = xor(bytes.fromhex(msg), target_query.encode('utf-8')).hex()
io.sendline(c)

io.interactive()

io.close()
