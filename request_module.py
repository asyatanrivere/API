import requests

url="https://w3schools.com/python/demopage.htm"

result=requests.get(url)

print(result.url) # https://www.w3schools.com:443/python/demopage.htm
print(result.status_code) # 200
print(result.reason) # OK
print(result.ok) # True
print(result.apparent_encoding) # ascii
print(result.encoding) # ISO-8859-1
print(result.content) # b'<!DOCTYPE html>\n<html>\n<body>\n\n<h1>This is a Test Page</h1>\n\n</body>\n</html>'
print(result.cookies) # <RequestsCookieJar[]>
print(result.elapsed) # 0:00:00.323360
# isteğin server'a gidip dönme süresini verir
print(result.headers)
"""
{'Content-Type': 'text/html', 'Last-Modified': 'Fri, 26 Jun 2026 11:29:34 GMT', 'Accept-Ranges': 'bytes', 'ETag': '"0638105f5dd1:0"', 'Content-Security-Policy': "frame-ancestors 'self' https://mycourses.w3schools.com https://pathfinder.w3schools.com;", 'X-Content-Security-Policy': "frame-ancestors 'self' https://mycourses.w3schools.com https://pathfinder.w3schools.com;", 'Vary': 'Accept-Encoding', 'Content-Encoding': 'gzip', 'Content-Length': '78', 'Cache-Control': 'public, max-age=30926198', 'Expires': 'Sat, 26 Jun 2027 12:29:11 GMT', 'Date': 'Fri, 03 Jul 2026 13:52:33 GMT', 'Connection': 'keep-alive', 'X-loc': 'true'}
"""
print(result.is_permanent_redirect) # False
print(result.is_redirect) # False
result.close()

url2="https://w3schools.com/python/demopage.js"

result2=requests.get(url2)

print(result2.json()) # {'firstname': 'John', 'lastname': 'Doe'}
