# Writeup

[前問](../We_need_you_1_5)で与えられたMEMファイルから開いているアドレスとポートを探す。

```bash
$ vol.py -f capture.mem --kdbg=0x82780c28 --profile=Win7SP1x86 netscan
Volatility Foundation Volatility Framework 2.6.1
Offset(P)          Proto    Local Address                  Foreign Address      State            Pid      Owner          Created
0x7ee41538         TCPv4    10.0.2.15:49159                146.59.156.82:4444   ESTABLISHED      3296     nc.exe         
```

`146.59.156.82:4444`へ`nc.exe`が接続を確立していることが分かる。

<!-- Hero{146.59.156.82:4444} -->
