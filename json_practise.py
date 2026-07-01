import json

me='{"name":"Asya","age":21,"department":"Computer Engineering","hobbies":["reading","listening music","sketching"],"nationality":"Turkish"}' # json string, not dictionary

result=json.loads(me) # now, we made it dictionary
print(type(result)) # <class 'dict'>

print(f"Name: {result["name"]}")
print(f"Age: {result["age"]}")
print(f"Department: {result["department"]}")
print(f"Nationality: {result["nationality"]}")

for item in result["hobbies"]:
    print(item,end=" ")
"""
Name: Asya
Age: 21
Department: Computer Engineering
Nationality: Turkish
reading listening music sketching 
"""
print("--------------------------------\n")
with open("data.json","r",encoding="utf-8") as f:
# dosyamızı f takma ismi ile kullanacağız
    result2=json.load(f)
    # json, dictionary'ye dönüştü
    # dosyada s takısı kalkar, sadece "load" olur
    # pythonda bir json verisi varsa loads
    print(f"Name: {result2["name"]}")
    print(f"Age: {result2["age"]}")
    print(f"City: {result2["city"]}")
    print("Hobbies:",end="")
    for item in result2["hobbies"]:
        print(item,end=" ")
"""
Name: Ahmet
Age: 26
City: Ankara
Hobbies:history pc games anime 
"""
print("--------------------------------\n")

sis={"name":"Ekin","age":20,"department":"Chemical Engineering","hobbies":["reading","listening music","playing go"],"nationality":"Turkish"} # dictionary

result3=json.dumps(sis,ensure_ascii=False,indent=4)
print(type(result3))
# <class 'str'> --> json stringi
print(result3)
"""
{
    "name": "Ekin",
    "age": 20,
    "department": "Chemical Engineering",
    "hobbies": [
        "reading",
        "listening music",
        "playing go"
    ],
    "nationality": "Turkish"
}
"""
zeyno={"isim":"Zeynep","şehir":"Denizli","yaş":21,"hobiler":["tiyatro","americano","sohbet"]}

with open("created.json","w",encoding="utf-8") as f:
    json_result=json.dump(zeyno,f,ensure_ascii=False,indent=4)