import requests

url="https://jsonplaceholder.typicode.com/posts"

payload={
    "userId":4,
    "id":36
}

result=requests.get(url,params=payload)
result=result.json()

print(result)

"""
[{'userId': 4, 'id': 36, 'title': 'fuga nam accusamus voluptas reiciendis itaque', 'body': 'ad mollitia et omnis minus architecto odit\nvoluptas doloremque maxime aut non ipsa qui alias veniam\nblanditiis culpa aut quia nihil cumque facere et occaecati\nqui aspernatur quia eaque ut aperiam inventore'}]
"""