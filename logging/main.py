import logging

# 設定 logging 的 format
logging.basicConfig(
    format="[%(asctime)s][%(name)-5s][%(levelname)-5s] %(message)s (%(filename)s:%(lineno)d)",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# 基礎 Root Logger
# 比較簡單的方式
logging.basicConfig(level=logging.INFO)     # 設定 Root Logger 為 INFO
logging.info('Hi!')
# 比較完整的方式
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)       # 設定 Root Logger 為 INFO
root_logger.warning('oh no!')

# Create a logger
main_logger = logging.getLogger('main')     # 父 Logger
sub_logger = logging.getLogger('main.sub')  # 子 Logger
sub_logger = main_logger.getChild('sub')    # 子 Logger（另一種寫法）

# Create a handler
# 方法一：透過 FileHandler
file_handler = logging.FileHandler('log.txt')   # 建立 FileHandler
# 方法二：透過 StreamHandler
file_handler = logging.StreamHandler(open('log.txt', 'a'))  # 建立 StreamHandler
# 將 file_handler 加入 main_logger
main_logger.addHandler(file_handler)

# log messages
main_logger.info('main info')   # 由於剛剛建立的 FileHandler，所以這行會被寫入 log.txt
sub_logger.debug('sub debug')   # 由於 main Logger 為 INFO，所以這行不會顯示和寫入 log.txt