import requests

url="https://jsonplaceholder.typicode.com/posts/1" # --> postslarda birinci veri

data={
    "userId": 1,
    "title": "Updated Title",
    "body": "This is an updated content."
  
}

result=requests.put(url,json=data)
print(f"Status code: {result.status_code}")
print(f"Json: {result.json()}")