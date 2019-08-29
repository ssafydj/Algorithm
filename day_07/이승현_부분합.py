# def backtrack(a, k, input):
# #     global MAXCANDIDATES
# #     c = [0] * MAXCANDIDATES
# #
# #     if k == input:
# #         process_solution(a, k) # 답이면 원하는 작업을 한다
# #     else:
# #         k += 1
# #         ncandidates = construct_candidates(a, k, input, c)
# #         for i in range(ncandidates):
# #             a[k] = c[i]
# #             backtrack(a, k, input)
# #
# # def construct_candidates(a, k, input, c):
# #     c[0] = True
# #     c[1] = False
# #     return 2
# #
# #
# # def process_solution(a, k):
# #     # print("(", end="")
# #     i_list = []
# #     sum = 0
# #     for i in range(k+1):
# #         if a[i] == True:
# #             i_list.append(i)
# #             sum += i
# #
# #     if sum == 10:
# #         print(i_list)
# #     # print(")", end="")
# #
# # MAXCANDIDATES = 100
# # NMAX = 100
# # a = [0] * NMAX
# # backtrack(a, 0, 10)

###################################

def qsort(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        qsort(a, low, pivot-1)
        qsort(a, pivot+1, high)

def partition(a, pivot, high):
    i = pivot + 1
    j = high

    while True:
        while i < high and a[i] < a[pivot]:
            i += 1
        while j > pivot and a[j] > a[pivot]:
            j -= 1
        if j <= i:
            break
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    a[pivot], a[j] = a[j], a[pivot]
    return j