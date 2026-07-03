import requests

my_url= "https://jsonplaceholder.typicode.com/todos"

result=requests.get(my_url)
result=result.json()

print(result[0]["id"]) # 1
print(result[0]["title"]) # delectus aut autem

for item in result:
    print(f"{item["id"]}-{item["title"]}")
"""
1-delectus aut autem
2-quis ut nam facilis et officia qui
3-fugiat veniam minus
4-et porro tempora
5-laboriosam mollitia et enim quasi adipisci quia provident illum
6-qui ullam ratione quibusdam voluptatem quia omnis
7-illo expedita consequatur quia in
.
.
"""

my_another_url= "https://jsonplaceholder.typicode.com/users"

result2=requests.get(my_another_url)
result2=result2.json()

for item in result2:
    print(f"{item["id"]}-{item["name"]}-{item["address"]["city"]}")
"""
1-Leanne Graham-Gwenborough
2-Ervin Howell-Wisokyburgh
3-Clementine Bauch-McKenziehaven
4-Patricia Lebsack-South Elvis
5-Chelsey Dietrich-Roscoeview
6-Mrs. Dennis Schulist-South Christy
7-Kurtis Weissnat-Howemouth
8-Nicholas Runolfsdottir V-Aliyaview
9-Glenna Reichert-Bartholomebury
10-Clementina DuBuque-Lebsackbury
"""
