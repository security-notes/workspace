# Writeup

Volatilityを使って.memファイルを解析する。

ヒントによると、メモ帳に表示されている文字が怪しそうなので、以下のコマンドを実行し`notepad.exe`を解析する。

```bash
$ vol.py -f image.mem imageinfo
$ vol.py -f image.mem --kdbg=0xf80002a3b0a0 --profile=Win7SP1x64 pstree
$ vol.py -f image.mem --kdbg=0xf80002a3b0a0 --profile=Win7SP1x64 memdump -D ./ -p 2696
$ strings -e l 2696.dmp | grep "UMASS"
UMASS{$3CUR3_$70Rag3}
```

[参考]

* [Volatility tips: how to extract text typed in a notepad window from a Windows memory dump](https://www.andreafortuna.org/2018/03/02/volatility-tips-extract-text-typed-in-a-notepad-window-from-a-windows-memory-dump/)