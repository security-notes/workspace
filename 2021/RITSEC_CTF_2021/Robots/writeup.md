# Writeup

http://34.69.61.54:5247/robots.txt を見ると

```
Allow: /flag/UlN7UjBib3RzX2FyM19iNGR9
```

という記述がある。

http://34.69.61.54:5247/flag/UlN7UjBib3RzX2FyM19iNGR9 にアクセスしてもNot Foundとなる。

UlN7UjBib3RzX2FyM19iNGR9 をBase64デコードしてみるとフラグになっている。

<!-- RS{R0bots_ar3_b4d} -->