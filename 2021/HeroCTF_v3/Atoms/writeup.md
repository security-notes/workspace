# Writeup

以下のテキストファイルが与えられる。

```
MtMdDsFmMdHsMdMdUuo
```

問題タイトルの`Atoms`から、これらのアルファベットの羅列が元素記号だと推測。原子番号をASCIIに直すと`mendeleev`となる。

```py
c = "MtMdDsFmMdHsMdMdUuo"
atoms = { "Mt": 109, "Md": 101, "Ds": 110, "Fm": 100, "Hs": 108, "Uuo": 118}
for key, value in atoms.items():
    c = c.replace(key,chr(value))
print(c)
```

<!-- Hero{mendeleev} -->