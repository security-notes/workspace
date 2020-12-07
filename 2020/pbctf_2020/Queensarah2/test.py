#!/usr/bin/env python3

from string import ascii_lowercase
from itertools import product
from random import SystemRandom
from math import ceil, log

random = SystemRandom()
ALPHABET = ascii_lowercase + "_"

bigrams = [''.join(bigram) for bigram in product(ALPHABET, repeat=2)]
random.shuffle(bigrams)

S_box = {}
for i in range(len(ALPHABET)):
    for j in range(len(ALPHABET)):
        S_box[ALPHABET[i]+ALPHABET[j]] = bigrams[i*len(ALPHABET) + j]

assert len(set(S_box.keys())) == 27*27

print(S_box)

def encrypt(message):
    if len(message) % 2:
        message += "_"

    message = list(message)
    rounds = int(2 * ceil(log(len(message), 2))) # The most secure amount of rounds

    print(rounds)

    for round in range(rounds):
        # Encrypt
        for i in range(0, len(message), 2):
            message[i:i+2] = S_box[''.join(message[i:i+2])]

        # print('en_msg = ',''.join(message))

        # Shuffle, but not in the final round
        if round < (rounds-1):
            message = [message[i] for i in range(len(message)) if i%2 == 0] + [message[i] for i in range(len(message)) if i%2 == 1]

        # print('sh_msg = ',''.join(message))
        
    return ''.join(message)


if __name__ == "__main__":
    print("This is a restricted service! Decrypt this password to proceed:")
    print(encrypt('a'*10000))
    print(encrypt('a'*9999+'b'))

    for _ in range(1500):
        question = input("> ").strip()
        assert 0 < len(question) <= 10000

        if not question:
            print("Bye.")
            break

        else:
            print("That's not quite right. Your password encrypts to this:")
            print(encrypt(question))

