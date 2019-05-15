def my_len(arr):
    if len(arr) == 1:
        return 1
    arr.pop()
    return 1 + my_len(arr)

bar = [x for x in range(10)]


if __name__ == "__main__":
    print(my_len(bar))
