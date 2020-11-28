# Writeup

`nc lcg.wanictf.org 50001`を実行。

```bash
$ nc lcg.wanictf.org 50001


     :::       .,-:::::  .,-:::::/
     ;;;     ,;;;'````',;;-'````'
     [[[     [[[       [[[   [[[[[[/
     $$'     $$$       "$$c.    "$$
    o88oo,.__`88bo,__,o,`Y8bo,,,o88o
    """"YUMMM  "YUMMMMMP" `'YMUP"YMM



      +=============================+
      | 1. Generate the next number |
      | 2. Guess the next number    |
      | 3. Exit                     |
      +=============================+

 - Guess the numbers in a row, and I'll give you a flag!
> 1
11570939290553957957
```

`1`で乱数を生成、`2`で乱数を予測できる。

どうやら、次の乱数を当て続ければフラグを取得できそう。

しかし、プログラムを読むと`ValueError`でも`continue`する（先に進んでしまう）ので、`int`以外を入れ続けてもよい。

```py
except ValueError:
    print("Please enter an integer\n\n\n")
    continue
```

おそらく、非想定解だが...

```bash
> 2
 - [1/10] Guess the next number!
> dasd
Please enter an integer

 - [2/10] Guess the next number!
> adsa
Please enter an integer

 - [3/10] Guess the next number!
> dsa
Please enter an integer

 - [4/10] Guess the next number!
> ds
aPlease enter an integer

 - [5/10] Guess the next number!
> fs
Please enter an integer

 - [6/10] Guess the next number!
> fa
Please enter an integer

 - [7/10] Guess the next number!
> sa
Please enter an integer

 - [8/10] Guess the next number!
> dsa
Please enter an integer

 - [9/10] Guess the next number!
> d
Please enter an integer

 - [10/10] Guess the next number!
> a
Please enter an integer

Congratz!　FLAG{
```

<!-- FLAG{y0u_sh0uld_buy_l0tt3ry_t1ck3ts} -->
