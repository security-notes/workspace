# Writeup

`main.s`に書かれている以下の部分を文字列に直してみる。

```
	movabsq	$7941081424088616006, %rax
	movabsq	$7311705455698409823, %rdx
	movabsq	$3560223458505028963, %rax
	movabsq	$35295634984951667, %rdx
```

```
n4c{GALF
exe_u0y_
1ht_e4uc
}e1if_s
```

逆さまに読んでつなぎ合わせれば良さそう。

```py
value = [7941081424088616006, 7311705455698409823, 3560223458505028963, 35295634984951667]

flag = ""
for v in value:
    flag += bytes.fromhex(hex(v)[2:]).decode('utf-8')[::-1]
print(flag)
```

<!-- FLAG{c4n_y0u_execu4e_th1s_fi1e} -->
