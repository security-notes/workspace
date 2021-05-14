from pwn import *

io = remote('oucs.cry.wanictf.org','50010')

plaintext = ""
ciphertext = ""
n = 0

# Get n
io.recvuntil('> ')
io.sendline('4')
exec(io.recvline().decode('utf-8')) # n

# Get c1
io.recvuntil('> ')
io.sendline('1')
exec(io.recvline().decode('utf-8'))
flag_encrypt = ciphertext

# Get c2
io.recvuntil('> ')
io.sendline('2')
io.recvuntil('> ')
io.sendline('0x01')
exec(io.recvline().decode('utf-8'))
one_encrypt = ciphertext

# decrypt c1*c2 mod n
io.recvuntil('> ')
io.sendline('3')
io.recvuntil('> ')
io.sendline(str(hex((flag_encrypt * one_encrypt)%n)))
exec(io.recvline().decode('utf-8'))

plaintext = hex(plaintext - 1)
print(bytes.fromhex(plaintext[2:]))
