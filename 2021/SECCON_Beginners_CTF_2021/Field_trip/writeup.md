# Writeup

`Merkle–Hellman knapsack cryptosystem`を使ってフラグが暗号化されている。

* https://en.wikipedia.org/wiki/Merkle%E2%80%93Hellman_knapsack_cryptosystem

`pub_key`の部分和が`cipher`である。

```
例：
flag = [1,0,0,1,1]
pub_key = [2,3,6,10,17]

cipher = 1*2 + 0*3 + 0*6 + 1*10 + 1*17 = 29
```

`Merkle–Hellman knapsack cryptosystem`はLLLアルゴリズムを使って解く。

* https://project-euphoria.dev/blog/10-lll-for-crypto/

* https://yoshiking.hatenablog.jp/entry/2020/01/26/205826#Crypto-200pts-knapsack

```py
# sage
from Crypto.Util.number import long_to_bytes

pub_key = ...(省略)
cipher = ...(省略)

def create_matrix(c,pk):
    matrix_size = len(pk) + 1
    M = [
        [0 for _ in range(matrix_size)] for _ in range(matrix_size)
    ]

    for i in range(matrix_size - 1):
        M[i][0] = pk[i]
        M[i][i+1] = 2
        M[matrix_size - 1][i+1] = -1

    M[matrix_size - 1][0] = - c
    return M

def is_valid_vector(b):
    if b[0] != 0:
        return False
    for i, x in enumerate(b):
        if i != 0 and abs(x) != 1:
            return False
    return True

lllm = Matrix(ZZ, create_matrix(cipher,pub_key)).LLL()

flag_vecs = []
for basis in lllm:
    if is_valid_vector(basis):
        flag_vecs.append(basis)

for v in flag_vecs:
    flag = ""
    for _bit in reversed(v[1:]):
        c = ("1" if _bit == 1 else "0")
        flag = c + flag

    print(long_to_bytes(int(flag, 2)))
```

<!-- ctf4b{Y35!_I_ju5t_n33d3d_th353_num63r5!} -->
