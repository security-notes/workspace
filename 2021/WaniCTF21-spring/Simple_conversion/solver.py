import os

c = open(os.path.dirname(__file__)+"/cry-simple-conversion/output.txt").read()
m = bytes.fromhex(hex(int(c))[2:])
print(m)
