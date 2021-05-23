import base64
import os

text = open(os.path.dirname(__file__)+"/cipher.txt").read()
cnt = 1

while True:
    text = base64.b64decode(text)
    if b'dctf{' in text:
        print(cnt, text)
        break
    cnt += 1
