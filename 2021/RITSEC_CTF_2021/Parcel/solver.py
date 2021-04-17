import base64
import os
import re

with open(os.path.dirname(__file__)+'/Parcel_extract') as f:
    text = f.read()
    text = text.replace('\n','')
    b64s = re.findall(r'iVB.*?-',text)
    for index, b in enumerate(b64s):
        # print(index)
        img = base64.b64decode(b[0:-1])
        with open(f"{os.path.dirname(__file__)}/extract_img/image{index}.png", 'bw') as fi:
            fi.write(img)