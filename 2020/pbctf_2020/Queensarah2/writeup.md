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

**[writeup]**

> for queensarah2, you can do a slide attack, or sqrt the permutation.
>
> slide attack was intended soln i think: 
>> https://www.robertxiao.ca/hacking/sarah2/
>
> solve script for queensarah2
>> https://github.com/captainGeech42/ctf-writeups/tree/master/pbctf2020/queensarah2
>
> [via Discord](https://discord.com/channels/748672086838607943/785302038606643231/785453953970208768)


> Here's my writeup for queensarah2 
>> https://github.com/qxxxb/ctf/tree/master/2020/pbctf/queensarah2. 
>
>I tried to explain the crypto clearly even tho my script is really bad :smiling_face_with_tear:
>
> [via Discord](https://discord.com/channels/748672086838607943/785302038606643231/785608839013597213)

> https://project-euphoria.netlify.app/blog/9-pbctf-2020/

2番目のwriteupが図で説明されていてわかりやすい。

`odd cycle`にうまく当てはまれば`S_box`を復元できるので、復号化できるようになる。

# Comment

一番シンプルな2文字の置換に着目した点はよかった。同じアルゴリズムでも確率次第でうまくいく／いかないがある問題が出題されること分かった。