# Writeup

```
rq7t{7vH_rFH_vI6_pHH1_qI67}
```

というテキストが与えられる。

ROT12すると以下のようになる。

```
dc7f{7hT_dRT_hU6_bTT1_cU67}
```

フラグフォーマットは`dctf{}`なので`7`を`t`に置換する。

```
dctf{thT_dRT_hU6_bTT1_cU6t}
```

同様に数字は、`1,2,3,4,5,6,7` -> `n,o,p,q,r,s,t` に置換する。

```
dctf{thT_dRT_hUs_bTTn_cUst}
```

断片的な単語から、元の文は`the die has been cast`であると推測。

Leetにもちょうど当てはまるようにできているので、`R,S,T,U` -> `1,2,3,4` に置換する。

```
dctf{th3_d13_h4s_b33n_c4st}
```

これがフラグになっていた。

<!-- dctf{th3_d13_h4s_b33n_c4st} -->