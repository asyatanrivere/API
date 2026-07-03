import requests
# var olan bir kaynağın sadece belirli yerlerini ksımi olarak güncellememizi sağlar
url="https://jsonplaceholder.typicode.com/posts/1" # --> postslarda birinci veri

result=requests.delete(url)
print(f"Status code: {result.status_code}")
print(f"Json: {result.json()}")

"""
Status code: 200
Json: {}
"""