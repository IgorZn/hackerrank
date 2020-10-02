import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n: int, ar: list):
    pairs = 0
    for i in list(set(ar)):
        if int(ar.count(i)/2) != 0:
            pairs += int(ar.count(i) / 2)
    return pairs


if __name__ == '__main__':
    n = random.randint(0, 20)
    ar = [random.randint(0, 10) for i in range(n)]

    result = sockMerchant(n, ar)
    print(n, ar)
    print(result)


