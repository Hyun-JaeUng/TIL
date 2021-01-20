# 파이썬 경로 추가
import sys
sys.path.append("C:/PyStudy")
print(sys.path)

# 하위 폴더가 있음으로 add, table.py를 import시 아래와 같이 해야함
import mypack.calc.add
mypack.calc.add.outadd(1,2)
# 패키지.패키지.모듈.모듈내함수(아규먼트)

import mypack.report.table
mypack.report.table.outreport()

# 파이썬에서는 하위 폴더를 패키지로 간주하여 위와 같이 쓴 것.
# 패키지 구분자는 점(.)이다.