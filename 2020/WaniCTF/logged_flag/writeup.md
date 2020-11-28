# Writeup

キーボードの入力が記録されているようなので見やすくする。

```py
import re

cmd = ''

with open('./key_log.txt') as f:
    for _ in range(317):
        line = f.readline()
        key = re.findall(r'(?<=\[).+?(?=\])',line)
        if len(key) == 0:
            continue
        if key[0] == 'Enter':
            cmd += '\n'
        elif key[0] == 'Shift':
            continue
        elif key[0] == 'Space':
            cmd += ' '
        elif key[0] == 'BackSpace':
            cmd = cmd[:-1]
        else:
            cmd += key[0].lower()
    
    print(cmd)
```

```bash
$ python3 solver.py 
mkdir steghide
cp original.jpg ./steghide
cd steghide
echo flag[k3y-l0gg3r-1s-v3ry-d4ng3r0us] . flag.txt
steghide embed -cf original.jpg -ef flag.txt -sf secret.jpg
machikanetamachikanesai
machikanetamachikanesai
steghide extract -sf secret.jpg
machikanetamachikanesai
ycat flag.txt
```

`Shift`の部分を適用して`FLAG{}`の形式にする。

英字配列のキーボードなので、`-`のシフト入力は`_`に読み替える。

<!-- FLAG{k3y_l0gg3r_1s_v3ry_d4ng3r0us} -->