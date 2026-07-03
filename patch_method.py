import requests
# var olan bir kaynağın sadece belirli yerlerini ksımi olarak güncellememizi sağlar
url="https://jsonplaceholder.typicode.com/posts/1" # --> postslarda birinci veri

data={
    "title": "Updated Title"
  
}

result=requests.patch(url,json=data)
print(f"Status code: {result.status_code}")
print(f"Json: {result.json()}")

"""
Status code: 200
Json: {'userId': 1, 
       'id': 1, 
       'title': 'Updated Title', 
       'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}"""