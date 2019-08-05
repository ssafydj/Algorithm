arr= [
[4 ,4 ,3 ,2 ,1],
[2 ,2 ,1 ,6 ,5],
[3 ,5 ,4 ,6 ,7],
[4 ,2 ,5 ,9 ,7],
[8 ,1 ,9 ,5 ,6]
]


print(sum(arr[0])





idx = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        idx += 1
        print(arr[i][j], end=' ')
        if idx == len(arr[0]):
            idx = 0
            print()

print('-----------------------------')

for j in range(len(arr)):
    for i in range(len(arr[j])):
        idx += 1
        print(arr[i][j], end=' ')
        if idx == len(arr[0]):
            idx = 0
            print()



arr= [
[4 ,4 ,3 ,2 ,1],
[2 ,2 ,1 ,6 ,5],
[3 ,5 ,4 ,6 ,7],
[4 ,2 ,5 ,9 ,7],
[8 ,1 ,9 ,5 ,6]
]

for i in range(0, len(arr[5]):
    print(sum(arr[i]))