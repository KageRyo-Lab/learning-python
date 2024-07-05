from dataclasses import dataclass, field
import datetime
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
    record_time: datetime.datetime = field(init=False, default_factory=datetime.datetime.now)
    def __post_init__(self):
        self.information = f'{self.name} {self.phone} {self.email}'

member1 = Member('steve','0900123456','uwu@gmail.com')
member2 = Member('people','0912345678','people@yahoo.com.tw')
member_logger.info(member1)
member_logger.info(member1.information)
member_logger.info(member2)
member_logger.info(member2.information)