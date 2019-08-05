for sample in range(10):
    n = int(input())
    num_list = list(map(int, input(.split())))
    
    for count in range(n):
        mx, mn = 0, 0
        for i in range(1, len(num_list)):
            if num_list[mx] < num_list[i]:
                mx = i
            if num_list[mn] > num_list[i]:
                mn = i

            if count == n: break
            num_list[mx] -= 1
            num_list[mn] += 1

    print('#{} {}'.format(sample+1, abs(j-k)))