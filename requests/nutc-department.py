import requests
from bs4 import BeautifulSoup as bs

# 要爬取的網址
url = 'https://www.nutc.edu.tw/p/404-1000-108697.php'

try:
    # 發送 GET 請求取得網頁內容，並忽略 SSL 驗證問題
    response = requests.get(url, verify=False)
    response.raise_for_status()  # 如果請求失敗，會拋出異常
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

# 將網頁內容轉換成 BeautifulSoup 物件
html_content = response.text
soup = bs(html_content, 'html.parser')

try:
    # 尋找 id 為 'Dyn_2_3' 的區塊
    webcontainer = soup.find('div', id='Dyn_2_3')
    if not webcontainer:
        raise ValueError("找不到 id 為 'Dyn_2_3' 的區塊。")
    
    # 尋找所有學院
    colleges = webcontainer.find_all('div', class_='col-md-4')
    for college in colleges:
        col_name = college.find('h2').get_text(strip=True)
        print(f"學院: {col_name}")
        
        # 尋找學院底下的系所
        departments = college.find_all('li', class_='con_li')
        for dpt in departments:
            dpt_name = dpt.get_text(strip=True)
            print(f"{dpt_name}")
        print()

except (AttributeError, ValueError) as e:
    print(f"Error... {e}")