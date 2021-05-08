import os
from pwn import xor

png_fixed9bytes = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A\x00'
e = open(os.path.dirname(__file__)+"/flag.png.enc","rb").read()
key = xor(e[0:9],png_fixed9bytes)
f = open(os.path.dirname(__file__)+"/flag.png","wb")
f.write(xor(e,key))