# Writeup

`.git`があるので`git clone`する。

```bash
$ git clone http://git.ritsec.club:7000/1597.git/
```

branch一覧を見ると、`!flag`ブランチがあることがわかる。

```
$ git branch -a
  master
  remotes/origin/!flag
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
```

`!flag`ブランチに切り替え、`flag.txt`を見るとフラグが書かれている。

```
$ git checkout !flag
$ cat flag.txt
```

<!-- RS{git_is_just_a_tre3_with_lots_of_branches} -->