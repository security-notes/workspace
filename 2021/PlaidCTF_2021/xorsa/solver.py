import os
from Crypto.PublicKey import RSA
from Crypto.Util.number import *
from Crypto.Cipher import PKCS1_OAEP

pubKey = RSA.import_key(open(os.path.dirname(__file__) + "/dist/public.pem").read())
e = pubKey.e
n = pubKey.n
x = 16158503035655503426113161923582139215996816729841729510388257123879913978158886398099119284865182008994209960822918533986492024494600106348146394391522057566608094710459034761239411826561975763233251722937911293380163746384471886598967490683174505277425790076708816190844068727460135370229854070720638780344789626637927699732624476246512446229279134683464388038627051524453190148083707025054101132463059634405171130015990728153311556498299145863647112326468089494225289395728401221863674961839497514512905495012562702779156196970731085339939466059770413224786385677222902726546438487688076765303358036256878804074494

primes = [[0,0]]
bit = 1
while bit <= 2**4096:
    next_primes = []
    for ps in primes:
        [p, q] = ps
        if p > q and [q, p] in primes:
            continue
        bit_mask = (bit << 1) - 1
        if (x & bit) == 0: # XOR : 0
            if ((p * q) & bit_mask) == (n & bit_mask) and p * q <= n: # 0,0
                next_primes.append([p, q])
            if ((p | bit) * (q | bit) & bit_mask) == (n & bit_mask) and (p | bit) * (q | bit) <= n: # 1,1
                next_primes.append([(p | bit), (q | bit)])
        else: # XOR : 1
            if (p * (q | bit) & bit_mask) == (n & bit_mask) and p * (q | bit) <= n: # 0,1
                next_primes.append([p, (q | bit)])
            if ((p | bit) * q & bit_mask) == (n & bit_mask) and (p | bit) * q <= n: # 1,0
                next_primes.append([(p | bit), q])   
    primes = next_primes
    bit <<= 1

for prime in primes:
    [p, q] = prime
    d = pow(e, -1, (p-1)*(q-1))
    key = RSA.construct((n,e,d,p,q))
    cipher = PKCS1_OAEP.new(key)
    print(cipher.decrypt(open(os.path.dirname(__file__) + "/dist/flag.enc", "rb").read()))
