# Writeup

以下のコードが書かれたファイルと、パスワード付きのzipファイルが与えられる。

```
::the::
Send, +wani
return

::password::
Send, +c+t+f
return

::for::
Send, {home}{right 3}{del}1{end}{left 2}{del}7
return

::today::
FormatTime , x,, yyyyMMdd
SendInput, {home}{right 4}_%x%
return

::is::
Send, _{end}{!}{!}{left}
return

:*?:ni::
Send, ^a^c{Esc}{home}password{:} {end}
return
```

これはAutoHotKeyのスクリプトであるので、拡張子を`.ahk`に変えて実行する。

* [AutoHotkeyのダウンロードとインストール](http://autohotkey.s365.xrea.com/download_install.html)

`the`と入力すると`::the::`内が実行される仕組みになっている。

スクリプトを起動した状態で、テキストエディタ等で`the password for today is nani`とキーボード入力してみると`password: Wan1_20210501_C7F!na!`と自動的に入力される。

`today`は動的に実行した日付が入るようになっているので、zipファイルの日付に合わせると、`Wan1_20210428_C7F!na!`がzipファイルのパスワードになっていた。

zipファイルの中身に画像ファイルが入っており、フラグが書かれていた。

<!-- FLAG{Nani!very_strong_password!} -->
