# Writeup

Git のURLが与えられるので、 clone してオブジェクトを全表示する。

`d06~` のオブジェクトの中身を見るとフラグが得られた。

```
$ git clone http://git.ritsec.club:7000/blob.git/

$ git rev-list --objects --all
a69cb6306e8b75b6762d6aa1b0279244cacf3f3b
d0644363aa853a17c9672cefff587580a43cf45e 
b9d6753be80df863c3656aa6389418d3213c96f2 
e597cc86a0881ab3028dba090f88c1cbd33ad9a4 README.md
df576e13e1ca1c4310d3260f63bef4db41218ba0 flag.txt

$ git cat-file -p d0644363aa853a17c9672cefff587580a43cf45e
RS{refs_can_b3_secret_too}
```

<!-- RS{refs_can_b3_secret_too} -->
