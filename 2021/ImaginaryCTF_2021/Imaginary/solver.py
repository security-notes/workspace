from pwn import *
import re
from tqdm import tqdm

io = remote('chal.imaginaryctf.org', '42015')

io.recvuntil('so watch out!)\n\n')

for _ in tqdm(range(300)):
    out = io.recvline().decode('utf-8')
    nums = list(re.findall(r'\(([0-9i+-]+)\)', out))
    opts = list(re.findall(r'\) ([+-]) \(', out))
    opts = ['+'] + opts # first number is positive
    real, image = 0, 0
    for idx, num in enumerate(nums):
        num = list(map(int, list(re.findall(r'\d+', num))))
        if opts[idx] == '+':
            real += num[0]
            image += num[1]
        else:
            real -= num[0]
            image -= num[1]
    if image >= 0:
        io.sendline(f'{real}+{image}i')
    else:
        io.sendline(f'{real}{image}i')
    if b'Correct!' not in io.recvline():
        break

io.interactive()
io.close()
