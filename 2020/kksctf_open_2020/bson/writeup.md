Not solved :(

# Try

```json
{"task_name":"bson","message_pack_data":"82a36b65795ca4666c6167dc003137372f27362f6c3203352f033f6c6c30033e292803343d2a6f0325332903282e35393803316f2f2f1c3b39032c3d3f3721"}
```

`message_pack_data`の部分を文字列に直してみると、

```
.£key\¤flagÜ.177/'6/l2.5/.?ll0.>)(.4=*o.%3).(.598.1o//.;9.,=?7!
```

となり、`key`と`flag`という単語が出てくる。

この後どうすればよいのか分からなかった...

# Solution

**[writeup]**

* https://github.com/r00tstici/writeups/tree/master/kksCTF_2020/bson

`massage_pack_data`の値は、その名の通り`MessagePack`というフォーマットになっている。

* https://msgpack.org/ja.html

これをデコードすると以下のようになる。

```json
{"key":92,"flag":[55,55,47,39,54,47,108,50,3,53,47,3,63,108,108,48,3,62,41,40,3,52,61,42,111,3,37,51,41,3,40,46,53,57,56,3,49,111,47,47,28,59,57,3,44,61,63,55,33]}
```

* [CyberChef(From Hex, From MessagePack)](https://gchq.github.io/CyberChef/#recipe=From_Hex('Space')From_MessagePack()JSON_Minify()&input=ODJhMzZiNjU3OTVjYTQ2NjZjNjE2N2RjMDAzMTM3MzcyZjI3MzYyZjZjMzIwMzM1MmYwMzNmNmM2YzMwMDMzZTI5MjgwMzM0M2QyYTZmMDMyNTMzMjkwMzI4MmUzNTM5MzgwMzMxNmYyZjJmMWMzYjM5MDMyYzNkM2YzNzIx)

`flag`と`key`とのXORをとるとフラグが得られる。

* [CyberChef(From Decimal, XOR)](https://gchq.github.io/CyberChef/#recipe=From_Decimal('Comma',false)XOR(%7B'option':'Decimal','string':'92'%7D,'Standard',false)&input=NTUsNTUsNDcsMzksNTQsNDcsMTA4LDUwLDMsNTMsNDcsMyw2MywxMDgsMTA4LDQ4LDMsNjIsNDEsNDAsMyw1Miw2MSw0MiwxMTEsMywzNyw1MSw0MSwzLDQwLDQ2LDUzLDU3LDU2LDMsNDksMTExLDQ3LDQ3LDI4LDU5LDU3LDMsNDQsNjEsNjMsNTUsMzM)

# Comment

`key`名がヒントになっていたとは... BSONについて調べまくっていた。