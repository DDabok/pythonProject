'''
파일명: Ex06-5-while-homework.py

2X1 3X1 4X1
2X2 ... ...

5단 6단 7단
'''
dan = 1
while dan <= 9: #dan = 10일때 바깥쪽  while문 종료
    n = 1
    dan += 1
    while n <= 9:
        print(f'{dan}X{n}={dan*n}', end=' ')
        n += 1
    print()