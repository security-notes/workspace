# Writeup

添付の`babymix`を実行するとパスワードが求められる。

```
With our propietary babymix™ technology, we assure you that this password cannot be stolen, modified, or tampered with!

Please enter your admin password: aaa

Incorrect :(
```

angr を使って調べる。

```
$ python solver.py
b'm1x_it_4ll_t0geth3r!1!\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00 @\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
```

<!-- dice{m1x_it_4ll_t0geth3r!1!} -->