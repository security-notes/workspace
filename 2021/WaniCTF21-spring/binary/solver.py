import os

f = open(os.path.dirname(__file__)+'/mis-binary/binary.csv').read()
f = f.replace("\n","")
print(bytes.fromhex(hex(int(f,2))[2:]))
