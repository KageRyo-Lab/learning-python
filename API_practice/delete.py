import requests

def delete_api():
    api_url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.delete(api_url)
    print(response.json())
    
    return response.json()