# Writeup

`nc netcat.pwn.wanictf.org 9001`を実行すると`ls`と入力するように言われる。

`flag.txt`があるので`cat`してみる。

```
$ nc netcat.pwn.wanictf.org 9001
congratulation!
please enter "ls" command
ls
chall
flag.txt
redir.sh


cat flag.txt
FLAG{this_is_the_same_netcat_problem_as_previous_one}
```

<!-- FLAG{this_is_the_same_netcat_problem_as_previous_one} -->
