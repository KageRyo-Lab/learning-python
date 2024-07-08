from datetime import datetime
from pydantic import BaseModel, PositiveInt, ValidationError
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

    external_data = {
        'id': '123',    # 故意打錯型態
        'tastes': {}    # 缺少必要的欄位
    }

    try:
        User(**external_data)
    except ValidationError as e:
        user_logger.error(e.errors())

if __name__ == '__main__':
    main()