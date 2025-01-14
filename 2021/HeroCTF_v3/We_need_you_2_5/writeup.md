# Writeup

[前問](../We_need_you_1_5)で与えられたMEMファイルからユーザー名とパスワードを探す。

```bash
$ vol.py -f capture.mem --kdbg=0x82780c28 --profile=Win7SP1x86 hivelist
Volatility Foundation Volatility Framework 2.6.1
Virtual    Physical   Name
---------- ---------- ----
0x823859c8 0x2b5d99c8 \SystemRoot\System32\Config\SAM
0x8941a2c0 0x2d58d2c0 \REGISTRY\MACHINE\SYSTEM

$ vol.py -f capture.mem --kdbg=0x82780c28 --profile=Win7SP1x86 hashdump -y 0x8941a2c0 -s 0x823859c8
Volatility Foundation Volatility Framework 2.6.1
Razex:1000:aad3b435b51404eeaad3b435b51404ee:78d9c7e905c695087ee3baa755ce43e4:::
```

`78d9c7e905c695087ee3baa755ce43e4`を`CrackStation`でハッシュを解読すると、`liverpoolfc123`となっており、これがパスワードである。

![](img/2021-04-24-21-44-39.png)

[参考]

* [Volatility/Retrieve-password](https://www.aldeid.com/wiki/Volatility/Retrieve-password)

<!-- Hero{Razex:liverpoolfc123} -->
