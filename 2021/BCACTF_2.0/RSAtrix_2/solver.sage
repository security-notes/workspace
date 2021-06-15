from Crypto.Util.number import *

p = 94653748632775872562206813156858988240379536044871601072940225022186828970998253
q = 47982815420210848939631963090916124891858755590019708758250635504732488148835047
n = p * q
e = 3
N = 23

R = Zmod(n)
MS = MatrixSpace(R, N, N)
s = PermutationGroupElement('(1,6,8)(2,3,4,5,7)(9,11,13,15,17,19,21,23)(10,12,14,16,18,20,22)')
P = MS(s.matrix())
with seed(1): C = MS([randrange(100) for i in range(N*N)])
G = C * P * C^-1

M = MS(eval(open('enc.txt','r').read())) * (G^-e)

d = power_mod(e,-1,(p-1)*(q-1))
print(long_to_bytes(power_mod(M[0][0],d,n)))