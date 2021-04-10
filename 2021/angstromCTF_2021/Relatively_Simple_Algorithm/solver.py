import os

exec(open(os.path.dirname(__file__) + "/rsa.txt").read())

d = pow(e,-1,(p-1)*(q-1))
m = pow(c,d,n)
print(bytes.fromhex(hex(m)[2:]).decode('utf-8'))
