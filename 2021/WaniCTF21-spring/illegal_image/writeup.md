# Writeup

pcapファイルが与えられる。画像のやり取りがあることが分かっているので、jpgファイルのファイル識別子である`ff d8 ff`で検索した。

検索した結果、ICMP通信でやり取りが行われていると推測。

ICMP通信のみを抜き出し、Data部分をつなぎ合わせてjpgファイルとして出力した。

```
import os
from scapy.all import rdpcap

pcap = rdpcap(os.path.dirname(__file__)+'/icmp.pcap')

data = [p.load for p in pcap]

with open(os.path.dirname(__file__)+'/flag.jpg','wb') as f:
    for d in data:
        f.write(d)
```

![](./flag.jpg)

[参考]

* [Data exfiltration with PING: ICMP - NDH16](https://www.boiteaklou.fr/Data-exfiltration-with-PING-ICMP-NDH16.html)


<!-- FLAG{ICMP_Exfiltrate_image} -->
