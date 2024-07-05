import logging

logging.basicConfig(level=logging.INFO) # 設定 Root Logger 為 INFO

main_logger = logging.getLogger('main')
main_logger.setLevel(logging.WARNING)   # 設定 main Logger 為 WARNING

sub_logger = logging.getLogger('main.sub')

logging.debug('root debug')             # 由於 Root Logger 為 INFO，所以這行不會顯示
main_logger.info('main info')           # 由於 main Logger 為 WARNING，所以這行不會顯示
sub_logger.debug('sub debug')           # 由於 main Logger 為 WARNING，所以這行不會顯示
sub_logger.info('sub info')             # 由於 main Logger 為 WARNING，所以這行不會顯示
sub_logger.warning('sub warning')       # 這行會顯示