n = input('삼각형 층수? (1층 이상 가능)')
n = int(n)
if 1 <= n:
    b = 1
    for n in range(n, 0, -1):
        print(' '*(n-1), '*'*b, sep='')
        b += 2
