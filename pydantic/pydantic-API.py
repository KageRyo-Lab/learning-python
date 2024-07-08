from pydantic import BaseModel, ValidationError
from requests import HTTPError, RequestException
import requests
import logging

# 設定 logging 的 format
def set_logging():
    logging.basicConfig(
        format="[%(asctime)s][%(name)-5s][%(levelname)-5s] %(message)s (%(filename)s:%(lineno)d)",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    api_logger = logging.getLogger('main')
    api_logger.setLevel(logging.INFO)
    return api_logger

# 定義 Pydantic 模型
class APIResponse(BaseModel):
    userId: int
    id: int
    title: str
    body: str

# 主程式函式
def main():
    api_logger = set_logging()

    # 呼叫 API 取得資料
    api_url = 'https://jsonplaceholder.typicode.com/posts/1'
    response = requests.get(api_url)
    try: 
        api_logger.info(f'API status: {response.status_code}')
        data = response.json()

        # 創建 APIResponse 實例並記錄日誌
        try:
            api_response = APIResponse(**data)
            api_logger.info(api_response)
        except ValidationError as e:
            api_logger.error(e.errors())
    except HTTPError as http_err:
        api_logger.error(f'HTTP error occurred: {http_err}')
    except RequestException as req_err:
        api_logger.error(f'Error occurred during API request: {req_err}')
    except Exception as err:
        api_logger.error(f'Unexpected error occurred: {err}')

if __name__ == '__main__':
    main()