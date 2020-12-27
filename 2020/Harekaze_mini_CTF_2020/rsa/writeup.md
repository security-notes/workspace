Unsolved :(

# Try

以下の2ファイルが与えられる。

```py
from Crypto.Util.number import getStrongPrime, getRandomRange

with open("flag", "rb") as f:
  flag = int.from_bytes(f.read(), "big")

p = getStrongPrime(512)
q = getStrongPrime(512)
n = p * q
phi = (p-1)*(q-1)
e = 65537
c1 = pow(flag, e, n)
c2 = pow(p + q, e, n)
c3 = pow(p - q, e, n)

print(f"{n=}")
print(f"{e=}")
print(f"{c1=}")
print(f"{c2=}")
print(f"{c3=}")
```

```txt
n=133957491909745071464818932891535809774039075882486614948793786706389844163167535932401761676665761652470189326864929940531781069869721371517782821535706577114286987515166157005227505921885357696815641758531922874502352782124743577760141307924730988128098174961618373787528649748605481871055458498670887761203
e=65537
c1=35405298533157007859395141814145254094484385088710533905385734792407576252003080929963085838327711405177354982539867453717921912839308282313390558033140654288445877937672625603540090399691469218188262950682485682814224928528948502206046863184746747265896306678488587444125143233443450049838709221084210200357
c2=23394879596667385465597018769822552384439114548016006879565586102300995936951562766011707923675690015217418498865916391314367448706185724546566348496812451258316472754407976794025546555423254676274654957362894171995220230464953432393865332807738040967281350952790472772600745096787761443699676372681208295288
c3=54869102748428770635192859184579301467475982074831093316564134451063250935340131274147041633101346896954483059058671502582914428555153910133076778016989842641074276293354765141522703887273042367333036465503084165682591308676428523152462442280924054400997210800504726635778588407034149919869556306659386868798
```

タイトルにもある通りRSA暗号の問題で、![p+q](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+p%2Bq%0A)と![p-q](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+p-q%0A)も同じように暗号化されている。

![n = pq](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+n+%3D+pq)であることから![c_2](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+c_2)は以下のように変形できる。

![\begin{eqnarray*}
 c_2 =& (p+q)^e \mod n \nonumber \\
=& \sum_{i=0}^{e} _{e}C_{i} p^e q^{e-i} \mod n \nonumber\\
=& \sum_{i=0}^{e} _{e}C_{i} p^e q^{e-i} \mod pq \nonumber\\
=& p^e + q^e \mod pq \nonumber\\
\end{eqnarray*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Beqnarray%2A%7D%0A+c_2+%3D%26+%28p%2Bq%29%5Ee+%5Cmod+n+%5Cnonumber+%5C%5C%0A%3D%26+%5Csum_%7Bi%3D0%7D%5E%7Be%7D+_%7Be%7DC_%7Bi%7D+p%5Ee+q%5E%7Be-i%7D+%5Cmod+n+%5Cnonumber%5C%5C%0A%3D%26+%5Csum_%7Bi%3D0%7D%5E%7Be%7D+_%7Be%7DC_%7Bi%7D+p%5Ee+q%5E%7Be-i%7D+%5Cmod+pq+%5Cnonumber%5C%5C%0A%3D%26+p%5Ee+%2B+q%5Ee+%5Cmod+pq+%5Cnonumber%5C%5C%0A%5Cend%7Beqnarray%2A%7D)

同様にして

![\begin{eqnarray*}
 c_3 =& p^e - q^e \mod pq \nonumber
\end{eqnarray*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Beqnarray%2A%7D%0A+c_3+%3D%26+p%5Ee+-+q%5Ee+%5Cmod+pq+%5Cnonumber%0A%5Cend%7Beqnarray%2A%7D)

である。

ここで、![c_2+c_3](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+c_2%2Bc_3)を計算すると

![\begin{eqnarray*}
 c_2 + c_3 =& 2p^e \mod pq\nonumber \\
\end{eqnarray*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Beqnarray%2A%7D%0A+c_2+%2B+c_3+%3D%26+2p%5Ee+%5Cmod+pq%5Cnonumber+%5C%5C%0A%5Cend%7Beqnarray%2A%7D)

となる。また、![k \in \mathbb{Z}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+k+%5Cin+%5Cmathbb%7BZ%7D)に対して

![\begin{eqnarray*}
 c_2 + c_3 =& 2p^e + kpq\nonumber \\
\end{eqnarray*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Beqnarray%2A%7D%0A+c_2+%2B+c_3+%3D%26+2p%5Ee+%2B+kpq%5Cnonumber+%5C%5C%0A%5Cend%7Beqnarray%2A%7D)

であるので、

![\begin{eqnarray*}
 c_2 + c_3 =& 0\mod p\nonumber \\
\end{eqnarray*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Beqnarray%2A%7D%0A+c_2+%2B+c_3+%3D%26+0%5Cmod+p%5Cnonumber+%5C%5C%0A%5Cend%7Beqnarray%2A%7D)

と変形できる。

つまり、![c_2+c_3](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+c_2%2Bc_3)は![p](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+p)の倍数であることがわかる。

![c_2+c_3](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+c_2%2Bc_3)を素因数分解してみたものの上手く解は得られなかった...

# Solution

**[Writeup]**

* https://github.com/TeamHarekaze/harekaze-mini-ctf-2020-challenges-public/blob/main/crypto/rsa/solution/solve.py

![c_2+c_3](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+c_2%2Bc_3)も![n](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+n)も![p](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+p)の倍数である＝![p](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+p)を約数に持つことがわかっているので、最大公約数を求めればよい。

```py
import math
import os

exec(open(f'{os.path.dirname(__file__)}/distfiles/output.txt').read())
pe = c2+c3

p = math.gcd(pe,n)
q = n // p
d = pow(e,-1,(p-1)*(q-1))
flag = pow(c1,d,n)

print(bytes.fromhex(hex(flag)[2:]))
```

<!-- HarekazeCTF{RSA_m34n5_Rin_Shiretoko_Ango} -->

# Comment

答えの一歩手前まではたどり着いたが、頭が固かった。

