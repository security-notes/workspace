

# This file was *autogenerated* from the file solver.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_0 = Integer(0); _sage_const_1 = Integer(1)
import os

exec(open('./'+os.path.dirname(__file__)+"/cry-extra/output.txt").read())

# N = p*q
# M = 2*p + q
# => 2*p**2 - M*p + N = 0

var('p')
assume(p,'integer')
sln = solve(_sage_const_2 *p**_sage_const_2  - M*p + N == _sage_const_0  ,p)

p = int(sln) 
q = N // p
d = power_mod(e,-_sage_const_1 ,(p-_sage_const_1 )*(q-_sage_const_1 ))
print(bytes.fromhex(hex(power_mod(c,d,N))[_sage_const_2 :]))

