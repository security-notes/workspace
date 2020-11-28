# Writeup

`https://simple.wanictf.org/index.php?file=test.txt`のように`file`パラメータの先にファイルパスを指定して表示する仕組みになっている。

ディレクトリトラバーサルであるというヒントがあるので、相対パス指定の`../`を使いたいところだが、そのままではサニタイズされているので工夫が必要。

`../`を` `(空白)に置換するので、`....//`を与えれば、結果は`../`となる。

よって、`https://simple.wanictf.org/index.php?file=....//flag.txt`とすればよい。

`index.php`と同じディレクトリに置かれているので、`https://simple.wanictf.org/flag.txt`にアクセスしてもフラグが得られる。

<!-- FLAG{y0u_c4n_get_hi5_5ecret_fi1e} -->