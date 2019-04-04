import math
def plusMinus(arr):
    len_arr = len(arr)
    positive = 0
    negative = 0
    zero = 0
    for item in arr:
        if item > 0: positive += 1
        if item < 0: negative += 1
        if item == 0: zero += 1

    results = [positive/len_arr, negative/len_arr, zero/len_arr]
    return_res = ['{:.6f}'.format(round(num, 6)) for num in results]
    return print("\n".join(map(str, return_res)))

arr = list(map(int, '-4 3 -9 0 4 1'.split()))
plusMinus(arr)