import sys
sys.stdin = open('sample_input (2).txt', 'r')

T = int(input())
for i in range(T):
    N = int(input())
    base = int(input())
    zero_room = [0]*10
# print(zero_room) 
    for j in range(N):
        zero_room[base % 10] += 1
        base //=10
# print(zero_room) 

    counting = 0
    for l in range(len(zero_room)):
        if zero_room[l] >= counting:
            counting = zero_room[l]
            num = l

        elif zero_room[l] == counting and l >zero_room[l-1]:
            counting = counting

    print('#{} {} {}'.format(i+1, num, counting))