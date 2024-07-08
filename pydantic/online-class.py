from pydantic import BaseModel, PositiveInt, ValidationError
from datetime import datetime
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
class OnlineClass(BaseModel):
    id: int                     # 課程編號
    name: str                   # 課程名稱
    price: PositiveInt          # 課程價格 
    starttime: datetime | None  # 開課時間
    endtime: datetime | None    # 結束時間

# 主程式函式
def main():
    class_logger = set_logging()

    data1= {
        'id': 1,
        'name': 'Python 程式設計',
        'price': 13000,
        'starttime': '2024-08-05 09:00',
        'endtime': '2024-08-09 17:00'
    }
    data2 = {
        'id': 2,
        'name': '機器學習',
        'price': 15000,
        'starttime': '2024-08-12 09:00',
        'endtime': '2024-08-19 17:00'
    }

    try:
        online_class = OnlineClass(**data1)
        class_logger.info(online_class)
    except ValidationError as e:
        class_logger.error(e.errors())

# 程式進入點
if __name__ == '__main__':
    main()