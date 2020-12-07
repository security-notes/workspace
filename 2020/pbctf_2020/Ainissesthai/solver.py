from string import ascii_uppercase as UC

cipherlist = []
with open('./output.txt') as f:
    while True:
        cipher = f.readline()
        if len(cipher) < 1:
            break
        cipherlist.append(cipher[0:-1]) # exclude \n

for i in range(17):
    string = [char[i] for char in cipherlist]
    diff = set(UC)-set(string)
    print(list(diff)[0],end='')