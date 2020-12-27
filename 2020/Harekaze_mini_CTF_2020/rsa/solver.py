import math
import os

exec(open(f'{os.path.dirname(__file__)}/distfiles/output.txt').read())
pe = c2+c3

p = math.gcd(pe,n)
q = n // p
d = pow(e,-1,(p-1)*(q-1))
flag = pow(c1,d,n)

print(bytes.fromhex(hex(flag)[2:]))
