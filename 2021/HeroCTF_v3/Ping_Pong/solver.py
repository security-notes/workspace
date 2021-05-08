import os

binary = ""
with open(os.path.dirname(__file__)+"/output.txt","r") as f:
    text = f.readline()
    while text:
        if "PING" in text:
            binary += "1"
        else :
            binary += "0"
        text = f.readline()
print(bytearray.fromhex(hex(int(binary,2))[2:]).decode())
