Not solved :(

# Try

提示された5つのリンクのうち、http://34.68.159.75:55275/ だけアクセスできる。

さらに2つリンクがあって、上ではJavaScript、下ではCSSが読み込まれる。

![](img/2020-12-06-12-54-56.png)

`JavaScript`

```js
// FOrce the user to click okay many times

console.log("uhmm you asked for it!!");

var i;



for (i  = 0; i < 100000;  i++)
  alert("Hello world!1!!!! ");


//ahh you disabled them :*(
//
document.write("Ahh why did you disable those dialogs...? We were having a lot of fun! ;)");
```

```css
@font-face {
    font-family: ComicSans;
    src: url(ComicSansMS3.ttf);
}

body {
  font-family: ComicSans;
}

.bold {
  font-weight: bold;
}

.it {
  font-style: italic;
}

.mono {
  font-family: Monospace;
}
```

手がかりがつかめず...

# Solution

**[writeup]**

* https://github.com/0xbigshaq/ctf-stuff/tree/main/perfect-blue-ctf-2020/apoche

`robots.txt`を使ってディレクトリ構造を確かめる。

こうして見つかった`secrets`ディレクトリの中にヒントがあるので、それをもとにディレクトリトラバーサルでフラグを入手。

(2020/12/07 サーバーが立ち上がっていないので確認できず...)

## Comment

Web問題で`robots.txt`を手がかりにするというのは、pwn問題でいうところの表層解析に等しいのかもしれないと思った。
