# Writeup

zipファイルにはパスワードがついているので、`Volatility`を使って常用しているパスワードを調べる。

[参考]

* https://www.aldeid.com/wiki/Volatility/Retrieve-password

```bash
$ vol.py -f ALLIGATOR.raw  --kdbg=0x82754de8 --profile=Win7SP1x86_23418 hivelist
Volatility Foundation Volatility Framework 2.6.1
Virtual    Physical   Name
---------- ---------- ----
0x96833008 0x29f35008 \??\C:\System Volume Information\Syscache.hve
0x9a37a008 0x0edcf008 \??\C:\Users\ALLIGATOR\ntuser.dat
0x9a37c008 0x0eed1008 \??\C:\Users\ALLIGATOR\AppData\Local\Microsoft\Windows\UsrClass.dat
0x8780a6b8 0x282fb6b8 [no name]
0x8781a008 0x28349008 \REGISTRY\MACHINE\SYSTEM
0x87838218 0x28367218 \REGISTRY\MACHINE\HARDWARE
0x8b0599c8 0x248859c8 \??\C:\Windows\ServiceProfiles\LocalService\NTUSER.DAT
0x8cb07008 0x26f46008 \Device\HarddiskVolume1\Boot\BCD
0x8e7f7008 0x26313008 \SystemRoot\System32\Config\SOFTWARE
0x904655f8 0x225685f8 \??\C:\Users\IEUser\ntuser.dat
0x9144b5c0 0x260205c0 \SystemRoot\System32\Config\DEFAULT
0x937338d0 0x250778d0 \SystemRoot\System32\Config\SECURITY
0x93791458 0x1d940458 \SystemRoot\System32\Config\SAM
0x937b79c8 0x248899c8 \??\C:\Users\IEUser\AppData\Local\Microsoft\Windows\UsrClass.dat
0x937fb758 0x248dd758 \??\C:\Windows\ServiceProfiles\NetworkService\NTUSER.DAT
0x96449458 0x03f4f458 \??\C:\Users\sshd_server\ntuser.dat
0x9645d3d8 0x2830b3d8 \??\C:\Users\sshd_server\AppData\Local\Microsoft\Windows\UsrClass.dat
```

```bash
$ vol.py -f ALLIGATOR.raw  --kdbg=0x82754de8 --profile=Win7SP1x86_23418 hashdump -y 0x8781a008 -s 0x93791458
Volatility Foundation Volatility Framework 2.6.1
Administrator:500:aad3b435b51404eeaad3b435b51404ee:fc525c9683e8fe067095ba2ddc971889:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
IEUser:1000:aad3b435b51404eeaad3b435b51404ee:fc525c9683e8fe067095ba2ddc971889:::
sshd:1001:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
sshd_server:1002:aad3b435b51404eeaad3b435b51404ee:8d0a16cfc061c3359db455d00ec27035:::
ALLIGATOR:1003:aad3b435b51404eeaad3b435b51404ee:5e7a211fee4f7249f9db23e4a07d7590:::
```

[crackstation](https://crackstation.net/)を使うと、`5e7a211fee4f7249f9db23e4a07d7590`は`ilovewani`であることがわかる。

zipファイルのパスワードは`ilovewani`で、中身を見るとフラグが書かれたテキストファイルがある。

<!-- FLAG{The_Machikane_Crocodylidae} -->