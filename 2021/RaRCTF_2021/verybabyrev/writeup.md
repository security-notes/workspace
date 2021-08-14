# Writeup

実行ファイルが与えられる。

```bash
$ ./verybabyrev
Enter your flag: hoge
Nope!
```

正しいフラグが入力できればよさそうなので、Ghidraで解析する。

```c
  local_108 = 0x45481d1217111313;
  local_100 = 0x95f422c260b4145;
  local_f8 = 0x541b56563d6c5f0b;
  local_f0 = 0x585c0b3c2945415f;
  local_e8 = 0x402a6c54095d5f00;
  local_e0 = 0x4b5f4248276a0606;
  local_d8 = 0x6c5e5d432c2d4256;
  local_d0 = 0x6b315e434707412d;
  local_c8 = 0x5e54491c6e3b0a5a;
  local_c0 = 0x2828475e05342b1a;
  local_b8 = 0x60450073b26111f;
  local_b0 = 0xa774803050b0d04;
  local_a8 = 0;
  printf("Enter your flag: ");
  fgets((char *)&local_98,0x80,stdin);
  local_c = 0;
  if ((char)local_98 != 'r') {
    puts("Nope!");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  while (local_c < 0x7f) {
    *(byte *)((long)&local_98 + (long)local_c) =
         *(byte *)((long)&local_98 + (long)local_c) ^
         *(byte *)((long)&local_98 + (long)(local_c + 1));
    local_c = local_c + 1;
  }
  iVar1 = memcmp(&local_108,&local_98,0x61);
  if (iVar1 == 0) {
    puts("Correct!");
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  puts("Nope!");
                    /* WARNING: Subroutine does not return */
  exit(0);
```

入力したフラグ`local_98`は

* 1文字目が`r`である

* `n`文字目と`n+1`文字目をXORした結果が、`local_108`以降のデータ列と一致する

という条件を満たすので、そのようなフラグを見つけるプログラムを作成する。

```py
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
```

<!-- rarctf{3v3ry_s1ngl3_b4by-r3v_ch4ll3ng3_u535_x0r-f0r_s0m3_r34s0n_4nd_1-d0nt_kn0w_why_dc37158365} -->
