# # <10, 2, 16 진수>
# num = 10
# num2 = 0b1010
# num16 = 0xa
# print(num, num2, num16)

# # and 단위의 값이 모두 1이어야 1 > 연산자 결합에 유용함
# a = 0b1010
# b = 0b1011
# c = a & b
# print(bin(c))

# # or 하나만 1이면 모두 1
# a = 0b1010
# b = 0b10011
# c = a | b
# print(bin(c))

# # a<<1 2진수 표기법에서 한 칸씩 앞으로 땡긴다.(*2)
# # a>>1 2진수 표기법에서 한 칸씩 뒤로 간다.(//2) 

# a = 0b1010

# print(a<<1, a<<2, a<<3)
# print(a>>1, a>>2, a>>3)
# print(1<<10)



arr = [3, 6, 7, 1, 5, 4]
N = len(arr)
subset = 10
for j in range(N):
	if subset & (1 << j):                 #2진수에서 [2]+[4]=20
		print(arr[j], end=' ')		
print()

# for subset in range(1<<N):
# 	print(subset, end = '>')
# 	for j in range(N):
# 		if subset & (1 << j):
# 			print(arr[j], end = ' ')
# 	print()

# << >> 개념 그리고 10진수를 2진수로 표현했을 때의 인덱스 값으로 문제를 풀이
