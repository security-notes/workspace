import os
os.environ['PWNLIB_NOTERM'] = 'True' # sage & pwntools

from pwn import *
import re
import itertools

class Generator():
    DIGITS = 8
    def __init__(self, seed):
        self.seed = seed
        assert(len(str(self.seed)) == self.DIGITS)

    def getNum(self):
        self.seed = int(str(self.seed**2).rjust(self.DIGITS*2, "0")[self.DIGITS//2:self.DIGITS + self.DIGITS//2])
        return self.seed

io = remote('crypto.2021.chall.actf.co','21600')

io.sendline('r')
r1 = int(re.search(r'\d+', io.recvline().decode('utf-8')).group())
print(r1)
io.sendline('r')
r2 = int(re.search(r'\d+', io.recvline().decode('utf-8')).group())
print(r2)
F = factor(r1)
f = [f[0] for f in F for _ in range(f[1])]
if len(f) >= 6:
    io.close()
    exit()
perm = [p for p in itertools.permutations(f)]
found = False
for p in perm :
    a = 1
    for n in p:
        if a * n < 99999999:
            a *= n
        else:
            break
    b = r1 // a
    if 10000000 <= a <= 99999999 and  10000000 <= b <= 99999999:
        g1 = Generator(a)
        g2 = Generator(b)
    else:
        continue
    if(g1.getNum()*g2.getNum() == r2):
        found = True
        break
if found:
    io.sendline('g')
    io.sendline(str(g1.getNum()*g2.getNum()))
    io.sendline(str(g1.getNum()*g2.getNum()))
    io.interactive()