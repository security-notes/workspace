from Crypto.Util.number import *

text = open('zwsp.txt','rb').read()

binary = ''
for i,t in enumerate(text):
    if(t == 0xe2):
        if(text[i:i+3] == b'\xe2\x80\x8b'):
            binary += '0'
        else:
            binary += '1'

print(long_to_bytes(int(binary,2)))