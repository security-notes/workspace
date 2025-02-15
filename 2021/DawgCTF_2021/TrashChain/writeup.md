# Writeup

以下のプログラムが与えられる。

```py
#!/usr/bin/env python3

# Hash constants
A = 340282366920938460843936948965011886881
B = 127605873542257115442148455720344860097

# Hash function
def H(val, prev_hash, hash_num):
    return (prev_hash * pow(val + hash_num, B, A) % A)


if __name__ == "__main__":

    # Print welcome message
    print("Welcome to TrashChain!")
    print("In this challenge, you will enter two sequences of integers which are used to compute two hashes. If the two hashes match, you get the flag!")
    print("Restrictions:")
    print("  - Integers must be greater than 1.")
    print("  - Chain 2 must be at least 3 integers longer than chain 1")
    print("  - All integers in chain 1 must be less than the smallest element in chain 2")
    print("Type \"done\" when you are finished inputting numbers for each chain.")

    # Get inputs
    chains = [[], []]
    for chain_num in range(len(chains)):
        print("\nProvide inputs for chain {}.".format(chain_num+1))
        while True:
            val = input("> ")
            if val == "done":
                break
            try:
                val = int(val)
            except ValueError:
                print("Invalid input, exiting...")
                exit(0)
            if val <= 1:
                print("Inputs must be greater than 1, exiting...")
                exit(0)
            chains[chain_num].append(val)

    # Validate chain lengths
    if not len(chains[0]):
        print("Chain 1 cannot be empty, exiting...")
        exit(0)
    if len(chains[1]) - len(chains[0]) < 3:
        print("Chain 2 must contain at least 3 more integers than chain 1, exiting...")
        exit(0)
    if max(chains[0]) >= min(chains[1]):
        print("No integer in chain 1 can be greater than the smallest integer in chain 2, exiting...")
        exit(0)

    # Compute hashes
    hashes = []
    for chain_num in range(len(chains)):
        cur_hash = 1
        for i, val in enumerate(chains[chain_num]):
            cur_hash = H(val, cur_hash, i+1)
        hashes.append(cur_hash)

    # Print hashes
    print("Hash for chain 1: {0:0{1}x}".format(hashes[0], 32))
    print("Hash for chain 2: {0:0{1}x}".format(hashes[1], 32))
    if hashes[0] == hashes[1]:
        print("Correct! Here's your flag: DogeCTF{not_a_real_flag}")
```

`chains[0]`と`chains[1]`を与えるとハッシュを計算し、2つのハッシュが一致すればフラグが得られる。

`chains[0]`と`chains[1]`には次のような条件がある。

1. `chains[0]`の要素は1以上

2. `chains[1]`の要素数は`chains[0]`よりも3以上多い

3. `chains[1]`の最小値は`chains[0]`の最大値よりも大きい

4. `chains`の中身は1より大きい

これらの条件を満たす例として、`chains[0] = [2], chains[1] = [3,4,5,6]`がある。

ハッシュの計算は以下の部分で行っている。

```py
# Hash constants
A = 340282366920938460843936948965011886881
B = 127605873542257115442148455720344860097

# Hash function
def H(val, prev_hash, hash_num):
    return (prev_hash * pow(val + hash_num, B, A) % A)
```

ここで、`val`は`chains`の要素、`prev_hash`は1個前のハッシュ値(初期値1)、`hash_num`は`chains`の0から始まるindexである。

`chains[0] = [2]`のとき、

`H = 1 * pow(2 + 0, B, A) % A`

というハッシュ値が得られ、

`chains[1] = [3,4,5,6]`のとき、

`H1 = 1 * pow(3 + 0, B, A) % A`

`H2 = H1 * pow(4 + 1, B, A) % A`

...

`H = H3 * pow(6 + 1, B, A) % A`

というハッシュ値が得られる。

ここで、`val + hash_num`が`A`の倍数であるとき、計算結果が必ず1になるので常にハッシュ値を1に固定することができる。

よって、`chains[0] = [A], chains[1] = [A*2, A*3-1, A*4-2, A*5-3]`を与えることによりハッシュ値を1で一致させることができる。

```py
from pwn import *

A = 340282366920938460843936948965011886881
io = remote("umbccd.io","3100")

def send_chain(num:[int]):
    for n in num:
        io.recvuntil('>')
        io.sendline(str(n))
    io.sendline('done')

# chain 1
send_chain([A])

# chain 2
send_chain([A*2, A*3-1, A*4-2, A*5-3])

print(io.recvall().decode('utf-8'))
io.close()
```

<!-- DawgCTF{We1rd_RSA_2nd_Pre1m4g3_th1ng} -->
