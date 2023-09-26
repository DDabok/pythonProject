'''
파일명: Ex12-3-module3.py
'''

from converter import * # 모듈 속 모든 함수를 함수명만으로 사용가능(참조 X)

miles = kilometer_to_miles(150)
print('150km = {}miles'.format(miles))

pounds = gram_to_pounds(1000)
print('1000g = {}pounds.'.format(pounds))
