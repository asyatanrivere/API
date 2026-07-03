import requests
# yeni data ekler
url="https://jsonplaceholder.typicode.com/posts"

data={
    "userId": 11,
    "title": "Monte Kristo Kontu",
    "body": "bir intikam hikayesi"
  
}

result=requests.post(url,json=data)
print(f"Status code: {result.status_code}")
print(f"Json: {result.json()}")

# Status code: 201 --> created and successful
# Json: {'userId': 11, 'title': 'Monte Kristo Kontu', 'body': 'bir intikam hikayesi', 'id': 101}