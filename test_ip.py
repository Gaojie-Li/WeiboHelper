import urllib.request
import socket
socket.setdefaulttimeout(10)
f = open("./proxy/proxy")
lines = f.readlines()
proxys = []
for i in range(0,len(lines)):
    ip = lines[i].strip("\n").split("\t")
    proxy_host = "http://"+ip[0]+":"+ip[1]
    proxy_temp = {ip[2]:proxy_host}
    proxys.append(proxy_temp)
url = "http://ip.chinaz.com/getip.aspx"
for proxy in proxys:
    try:
        req = urllib.request.Request(url)
        type = list(proxy.keys())[0]
        req.set_proxy(proxy[type], type.lower())
        res = urllib.request.urlopen(req).read()
        print(res)
    except Exception as e:
        print(proxy)
        print(e)
        continue
