def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(len(ar)):
        print(ar[i], ar[1+i::])
        for v in ar[1+i::]:
            if sum([v+ar[i]]) % k == 0:
                print(sum([v + ar[i]]))
                count += 1
    print(count)
    return count

if __name__ == "__main__":
    arr = list(map(int, '1 3 2 6 1 2'.split()))
    arr1 = list(map(int, '5 9 10 7 4'.split()))
    n = 0
    k = 3
    divisibleSumPairs(n, k, arr)