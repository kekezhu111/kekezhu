lists_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lists_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lists_3 = []


for i in range(len(lists_1) - 1):

    lst_1 = lists_1.pop(0)
    lists_3.append(lst_1)

    lst_2 = lists_2.pop(0)
    lists_3.append(lst_2)

print(lists_3)
