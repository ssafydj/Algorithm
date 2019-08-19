import sys
sys.stdin = open("2056.txt", "r")

tc = int(input())
for k in range(1, tc + 1):
    n = list(map(int, input().split()))
    print(n)
    
calendar = { 
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31,6: 30, 
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31 
} 
for month, day in calendar.items():
    

