def bigges_num(arr):
    arr.sort()
    return arr[-1]

if __name__ == "__main__":
    bar = [x for x in range(10)]
    print(bigges_num(bar))

