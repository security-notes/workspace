import itertools

def encrypt(plaintext: str, a: int, b: int) -> str:
    ciphertext = ""
    for x in plaintext:
        if "A" <= x <= "Z":
            x = ord(x) - ord("A")
            x = (a * x + b) % 26
            x = chr(x + ord("A"))
        ciphertext += x

    return ciphertext

if __name__ == "__main__":
    ciphertext = "HLIM{OCLSAQCZASPYFZASRILLCVMC}"

    for i,j in itertools.product(range(26),range(26)):
        c = encrypt("FLAG{", a=i, b=j)
        if c == "HLIM{":
            break

    for _ in range(26):
        ciphertext = encrypt(ciphertext,a=i, b=j)
        if "FLAG{" in ciphertext:
            print(ciphertext)
            break
