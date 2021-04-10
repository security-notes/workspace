# Writeup

はじめに用意されたシェルサーバーへアクセスする。

```
The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

Welcome to the
                       _                            _    __
   ()                 | |                          | |  / _|
  __ _ _ __   __ _ ___| |_ _ __ ___  _ __ ___   ___| |_| |_
 / _` | '_ \ / _` / __| __| '__/ _ \| '_ ` _ \ / __| __|  _|
| (_| | | | | (_| \__ \ |_| | | (_) | | | | | | (__| |_| |
 \__,_|_| |_|\__, |___/\__|_|  \___/|_| |_| |_|\___|\__|_|
              __/ |
             |___/

shell server!

*==============================================================================*
*  Please be respectful of other users. Abuse may result in disqualification.  *
*Data can be wiped at ANY TIME with NO WARNING. Keep backups of important data!*
*==============================================================================*
team8861@actf:~$
```

`/problems/2021/archaic/archive.tar.gz`を取ってくる。

```bash
$ cp /problems/2021/archaic/archive.tar.gz ./
```

拡張子が`.tar`なので解凍する。

```bash
$ tar -xzvf archive.tar.gz
flag.txt
```

`flag.txt`の中身を見る。読み取り権限がないので、権限をつけてから読む。

```bash
$ cat flag.txt
cat: flag.txt: Permission denied

$ ls -la flag.txt
---------- 1 team8861 team8861 37 Apr  1  1921 flag.txt

$ chmod +r flag.txt

$ ls -la flag.txt
-r--r--r-- 1 team8861 team8861 37 Apr  1  1921 flag.txt

$ cat flag.txt
actf{thou_hast_uncovered_ye_ol_fleg}
```

<!-- actf{thou_hast_uncovered_ye_ol_fleg} -->