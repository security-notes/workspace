cipher = open("ciphertext.md","rb").read()

byte = []
for i,c in enumerate(cipher):
    if(c == 0xf4):
        if(cipher[i:i+4] not in byte):
            byte.append(cipher[i:i+4])

byte = sorted(byte)

# byte = [b'\xf4\x80\xb4\xa0', b'\xf4\x81\xab\x9e', b'\xf4\x83\x84\x8f', b'\xf4\x83\x97\x81', b'\xf4\x84\xa7\xbb', b'\xf4\x84\xba\xb7', b'\xf4\x86\x86\x97', b'\xf4\x86\x96\x93', b'\xf4\x86\x9e\x8e', b'\xf4\x87\xba\x9f', b'\xf4\x87\xbd\x9b', b'\xf4\x89\x82\xab', b'\xf4\x89\x97\xbd', b'\xf4\x89\xaf\x93', b'\xf4\x8a\xb6\xac', b'\xf4\x8a\xb8\x89', b'\xf4\x8b\x84\x9a', b'\xf4\x8b\x90\x9d', b'\xf4\x8c\x98\x97', b'\xf4\x8c\xb2\x94', b'\xf4\x8c\xb6\xb4', b'\xf4\x8f\x95\x88', b'\xf4\x8f\x9f\x9f']
char = [ "(" + str(i) + ")" for i in range(len(byte))]

# guess from result
char[11] = "h"
char[10] = "t"
char[2] = "p"
char[1] = "s"
char[8] = "b"
char[5] = "c"
char[4] = "a"
char[20] = "f"
char[15] = "e"
char[19] = "u"
char[3] = "r"
char[7] = "o"
char[9] = "n"
char[12] = "d" 
char[17] = "l"
char[6] = "i"
char[21] = "w"
char[22] = "k"
char[16] = "g"
char[14] = "v"
char[13] = "y"
char[0] = "j"
char[18] = "m"

translate = dict(zip(byte,char))

plain = ""
cnt = 0
while(cnt < len(cipher)):
    c = cipher[cnt]
    if(c == 0xf4):
        plain += translate[cipher[cnt:cnt+4]]
        cnt += 4
    else:
        plain += chr(cipher[cnt])
        cnt += 1

print(plain)