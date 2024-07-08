from datetime import datetime
from typing import Tuple        # 用來標示 dimensions 的型別所需的函式

from pydantic import BaseModel
import logging

logging.basicConfig(
    format="[%(asctime)s][%(name)-5s][%(levelname)-5s] %(message)s (%(filename)s:%(lineno)d)",
    datefmt="%Y-%m-%d %H:%M:%S",
)
m_logger = logging.getLogger('main')
m_logger.setLevel(logging.INFO)

# Define a Pydantic model
class Delivery(BaseModel):
    timestamp: datetime         # 設定 timestamp（時間戳）為 datetime
    dimensions: Tuple[int, int] # 設定 dimensions（尺寸）為 Tuple[int, int]

# 設定 m 變數是 Delivery 類別的一個實例，並且傳入 timestamp 和 dimensions
m = Delivery(timestamp='2020-01-01T03:04:05Z', dimensions=(10, 20))

m_logger.info(repr(m.timestamp))    # 顯示 timestamp，這裡用repr()是為了顯示更多資訊，如果沒有repr()，只會顯示時間字串
m_logger.info(m.dimensions)