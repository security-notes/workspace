from Crypto.Cipher import AES

for k in range(31):
    k = str(k)

    # pad key to 16 bytes (128bit)
    key = ""
    i = 0
    padding = "uiuctf2021uiuctf2021"
    while (16 - len(key) != len(k)):
        key = key + padding[i]
        i += 1
    key = key + k
    key = bytes(key, encoding='ascii')

    with open('output.txt', 'rb') as f:
        out = bytes.fromhex(f.read().decode())

    iv = bytes("kono DIO daaaaaa", encoding = 'ascii')
    cipher = AES.new(key, AES.MODE_CFB, iv)
    ciphertext = cipher.decrypt(out)

    if b'uiuctf' in ciphertext:
        print(f'{key = }')
        print(f'{ciphertext = }')
