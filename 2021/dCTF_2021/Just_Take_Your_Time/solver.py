from pwn import *
from time import time
from Crypto.Cipher import DES3

from pwnlib.util.fiddling import xor

io = remote('dctf-chall-just-take-your-time.westeurope.azurecontainer.io', '9999')

io.recvuntil('You have one second.\n')

calc = None
exec('calc = ' + io.recvline().decode('utf-8').split('=')[0])
io.sendline(str(calc))

io.recvuntil('flag shall be yours!\n')
encrypted = bytes.fromhex(io.recvline_regex(r'[0-9a-f]*').decode('utf-8'))

now = int(time())
for i in range(60):
    key = str(now-i).zfill(16).encode("utf-8")
    cipher = DES3.new(key, DES3.MODE_CFB, b"00000000")
    decrypted = cipher.decrypt(encrypted)
    if '\\x' not in str(decrypted):
        io.sendline(decrypted)
        print(decrypted, -i)
        break

print(io.recvall())
io.close()
