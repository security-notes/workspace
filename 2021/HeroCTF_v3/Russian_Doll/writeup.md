# Writeup

与えられたzipファイルを解凍すると

```bash
> find ./you -type f
./you/are/about/to/get/rick/rolled/rickRollIncoming/no/iMean/really/lastWarning/flag
./you/are/about/to/get/rick/rolled/rickRollIncoming/no/iMean/really/lastWarning/toldYou/you/should/have/listened/now/stop/looking/in/someoneElse/ ...(省略)... /bonOk/flag.txt

$ find ./you -type f | xargs cat
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://www.youtube.com/watch?v=dQw4w9WgXcQ
Hero{if_yOu_gOt_HEre_By_clIcKInG_mANnUaLly_YoU_sHOuLd_REalLy_SeE_SoMeOne}
```

<!-- Hero{if_yOu_gOt_HEre_By_clIcKInG_mANnUaLly_YoU_sHOuLd_REalLy_SeE_SoMeOne} -->
