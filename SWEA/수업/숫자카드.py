import sys
sys.stdin = open('4834.txt', 'r')

tc = int(input())
# print(tc)

for i in range(tc):
    n = int(input())
    card = input().split()
    card_base = card[0]
    # print(card_base)
    # print(card_base[0])

    # print(card_base)
    # print(card_base[0])


    result = {}
    for j in range(len(card_base)):
        if card_base[j] in result:
            result[card_base[j]] += 1
        else:
            result[card_base[j]] = 1
    # print(result)
    first_key = key[0]
    first_value = value[0]
    for key, value in result.items():






    # key_list = []
    # value_list = []
    # for key, value in result.items():
    #     key_list.append(key)
    #     value_list.append(value)
    # # print(key_list)
    # # print(value_list)
    #     Max_key = max(key_list)
    #     Max_value = max(value_list)
    # print(Max_key)
    # print(Max_value)



