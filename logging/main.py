import logging

# 基礎 Root Logger
# 比較簡單的方式
logging.basicConfig(level=logging.INFO)
logging.info('Hi!')
# 比較完整的方式
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
root_logger.info('Hi!')

