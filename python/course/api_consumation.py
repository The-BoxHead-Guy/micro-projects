import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()

for user in users:
    name = user["name"]
    email = user["email"]

    print(f"Name: {name}, Email: {email}")
