# Writeup

実行ファイルが与えられる。

```
$ ./chal
enter input with the form: flag_words_with_underscores_and_letters
give_me_flag
incorrect
enter input with the form: flag_words_with_underscores_and_letters
flag_words_with_underscores_and_letters
very funny
```

Ghidraで解析したところ、

```
azeupqd_ftq_cgqefuaz_omz_ymotuzqe_ftuzwu_bdabaeq_fa_o
```

という文字列があり、これをROT14したところ

```
onsider_the_question_can_machines_thinki_propose_to_c
```

となった。

意味が通るようにすると

```
i_propose_to_consider_the_question_can_machines_think
```

となる。これを入力したところフラグが得られた。

<!-- uiuctf{i_propose_to_consider_the_question_can_machines_think} -->
