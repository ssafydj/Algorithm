import sys
sys.stdin = open("1970.txt", "r")

tc = int(input())

for k in range(1, tc + 1):                  
    n = int(input())            
 

    # 입력된 값 n은 위에서 아래로 순차적으로 작동한다.
    # 몫과 나머지 기본원리만으로 풀이.
    # for 와 if는 꼭 필요한 경우에만 사용하자.
    
    a = n // 50000
    n = n % 50000

    b = n // 10000
    n = n % 10000

    c = n // 5000
    n = n % 5000

    d = n // 1000
    n = n % 1000

    e = n // 500
    n = n % 500

    f = n // 100
    n = n % 100

    g = n // 50
    n = n % 50

    h = n // 10
    n = n % 10

    print("#{}". format(k)) 
    print("{} {} {} {} {} {} {} {}".format(a, b, c, d, e, f, g, h))
  


    

    





