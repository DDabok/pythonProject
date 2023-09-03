'''
파일명: Ex08-3-continue.py

continue
    while문이나 for문과 같은 반복문을 강제로 건너뛰게 한다.
'''

total = 0
# range(1~101) 1~100까지 연속된 수
for a in range(1, 101):
    if a % 3==0:
        continue
    total += a
    print(f'a: {a}, total {total}')

print(total)