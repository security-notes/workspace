# ファイル読み込み
with open('./output.txt') as f:
    ciphertext = f.read()

# s1,s2に対してXOR演算を行う
def decrypt(s1, s2):
    assert len(s1) == len(s2)

    result = ""
    for c1, c2 in zip(s1, s2):
        result += chr(ord(c1) ^ ord(c2))
    return result

# 先頭3文字のXORをとってKeyを計算
key = decrypt(ciphertext[0:3],'FLA')

# Keyの繰り返しと暗号文のXORを計算
plaintext = decrypt(key*19,ciphertext)

print(plaintext)