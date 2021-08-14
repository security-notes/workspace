from Crypto.Util.number import *
import string

CHARS = string.printable

locals = [0x45481d1217111313, 0x95f422c260b4145, 0x541b56563d6c5f0b, 0x585c0b3c2945415f, 0x402a6c54095d5f00, 0x4b5f4248276a0606, 0x6c5e5d432c2d4256, 0x6b315e434707412d, 0x5e54491c6e3b0a5a, 0x2828475e05342b1a, 0x60450073b26111f, 0xa774803050b0d04]
locals = [ long_to_bytes(l)[::-1] for l in locals]

flag = 'r'
idx = 0

for local in locals:
    for l in local:
        for c in CHARS:
            if ord(flag[idx]) ^ ord(c) == l:
                flag += c
                idx += 1
                if c == '}':
                    print(flag)
                    exit(0)
                break
