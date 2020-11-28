# Writeup

`file`コマンドを使ってファイル形式を調べる。

```bash
$ file eaten.png 
eaten.png: data
```

どうやらただのPNGファイルではなさそう。イメージとしても開けない。

`srtings`コマンドを使ってみると、`WANI`という単語が出現する。

```bash
$ strings eaten.png | head -n 10
WANI
sRGB
gAMA
	pHYs
tEXtSoftware
Adobe ImageReadyq
$iTXtXML:com.adobe.xmp
<?xpacket begin="
" id="W5M0MpCehiHzreSzNTczkc9d"?> <x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.3-c011 66.145661, 2012/02/06-14:56:27        "> <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"> <rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/" xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/" xmlns:stRef="http://ns.adobe.com/xap/1.0/sType/ResourceRef#" xmp:CreatorTool="Adobe Photoshop CS6 (Macintosh)" xmpMM:InstanceID="xmp.iid:A12986FEBD5C11E3A38AFE01A4935390" xmpMM:DocumentID="xmp.did:A12986FFBD5C11E3A38AFE01A4935390"> <xmpMM:DerivedFrom stRef:instanceID="xmp.iid:A12986FCBD5C11E3A38AFE01A4935390" stRef:documentID="xmp.did:A12986FDBD5C11E3A38AFE01A4935390"/> </rdf:Description> </rdf:RDF> </x:xmpmeta> <?xpacket end="r"?>
PWANIx^

$ strings eaten.png | grep WANI
WANI
PWANIx^
WANI
WANI
WANI
```

最初のWANIをIHDR, 最後のWANIをIEND, それ以外のWANIをIDATにするとPNGとして画像を見ることができる。

* [PNGファイルフォーマット](https://www.setsuki.com/hsp/ext/png.htm)

バイナリの書き換えには`青い空を見上げればいつもそこに白い猫 for うさみみハリケーン`を使用した。

<!-- FLAG{chunk_is_so_yummy!} -->