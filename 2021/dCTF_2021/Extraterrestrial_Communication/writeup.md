# Writeup

QSSTVを使って音声ファイルから画像ファイルが生成できないか試してみる。

mp3のままでは上手くいかなかったのでwavに変換する。

```
$ ffmpeg -i "A_message_from_outer_space.mp3" -vn -ac 2 -ar 44100 -acodec pcm_s16le -f wav "out.wav"

# Settings
$ pactl load-module module-null-sink sink_name=virtual-cable
$ pavucontrol &
$ qsstv &

$ paplay -d virtual-cable out.wav
```

すると、以下の画像が表示された。

![](flag.png)

<!-- dctf{wHat_ev3n_1s_SSTV} -->
