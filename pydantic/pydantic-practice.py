from datetime import datetime
from typing import Tuple
from pydantic import BaseModel
import logging

# 定義 Pydantic 模型
class Delivery(BaseModel):
    timestamp: datetime
    dimensions: Tuple[int, int]

# 設定日誌系統的函式
def setup_logging():
    logging.basicConfig(
        format="[%(asctime)s][%(name)-5s][%(levelname)-5s] %(message)s (%(filename)s:%(lineno)d)",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    m_logger = logging.getLogger('main')
    m_logger.setLevel(logging.INFO)
    return m_logger

# 主程式函式
def main():
    m_logger = setup_logging()
    # 創建 Delivery 實例並記錄日誌
    m = Delivery(timestamp='2020-01-01T03:04:05Z', dimensions=(10, 20))
    m_logger.info(repr(m.timestamp))
    m_logger.info(m.dimensions)

if __name__ == '__main__':
    main()