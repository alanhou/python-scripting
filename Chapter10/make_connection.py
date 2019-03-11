import http.client

con_obj = http.client.HTTPConnection("https://www.baidu.com", 80, timeout=20)
print(con_obj)
