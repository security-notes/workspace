# Writeup

暗号文`egddagzp_ftue_rxms_iuft_rxms_radymf`と、以下のプログラムが与えられる。

```py
import random

key = random.randint(0, 25)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
shifted = alphabet[key:] + alphabet[:key]
dictionary = dict(zip(alphabet, shifted))

print(''.join([
    dictionary[c]
    if c in dictionary
    else c
    for c in input()
]))
```

ランダムな数でローテーションシフトしていることが分かる。

ROT14したところ、意味のある英文になった。

* [CyberChef](https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,14)&input=ZWdkZGFnenBfZnR1ZV9yeG1zX2l1ZnRfcnhtc19yYWR5bWY)

<!-- flag{surround_this_flag_with_flag_format} -->
