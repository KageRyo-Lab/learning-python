from dataclasses import dataclass
import logging

# 設定 logging 的 format
logging.basicConfig(
    format="[%(asctime)s][%(name)-5s][%(levelname)-5s] %(message)s (%(filename)s:%(lineno)d)",
    datefmt="%Y-%m-%d %H:%M:%S",
)
member_logger = logging.getLogger('member')
member_logger.setLevel(logging.INFO)

@dataclass
class Member:
    name: str
    phone: str
    email: str

member1 = Member('abbc','0900123456','abbc@gmail.com')
member2 = Member('people','0912345678','peo@yahoo.com.tw')
member_logger.info(member1)
member_logger.info(member2)