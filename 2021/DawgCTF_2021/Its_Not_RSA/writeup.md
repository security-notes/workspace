# Writeup

以下のjsonファイルが与えられる。

```json
{
	"ewfd_sodr": "evgnguextliwcmndypzdnhbshracrnpz",
	"srtosr": {
		"9": "III",
		"x": "IV",
		"b": "I",
		"i8xlec7ro": "B"
	},
	"ix99lnvs": [
		{
			"gebsiqw": "C",
			"ocnqgi": "F"
		},
		{
			"xlbienx": "L",
			"pxksnl": "V"
		},
		{
			"bloiens": "F",
			"lcnoin": "M"
		}
	],
	"ixla_gbafg": {
		"x": "AU",
		"4": "CB",
		"h": "GI",
		"g": "ZX",
		"t": "YQ",
		"z": "OS",
		"m": "FE"
	}
}
```

見た目からしてEnigmaの設定のようなので、`evgnguextliwcmndypzdnhbshracrnpz`を上記の設定で暗号化してみる。

* [CyberChef](https://gchq.github.io/CyberChef/#recipe=Enigma('3-rotor','LEYJVCNIXWPBQMDRTAKZGFUHOS','A','A','BDFHJLCPRTXVZNYEIWGAKMUSQO%3CW','C','F','ESOVPZJAYQUIRHXLNFTGKDCMWB%3CK','L','V','EKMFLGDQVZNTOWYHXUSPAIBRCJ%3CR','F','M','AY%20BR%20CU%20DH%20EQ%20FS%20GL%20IP%20JX%20KN%20MO%20TZ%20VW','AU%20CB%20GI%20ZX%20YQ%20OS%20FE',false)&input=ZXZnbmd1ZXh0bGl3Y21uZHlwemRuaGJzaHJhY3JucHo)

フラグの形式と一致した文字列が得られたので整形する。

```
DAWGCTFSPINNINGANDROTATINGROTORS
```

フラグフォーマットは`DawgCTF{}`、大文字小文字が区別されるので、平文と同じ小文字に直す。

<!-- DawgCTF{spinningandrotatingrotors} -->
