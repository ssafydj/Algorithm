# for <=> while 변환 가능하다.
# for => 반복횟수를 아는 경우
# while => 반복횟수를 모르는 경우

for i in range(5):
    print('Hello')          # 5번 반복되는 Hello

for i in range(5):
    print(i)
    i += 10
    print('===>', i)        # for와 range의 원리를 이해하자

while '수식':              # 1) 수식 = 반복의 종료조건 일정 조건이 성립되면 종료되는 변수로 지정(<>상수)
    print('hello')

i = 0   # 2) 수식에 사용되는 초기값 설정  
while i < 5:
    print(i)
    i += 1    # 3) 수식에 사용된 변수의 값을 변경하는 값 지정


# 중첩된 for 문에서 break -> 자기를 둘러싸고 있는 for 문에서만 빠져나감
# break = 바로 다음 항만 건너뜀
    for i in range(5):
        for j in range(5):
            for k in range(5):
                if k > j:
                    break

# for else 
for i in range(5):
    print
    if i == 5:
        break
else:
    print('else....')

#i = 4가 되는 순간 -> break에 걸리면서 else를 건너뛰고 0, 1, 2, 3 만 출력하고 끝난다.
    for i in range(5):
        print
        if i == 4:
            break
    else:
        print('else....')