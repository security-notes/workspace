# Writeup

`strings`コマンドで見つかった文字列を入力するとフラグが得られた。

```bash
$ strings secret
Input secret key : 
Incorrect
wani_is_the_coolest_animals_in_the_world!
Correct! Flag is %s

$ ./secret

   ▄▀▀▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▄▄▄▄   ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▀█▀▀▄
  █ █   ▐ ▐  ▄▀   ▐ █ █    ▌ █   █   █ ▐  ▄▀   ▐ █    █  ▐
     ▀▄     █▄▄▄▄▄  ▐ █      ▐  █▀▀█▀    █▄▄▄▄▄  ▐   █
  ▀▄   █    █    ▌    █       ▄▀    █    █    ▌     █
   █▀▀▀    ▄▀▄▄▄▄    ▄▀▄▄▄▄▀ █     █    ▄▀▄▄▄▄    ▄▀
   ▐       █    ▐   █     ▐  ▐     ▐    █    ▐   █
           ▐        ▐                   ▐        ▐

Input secret key : wani_is_the_coolest_animals_in_the_world!
Correct! Flag is FLAG{ana1yze_4nd_strin6s_and_execu7e_6in}
```

<!-- FLAG{ana1yze_4nd_strin6s_and_execu7e_6in} -->
