import http.client

con_obj = http.client.HTTPSConnection("www.imdb.com")
con_obj.request("GET", "/")
response = con_obj.getresponse()

print("Status: {}".format(response.status))

headers_list = response.getheaders()
print("Headers: {}".format(headers_list))

con_obj.close()
