import requests

try:
    my_url="https://w3schools.com/python/demopage.htm"
    result=requests.get(my_url)
    result.raise_for_status()
except requests.exceptions.HTTPError as e:
    print("HTTP Hatası:",e)
except Exception as err:
    print("Başka bir hata oluştu",err)
else:
    print("İstek başarılı!")

result.close() # İstek başarılı!

try:
    my_url2="https://w3schools.com/python/demopage2.htm"
    result2=requests.get(my_url2)
    result2.raise_for_status()
except requests.exceptions.HTTPError as e:
    print("HTTP Hatası:",e)
except Exception as err:
    print("Başka bir hata oluştu",err)
else:
    print("İstek başarılı!")

result2.close() 
# HTTP Hatası: 404 Client Error: Not Found for url: https://www.w3schools.com:443/python/demopage2.htm