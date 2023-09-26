'''
파일명: Ex12-8-time.py

'''

import time

#1970년  1월 1일 0시 0분 0초(UTC)부터 현재까지 경과 시간을 반환(TIMESTAMP)
print(time.time())

# ctime() 함수 - 인수로 전달된 time을 시간 형식을 갖춰 반환
print(time.ctime(time.time()))

#인수로 전달된 날짜와 지시자를 이용하여 형식을 갖춘
#날짜 데이터를 문자열로 반환

print(time.strftime('%Y-%m-%d %p %H:%M:%S'))

print(time.strftime('%Y년 %m월 %d일 %p %H:%M:%S'))

# 만약 인코딩 문제 발생시 아래와 같이 사용하면 된다.
print(time.strftime(
    '%Y년 %m월 %d일 %p %H:%M:%S'
    .encode('unicode-escape')
    .decode()
).encode().decode('unicode-escape'))

#encode 문자열을 숫자로 바꾸는것
#decode byte코드를 문자로 바꾸는 것

# 인자 초만큼 시스템 일시중지
time.sleep(1)

sec = 1
while True:
    print(sec)
    if sec == 10:
        break

    time.sleep(1)
    sec += 1