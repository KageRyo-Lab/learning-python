import requests
import json

def get_api():
    api_url = 'https://jsonplaceholder.typicode.com/posts/1'

    response = requests.get(api_url)
    output_response = json.dumps(response.json(), indent=4)
    print(output_response)
    
    return response.json()