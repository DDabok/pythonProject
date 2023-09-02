'''
파일명: Ex06-4-while4.py
'''
dan = 1
while dan <= 9: #dan = 10일때 바깥쪽  while문 종료
    n = 1
    dan += 1
    while n <= 9:
        print(f'{dan}X{n}={dan*n}', end=' ')
        n += 1
    print()