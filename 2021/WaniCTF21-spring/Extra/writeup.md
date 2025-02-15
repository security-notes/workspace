# Writeup

RSA暗号の`c,e,N`と`M = 2*p + q`が与えられる。

```
N = p*q
M = 2*p + q
```

より、

```
2*p**2 - M*p + N = 0
```

を`p`について解けばよい。`p`が分かれば復号化するのみ。

```py
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
```

<!-- FLAG{@n_ex7ra_param3ter_ru1n5_3very7h1n9} -->
