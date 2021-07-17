n = 228430203128652625114739053365339856393
e = 65537
c = 126721104148692049427127809839057445790

from factordb.factordb import FactorDB
from Crypto.Util.number import *

f = FactorDB(n)
f.connect()
factors = f.get_factor_list()

[p, q] = factors
d = pow(e,-1,(p-1)*(q-1))
m = pow(c,d,n)

print(long_to_bytes(m))
