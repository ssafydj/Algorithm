import sys
sys.stdin = open("1983.txt", "r")

tc = int(input())

for i in range(1, tc + 1):
    num, student = map(int, input().split())          # 1) 변수를 2개로 받는 이유
#     print(num, student)
    for j in range(num):                              # 2) num으로 다시 for 문 돌리는 이유
        mid, fin, home = map(int, input().split())
        result0 = (mid*0.35) + (fin*0.45) + (home*0.2)
        result = round(result0, 2)
        print('{}'.format(i), mid, fin, home, '==>', result) # 3) 어떻게 stduent index에 접근해야하는지? 딕셔너리 or index

        


       
        



        


        

    


        


        