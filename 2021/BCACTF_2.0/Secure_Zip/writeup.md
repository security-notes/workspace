# Writeup

パスワード付きのzipファイルが与えられる。

```bash
$ zip2john chall.zip > chall_hash

$ john chall_hash --wordlist=rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 16 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
dogedoge         (chall.zip)
```

john the ripper で解析すると、パスワードは`dogedoge`であることが分かった。

zipファイル内のテキストにフラグが書かれていた。

<!-- bcactf{cr4ck1ng_z1p_p455w0rd5_15_fun_a12ca37bdacef7} -->
