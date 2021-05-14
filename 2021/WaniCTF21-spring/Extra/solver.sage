import os

exec(open('./'+os.path.dirname(__file__)+"/cry-extra/output.txt").read())

# N = p*q
# M = 2*p + q
# => 2*p**2 - M*p + N = 0

var('p')
assume(p,'integer')
sln = solve(2*p**2 - M*p + N == 0 ,p)

p = int(sln) 
q = N // p
d = power_mod(e,-1,(p-1)*(q-1))
print(bytes.fromhex(hex(power_mod(c,d,N))[2:]))
