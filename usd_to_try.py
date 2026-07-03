import requests

api_key="YOUR_API_KEY"
exchange_currency=input("Enter exchange currency: ")
foreign_exchange_received=input("Enter exchange received: ")
amount=int(input("Enter the amount: "))
url=f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{exchange_currency}"

result=requests.get(url)
result=result.json()

final=amount*result["conversion_rates"][foreign_exchange_received]

print(f"{amount} {exchange_currency} = {final} {foreign_exchange_received}")