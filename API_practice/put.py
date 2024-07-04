import requests

def put_api():
    api_url = "https://jsonplaceholder.typicode.com/posts/1"

    data = {
        "userId": 1,
        "id": 1,
        "title": "Hambuger",
        "body": "good"
    }

    response = requests.put(api_url, json=data)
    print(response.json())
    
    return response.json()