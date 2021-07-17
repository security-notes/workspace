from Crypto.Util.number import *

c = open('round-the-bases','r').read()
c = c.split('7D')

b = ''
for d in c:
    if 'IIcu' in d:
        b += '0'
    else:
        b += '1'

print(long_to_bytes(int(b,2)))
