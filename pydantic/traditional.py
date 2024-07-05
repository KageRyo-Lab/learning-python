import logging

# 設定 logging 的 format
logging.basicConfig(
    format="[%(asctime)s][%(name)-5s][%(levelname)-5s] %(message)s (%(filename)s:%(lineno)d)",
    datefmt="%Y-%m-%d %H:%M:%S",
)
member_logger = logging.getLogger('member')
member_logger.setLevel(logging.INFO)

# 不用 dataclass 
class Member:
    def __init__(self, name, phoneNum, email):
        self.name = name 
        self.phone = phoneNum
        self.email = email

    def __str__(self):
        return f'{self.name} {self.phone} {self.email}'

member1 = Member('abbc','0900123456','abbc@gmail.com')
member_logger.info(member1)