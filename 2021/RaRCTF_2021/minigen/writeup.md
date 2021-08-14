# Writeup

以下のプログラムと出力結果が与えられる。

```py
exec('def f(x):'+'yield((x:=-~x)*x+-~-x)%727;'*100)
g=f(id(f));print(*map(lambda c:ord(c)^next(g),list(open('f').read())))
```

```
281 547 54 380 392 98 158 440 724 218 406 672 193 457 694 208 455 745 196 450 724
```

暗号化は`((x:=-~x)*x+-~-x)%727 * ord(c)`によって行われている。

`x:=-~x`は`x>0`のとき`x:=x+1`に等しいので、`x`の値は`f(x)`の中で1ずつ増えていく。

また、`((x:=-~x)*x+-~-x)%727`を変形すると、`((x+1)*(x+1)+(-x))%727 = (x^2 + x + 1)%727`となる。

差は`f(x+1)-f(x) = 2x + 2 (mod 727)`であり`x`によって決まる固定値を取り続けるので、差が同じになるような`ord(c)`の`c`を見つける。

```py
import string

CHAR = string.printable

ct = [281, 547, 54, 380, 392, 98, 158, 440, 724, 218, 406, 672, 193, 457, 694, 208, 455, 745, 196, 450, 724]
flag = 'ra' # rarctf{

s, t, u = ct[0]^ord('r'), ct[1]^ord('a'), ct[2]^ord('r')
d = (t-s)%727
diff = ((u-t)%727 - d)

for idx in range(2,len(ct)):
    for c in CHAR:
        u = ct[idx]^ord(c)
        if d + diff == (u-t)%727:
            flag += c
            d = (u-t)%727
            s = t
            t = u
            break
print(flag)
```

<!-- rarctf{pyg01f_1s_fun} -->


