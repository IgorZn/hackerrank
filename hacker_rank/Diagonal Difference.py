def diagonalDifference(arr):
    filtered_list = [elem for elem in arr if len(elem) > 1]
    sum_list = [[], []]


    for i, elem_1 in enumerate(filtered_list):
        sum_list[0].append(elem_1[i])


    for i, elem_1 in enumerate(filtered_list):
        a = elem_1.reverse()
        sum_list[1].append(elem_1[i])

    print(sum_list)
    print(sum(sum_list[0]))
    print(sum(sum_list[1]))
    diff = sum(sum_list[0]) - sum(sum_list[1])
    return diff if abs(diff) is False else abs(diff)


my_list = [
    [1],
    [11, 2, 4,4,5],
    [4, 5, 6,6,7],
    [10, 8, -12,3,6],
    [10, 8, -12,3,6],
]

diagonalDifference(my_list)



















# ar = '1001458909 1004570889 1007019111 1003302837 1002514638 1006431461 1002575010 1007514041 1007548981 1004402249'.split()
# foo =[]
#
# for item in range(1, len(ar)+1):
#     foo.append(int(ar[item-1]))
#
# print(sum(foo))

