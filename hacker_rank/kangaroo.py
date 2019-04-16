import math
import os
import random
import re
import sys


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if (v1 > v2 and not ((x2-x1)%(v1-v2))):
        print("YES")
        return 'YES'
    else:
        print("NO")
        return 'NO'
    # f1 = lambda x, y: x in y
    # arr1 = [x for x in range(10000) if x % (x1+v1) == 0]
    # arr2 = [x for x in range(10000) if x % (x2+v2) == 0]
    # print(arr1,'\n',arr2)
    # longest = 'arr1' if len(arr1) > len(arr2) else 'arr2'
    # longest_arr = arr1 if len(arr1) > len(arr2) else arr2
    # smallest = arr2 if longest == 'arr1' else arr1
    # for i in range(1, len(arr1 if len(arr1) > len(arr2) else len(arr2))):
    #     if i == len(smallest):
    #         break
    #     print(i, smallest[i], f1(smallest[i], arr1 if longest == 'arr1' else arr2))
    #     state = f1(smallest[i], arr1 if longest == 'arr1' else arr2)
    #     if state is True: return 'YES'
    # return 'NO'




vals = list(map(int, '0 2 5 3'.split()))
vals1 = list(map(int, '0 3 4 2'.split()))
vals3 = list(map(int, '21 6 47 3'.split()))
x1, v1, x2, v2 = vals3.append()
kangaroo(x1, v1, x2, v2)