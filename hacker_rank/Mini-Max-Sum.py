def miniMaxSum(arr):
    temp_arr = []
    for item in range(len(arr)):
        if item == 0:
            print(item, arr[:item-1], sum(map(int, arr[:item-1])))
            temp_arr.append(sum(map(int, arr[:item-1])))
            continue
        if item == 1:
            print(item, arr[item:], sum(map(int, arr[item:])))
            temp_arr.append(sum(map(int, arr[item:])))
        else:
            print(item, arr[:item-1]+arr[item:], sum(map(int, arr[:item-1]+arr[item:])))
            temp_arr.append(sum(map(int, arr[:item-1]+arr[item:])))

    print(min(temp_arr), max(temp_arr))




arr = list(map(int, '1 2 3 4 5'.split()))

miniMaxSum(arr)