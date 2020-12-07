Not solved :(

# Try

`nc`コマンドを実行してみると文字列が出力され、パスワードを求められる。

入力したパスワードが違ったときは、そのパスワードを暗号化してくれるっぽい。

```bash
$ nc queensarah2.chal.perfect.blue 1
This is a restricted service! Decrypt this password to proceed:
{'ywflzvbwvvyrmtfsgwiuanwgxpdfmztdgcgvqalohrnibwjl_pxrwiuaou'}
> password
That's not quite right. Your password encrypts to this:
vbfxjxpn
> hello
That's not quite right. Your password encrypts to this:
qw_qxn
> pbctf
That's not quite right. Your password encrypts to this:
bdqlck
> a
That's not quite right. Your password encrypts to this:
y_
> aa
That's not quite right. Your password encrypts to this:
sr
> aaa
That's not quite right. Your password encrypts to this:
lguh
```

プログラムを読むと、以下のように暗号化していることが分かる。

例として、文字列 `hello` を暗号化する手順を示す。

---

1. `[a-z_]`のバイグラムを別のバイグラムに対応させた辞書`S_box`をランダムに作る(27\*27通り)

    `{'he':'de', 'll':'dg', 'o_':'at' , ...}`

1. 入力文字列の長さが奇数なら末尾に'_'をつける

    `hello` ⇒ `hello_`

1. 辞書をもとに先頭から2文字ずつ変換する

    `hello_` ⇒　`dedgat`

1. 文字列を偶数番目と奇数番目に分けてつなげる（シャッフル）

    `dedgat` ⇒ `dda`+`egt` ⇒ `ddaegt`

1. 2~4 を `2 * ceil(log(len(message), 2))`回繰り返す　(ただし最後の1回はシャッフルしない)

    `hello_` ⇒ `ddaegt` ⇒ `fgjtth` ⇒ `vlvued` ⇒ `ziagnh` ⇒ `yxl_tz` ⇒ `xnqsfv`

---

復号化するためには、辞書`S_box`の逆対応表があればよい。（`he`⇒`de`が暗号化なら`de`⇒`he`は復号化）

ただし`len(message)=2`のとき、2回暗号化されてしまうため、単純に逆にすれば求まるわけではない。((input)`he`⇒`de`⇒`??`(output))

暗号化の方式は俗にいうブロック暗号なので、何か解読手段はないかと模索...

* https://ja.wikipedia.org/wiki/ブロック暗号#ショートカット法

# Solution