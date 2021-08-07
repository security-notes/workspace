# Writeup

`.cap`ファイルが与えられる。

`aircrack-ng`を使って辞書攻撃をしたところ、パスワードが`nanotechnology`であることが分かった。

```bash
$ aircrack-ng megacorp-01.cap -w ~/john/rockyou.txt
Reading packets, please wait...
Opening megacorp-01.cap
Read 1914 packets.

   #  BSSID              ESSID                     Encryption

   1  E4:95:6E:45:90:24  joesheer                  WPA (1 handshake)

Choosing first network as target.

Reading packets, please wait...
Opening megacorp-01.cap
Read 1914 packets.

1 potential targets

                               Aircrack-ng 1.6

      [00:04:14] 5325566/14344391 keys tested (21254.74 k/s)

      Time left: 7 minutes, 4 seconds                           37.13%

                        KEY FOUND! [ nanotechnology ]


      Master Key     : 12 71 F9 32 8F FA BF E0 E2 80 F5 D3 F8 E0 A7 C0
                       73 E1 BB 0C AE 51 08 DA CF FD D3 7A 79 04 73 15

      Transient Key  : CF AC 16 F6 95 E1 93 05 94 A2 43 EC 52 A8 AB C7
                       46 C5 45 71 16 5F 1C 82 27 1E 8C B2 B6 7E 03 33
                       6A 16 E3 15 4E 39 4E EC 4F DB 35 3C CF 95 D7 9A
                       F7 BF 06 69 E4 4F 34 D4 04 B0 3F F2 AC D7 7B 6C

      EAPOL HMAC     : 06 C0 57 DC F4 DD 8F 2C F5 98 99 19 9E E3 45 32
```

<!-- uiuctf{nanotechnology} -->
