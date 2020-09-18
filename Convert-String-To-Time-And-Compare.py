import re
from datetime import datetime
from datetime import timedelta

a = "2020-07-24T10:59:00-06:00"
productTime = datetime.fromisoformat(a)

nowTime = datetime.now().astimezone().replace(microsecond=0)

print(productTime)
print(nowTime)

if productTime > nowTime:
	print("yey")
