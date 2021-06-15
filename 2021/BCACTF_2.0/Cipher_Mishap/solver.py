import string

UPPER = string.ascii_uppercase * 2

l = open('text.txt','r').read().replace('\n','').split(', ')

plain = ''
for s in l:
    ss = s.split('-')
    c = chr(int(ss[0],8))
    if(len(ss) == 2):
        c = UPPER[UPPER.find(c) + 23] # ROT23
        if(ss[1] == 'Y'):
            plain += c
        else:
            plain += c.lower()
    else:
        plain += c

print(plain)