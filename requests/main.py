import requests
from requests.exceptions import HTTPError

# 取得 API 連結
api_urls = ["https://api.github.com"]

# 依序判斷 api_urls 這個 list 中的 status
for url in api_urls:
    try:
        response = requests.get(url)    # 取得連接
        response.raise_for_status()     # 取得狀態

        # response 的內容        
        content = response.content
        print(content, "\n type: ", type(content))
        # response 的內容 (text)
        response.encoding = "utf-8" # 設定編碼 UTF-8
        text_content = response.text
        print(text_content, "\n type: ",type(text_content))
        # response 的內容 (json)
        json_content = response.json()
        print(json_content, "\n type: ",type(json_content))
        # 從 response 的內容中取得 emojis_url
        response_dict = response.json()
        emojis_url = response_dict["emojis_url"]
        print(emojis_url)

        # headers
        headers = response.headers
        print(headers, "\ntype: ", headers["content-type"])

        # Query String Parameters
        # 搜尋 Python 語言的 repository，按照 stars 來排序
        response = requests.get(
                    "https://api.github.com/search/repositories",
                    params={"q": "language:python", "sort": "stars", "order": "desc"}
                    )
        # 取得 response 的內容，並印出前三個 repository 的名稱、描述、星星數、連結
        json_response = response.json()
        popular_repo = json_response["items"]
        print()
        for repo in popular_repo[:3]:
            print("Repository Name:", repo["name"])
            print("Description:", repo["description"])
            print("Stars:", repo["stargazers_count"])
            print("URL:", repo["html_url"])
            print("-" * 50)

        # Request Headers
        # 搜尋 Python 語言的 repository，只接受 text-match+json 格式的 response
        response = requests.get(
                    "https://api.github.com/search/repositories",
                    params={"q": '"real python"'},                                  # 搜尋 "real python"
                    headers={"Accept": "application/vnd.github.text-match+json"}    # 只接受 text-match+json 格式的 response
                    )
        # 取得 response 的內容，並印出第一個 repository 的 text_matches
        json_response = response.json()         # 將 response 的內容轉換成 json 格式
        first_repo = json_response["items"][0]  # 取得第一(0)個 repository
        print()
        print(first_repo["text_matches"][0]["matches"],"\n")

        # Other HTTP Methods (POST, PUT, DELETE, ...)
        # POST
        response = requests.post("https://httpbin.org/post", data={"key": "value"})
        print(response.json())
        # PUT
        response = requests.put("https://httpbin.org/put", data={"key": "value"})
        print(response.json())
        # DELETE
        response = requests.delete("https://httpbin.org/delete")
        print(response) # Delete 只會有成功或失敗的訊息
        # HEAD
        response = requests.head("https://httpbin.org/get")
        print(response.headers) # 只會有 headers
        # PATCH
        response = requests.patch("https://httpbin.org/patch", data={"key": "value"})
        print(response.json()) 
        # OPTIONS
        response = requests.options("https://httpbin.org/get")
        print(response.headers) # 只會有 headers

    except HTTPError as http_err:       # ... 可能根本沒這個頁面或是其他和網頁有關的問題
        print("HTTP error! ... ", http_err)
    except Exception as err:            # ... 可能格式根本就是錯的？
        print("Other Error! ... ", err)
    else:
        print("Success!")               # 都沒出錯 -> Success! (200)