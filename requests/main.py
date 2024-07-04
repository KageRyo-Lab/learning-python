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

    except HTTPError as http_err:       # ... 可能根本沒這個頁面或是其他和網頁有關的問題
        print("HTTP error! ... ", http_err)
    except Exception as err:            # ... 可能格式根本就是錯的？
        print("Other Error! ... ", err)
    else:
        print("Success!")               # 都沒出錯 -> Success! (200)