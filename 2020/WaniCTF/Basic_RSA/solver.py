from pwn import *
from Crypto.Util.number import inverse

conn = remote('rsa.wanictf.org',50000)

# 第1段階
conn.recvuntil('p = ')
p = int(conn.recvline())
conn.recvuntil('q = ')
q = int(conn.recvline())
n = p * q
conn.sendline(str(n))

# 第2段階
conn.recvuntil('m = ')
m = int(conn.recvline())
conn.recvuntil('e = ')
e = int(conn.recvline())
conn.recvuntil('n = ')
n = int(conn.recvline())
c = pow(m,e,n)
conn.sendline(str(c))

# 第3段階
conn.recvuntil('p = ')
p = int(conn.recvline())
conn.recvuntil('q = ')
q = int(conn.recvline())
conn.recvuntil('e = ')
e = int(conn.recvline())
conn.recvuntil('c = ')
c = int(conn.recvline())
d = inverse(e,(p-1)*(q-1))
m = pow(c,d,p*q)
conn.sendline(str(m))

# フラグ出力
print(conn.recvline())
conn.close()
