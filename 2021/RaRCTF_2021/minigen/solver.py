import string

CHAR = string.printable

ct = [281, 547, 54, 380, 392, 98, 158, 440, 724, 218, 406, 672, 193, 457, 694, 208, 455, 745, 196, 450, 724]
flag = 'ra' # rarctf{

s, t, u = ct[0]^ord('r'), ct[1]^ord('a'), ct[2]^ord('r')
d = (t-s)%727
diff = ((u-t)%727 - d)

for idx in range(2,len(ct)):
    for c in CHAR:
        u = ct[idx]^ord(c)
        if d + diff == (u-t)%727:
            flag += c
            d = (u-t)%727
            s = t
            t = u
            break
print(flag)
