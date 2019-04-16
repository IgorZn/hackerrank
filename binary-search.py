from random import random
N = 100
array = []
for i in range(N):
    array.append(int(random()*100))
array.sort()
print(array)
print(len(array))

number = 78

low = 0
high = N-1
while low <= high:
    print(low, high)
    mid = (low + high) // 2
    print('mid: '+str(mid))
    if number < array[mid]:
        high = mid - 1
        print('high: ' + str(high))
    elif number > array[mid]:
        low = mid + 1
        print('low: ' + str(low))
    else:
        print("ID in arr =", mid, array[mid])
        break
else:
    print("No the number")