# 07/29 교재 연습문제 1 (p.16)

# 문제 접근법 1) 모든 상자의 낙폭을 구할 필요가 없다. A 만 확인하면 된다.

     # 2) A 밑에 깔리는 상자의 개수를 알면 바닥과의 거리를 통해 낙폭을 알 수 있다.

​           # 3) 가로를 for 문 돌려 길이를 파악해서 A 의 높이와 같은 높이를 비교해서 알 수 있음. 

data = [7, 4, 2, 0, 0, 6, 0, 7, 0]
box = []
def height(data):
    for i in range(0, 100):
        if data[0] == data[i]:
           result = box.appned(1)
        print(result)

# 교재 연습문제 Baby-gin game (p.20)
# 문제 접근법: (6C3 * 3C3) / 2*1 으로 경우의수를 구하고 나열 확인(완전검색)


# 일의 자리 숫자를 지워 나가는 방법
num = 123456

arr = []

arr.append(num % 10) # 6제거
num // = 10    

# 반복
arr.append(num % 10) # 5제거
num // = 10  

# 반복...

# 반복문으로 한번에 표현
while num >0:
        arr.append(num % 10)
        num // = 10
