a, b = map(int, input().split())


for j in range(1, 10):
    print('{} * {} = {}   {} * {} = {}'.format(a, j, a*j, b, j, b*j))
