Not solved :(

# Try

Goプログラムのmain関数の中身を見ると、`(command)|(base64)` の形式でを入力すればよいことがわかる。

```go
var commands = []string{
	"flag",
	"debug",
}
```

```go
input = strings.TrimSpace(input)
components := strings.Split(input, "|")
if len(components) < 2 {
    fmt.Println("command must contain hmac signature")
    continue
}

command := components[0]
check, err := base64.StdEncoding.DecodeString(components[1])
if err != nil {
    fmt.Println("hmac must be base64")
    continue
}

if !contains(commands, command) {
    fmt.Println("invalid command")
    continue
}
```

問題文中の`9W5iVNkvnM6igjQaWlcN0JJgH+7pComiQZYdkhycKjs=`がBase64文字列っぽいので、入力してみる。

```bash
$ nc challenges.2020.squarectf.com 9020

Enter command: flag|9W5iVNkvnM6igjQaWlcN0JJgH+7pComiQZYdkhycKjs=
invalid hmac

Enter command: debug|9W5iVNkvnM6igjQaWlcN0JJgH+7pComiQZYdkhycKjs=
debug mode enabled
-----------DEBUG MODE ENABLED-----------

Enter command: flag|9W5iVNkvnM6igjQaWlcN0JJgH+7pComiQZYdkhycKjs=
command: flag, check: 9W5iVNkvnM6igjQaWlcN0JJgH+7pComiQZYdkhycKjs=
took 666178 nanoseconds to verify hmac
invalid hmac
```

どうやら上のBase64文字列がデバッグコマンドを実行するために必要な文字列になっているらしい。

```go
check, err := base64.StdEncoding.DecodeString(components[1])
if err != nil {
    fmt.Println("hmac must be base64")
    continue
}

if !hmacWrapper.verifyHmac(command, check) {
    fmt.Println("invalid hmac")
    continue
}
```

```go
func (h *HmacVerifier) verifyHmac(message string, check []byte) bool {
	start := time.Now()
	match := compare(h.codes[message], check)
	verifyTime := time.Since(start).Nanoseconds()

	if debug {
		fmt.Printf("took %d nanoseconds to verify hmac\n", verifyTime)
	}

	return match
}
```

`flag|(flagに対応するbase64)`を入力すればフラグが表示されそうだと分かる。

プログラムを読むと`flagに対応するbase64`は、`flag`を`key`でSHA256変換⇒文字列変換⇒base64変換という流れで計算されている。

```
flag を squarectf で SHA256 変換 (HMAC方式)

    32500c064e1eb1053b70ea0a6edc4eb5bc6ab25d1316b413f35e6f9a44e6a9ac

文字列変換

    2P..N.±.;pê nÜNµ¼j²]..´.ó^o.Dæ©¬

Base64変換

    MlAMBk4esQU7cOoKbtxOtbxqsl0TFrQT815vmkTmqaw=
```

もし、keyの中身が`squarectf`なら`flag|MlAMBk4esQU7cOoKbtxOtbxqsl0TFrQT815vmkTmqaw=`と入力すればフラグが得られるということになる。

* [CyberChef](https://gchq.github.io/CyberChef/#recipe=HMAC(%7B'option':'UTF8','string':'squarectf'%7D,'SHA256')From_Charcode('CRLF',16)To_Base64('A-Za-z0-9%2B/%3D')&input=ZmxhZw)

わざわざ`compare`関数内で`time.Sleep`しているので、デバッグモード内で時間を見ることが重要であると推測。バイト列を先頭から比較していく仕組みになっている。

```go
func compare(s1, s2 []byte) bool {
	if len(s1) != len(s2) {
		return false
	}

	c := make(chan bool)

	// multi-threaded check to speed up comparison
	for i := 0; i < len(s1); i++ {
		go func(i int, co chan<- bool) {
			// avoid race conditions
			time.Sleep(time.Duration(((500*math.Pow(1.18, float64(i+1)))-500)/0.18) * time.Microsecond)
			co <- s1[i] == s2[i]
		}(i, c)
	}

	for i := 0; i < len(s1); i++ {
		if <-c == false {
			return false
		}
	}

	return true
}
```

試しに、debugの成功時と失敗時の時間を計ってみると明らかに時間差があることが確認できた。

```
$ nc challenges.2020.squarectf.com 9020
Enter command: debug|9W5iVNkvnM6igjQaWlcN0JJgH+7pComiQZYdkhycKjs=
debug mode enabled
-----------DEBUG MODE ENABLED-----------

Enter command: debug|9W5iVNkvnM6igjQaWlcN0JJgH+7pComiQZYdkhycKjs=
command: debug, check: 9W5iVNkvnM6igjQaWlcN0JJgH+7pComiQZYdkhycKjs=
took 552108195 nanoseconds to verify hmac
debug mode disabled

Enter command: debug|9W5iVNkvnM6igjQaWlcN0JJgH+7pComiQZYdkhycKjs=
debug mode enabled
-----------DEBUG MODE ENABLED-----------

Enter command: debug|8W5iVNkvnM6igjQaWlcN0JJgH+7pComiQZYdkhycKjs=
command: debug, check: 8W5iVNkvnM6igjQaWlcN0JJgH+7pComiQZYdkhycKjs=
took 712276 nanoseconds to verify hmac
invalid hmac
```

時間の情報をもとに1バイト目から順に確定させていくプログラムを作成した。

```py
from pwn import *
import base64
import struct
import re

conn = remote('challenges.2020.squarectf.com',9020)

# debug mode
conn.recvuntil('Enter command:',drop=True)
conn.sendline('debug|9W5iVNkvnM6igjQaWlcN0JJgH+7pComiQZYdkhycKjs=')
conn.recvuntil('Enter command:',drop=True)

result = [0 for _ in range(2**8)]

payload = b''

for j in range(1,33):

    buf = b'\x00'*(32-j)

    top = [k for k in range(2**8)]
    while len(top) != 1:
        for i in range(2**8):
            if i not in top:
                continue
            data = struct.pack("B",i) # \x00 - \xff
            data = payload + data + buf
            b64_data = base64.b64encode(data).decode()
            conn.sendline('flag|' + b64_data)
            conn.recvline()
            msg = conn.recvline().decode() # time info
            varify_time = int(re.sub(r"\D","",msg)) 
            result[i] = [varify_time,i]
            print(i,msg,end='') # for debug
            skip = conn.recvuntil('Enter command:',drop=True)
            if(j == 32):
                print(skip) # flag check

        sort_result = sorted(result,reverse=True)
        topgroup = [x[1] for x in sort_result][:10] # just in case
        top = [x for x in top if x in topgroup]
        print('top: ', top)

    payload += struct.pack("B",top[0])
    print('payload: ', payload)
```

時間はかかるがフラグを入手。

<!-- flag{d1d_u_t4k3_the_71me_t0_appr3c14t3_my_c0mm4nd5} -->