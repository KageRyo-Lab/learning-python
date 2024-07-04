import requests

api_url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "userId": 1,
    "title": "Today Weather",
    "body": "HOOOOOOOOOOOT!"
}

response = requests.post(api_url, json=data)
print(response.json())