# Writeup

先頭行のメッセージを調べると、`Trithemius Ave Maria`という暗号であることがわかる。以下のサイトで復号化する。

* https://www.dcode.fr/trithemius-ave-maria

```
RSTHISISTRITHEMIUS
```

case sensitive なので、大文字小文字の区別をしなければならない。

暗号文の単語の先頭が大文字か小文字かで区別したところ正しいフラグが得られた。

<!-- RS{ThIsIsTrItHeMiUs} -->