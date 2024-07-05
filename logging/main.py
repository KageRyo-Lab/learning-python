import logging

# 基礎 Root Logger
# 比較簡單的方式
logging.basicConfig(level=logging.INFO)
logging.info('Hi!')
# 比較完整的方式
root_logger = logging.getLogger()
root_logger.setLevel(logging.WARNING)
root_logger.warning('oh no!')

# Create a logger
main_logger = logging.getLogger('main')     # 父 Logger
sub_logger = logging.getLogger('main.sub')  # 子 Logger
sub_logger = main_logger.getChild('sub')    # 子 Logger（另一種寫法）