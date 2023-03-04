from cities import *
import http.client

'''
http client seems to be faster than request
https://stackoverflow.com/questions/39435443/why-is-python-3-http-client-so-much-faster-than-python-requests

'''

# conn = http.client.HTTPSConnection("api.weather.gov")
# for grid in cities:
#     headers = {}
#     conn.request("GET", "/gridpoints/TOP/{}/forecast".format(grid), headers)
#     res = conn.getresponse()
#     data = res.read()
#     print(data.decode("utf-8"))

    
conn = http.client.HTTPSConnection("api.weather.gov")
payload = ''
headers = {
    'User-Agent':'PostmanRuntime/7.31.1'}
for grid in cities:
    conn.request("GET", "/gridpoints/TOP/{grid}/forecast".format(grid=grid), payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
