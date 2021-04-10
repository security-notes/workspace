from itertools import cycle
import string

c = 'ae27eb3a148c3cf031079921ea3315cd27eb7d02882bf724169921eb3a469920e07d0b883bf63c018869a5090e8868e331078a68ec2e468c2bf13b1d9a20ea0208882de12e398c2df60211852deb021f823dda35079b2dda25099f35ab7d218227e17d0a982bee7d098368f13503cd27f135039f68e62f1f9d3cea7c'
c = bytes.fromhex(c)
m = b'actf{'

def xor(text,key):
    return bytes([a ^ b for (a,b) in zip(text, cycle(key))])

def is_ascii(text):
    return all(char in bytes(string.printable,'ascii') for char in text)

while len(c) > len(m):
    key = xor(c,m)[:5]
    plaintext = xor(c,key)
    if is_ascii(plaintext) and b'}' in plaintext:
        print(plaintext)
    c = c[1:]