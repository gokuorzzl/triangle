import sys


n = input('삼각형 층수? (1층 이상 가능)')
n = int(n)
if 1 <= n:
    a = n
    b = 1
    for n in range(n, 0, -1):
        print(' '*n,'*'*b,' '*n)
        b= b+2