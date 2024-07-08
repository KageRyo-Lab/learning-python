from datetime import datetime
from pydantic import BaseModel, PositiveInt
import logging

# 設定 logging 的 format
def set_logging():
    logging.basicConfig(
        format="[%(asctime)s][%(name)-5s][%(levelname)-5s] %(message)s (%(filename)s:%(lineno)d)",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    user_logger = logging.getLogger('main')
    user_logger.setLevel(logging.INFO)
    return user_logger

# 定義 Pydantic 模型
class User(BaseModel):
    id: int  
    name: str = 'John Doe'  
    signup_ts: datetime | None  
    tastes: dict[str, PositiveInt]

# 主程式函式
def main():
    user_logger = set_logging()

    # 創建 User 實例並記錄日誌
    external_data = {
        'id': 123,
        'signup_ts': '2019-06-01 12:22',  
        'tastes': {
            'wine': 9,
            b'cheese': 7,  
            'cabbage': '1',  
        },
    }
    user = User(**external_data)

    user_logger.info(user.id)
    user_logger.info(user.model_dump())

# 執行主程式
if __name__ == '__main__':
    main()