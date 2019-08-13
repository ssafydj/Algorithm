import sys
sys.stdin = open("1983.txt", "r")

tc = int(input())

for i in range(1, tc + 1):
    num, student = map(int, input().split())
    # print(num, student)
    for j in range(num):
        mid, fin, home = map(int, input().split())
        result0 = (mid*0.35) + (fin*0.45) + (home*0.2)
        result = round(result0, 2)
        # print('{}'.format(i), mid, fin, home, '==>', result)

        


       
        



        


        

    


        


        