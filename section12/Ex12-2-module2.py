'''
파일명: Ex12-2-module2.py

모듈 사용법
from 모듈명 import 함수
from 모듈명 import 함수1, 함수2
from 모듈명 import *


'''

from converter import kilometer_to_miles # 모듈 속 함수를 함수명만으로 사용가능(참조 X)

miles = kilometer_to_miles(150)
print(f'150km = {miles}miles')