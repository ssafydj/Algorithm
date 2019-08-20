n, m = map(int, input().split())

if n > m:
    for i in range(1, 10):
        for j in range(n, m-1, -1):
            print('{} * {:2} = {:2}'.format(j, i, i*j), end='   ')
        print()
