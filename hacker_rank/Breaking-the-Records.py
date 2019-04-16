a = list(map(int, '3 4 21 36 10 28 35 5 24 42'.split()))
a2 = list(map(int, '10 5 20 20 4 5 2 25 1'.split()))

def breakingRecords(a):
    N = len(a)
    print(N)
    min_score = []
    max_score = []
    min_score.append(a[0])
    max_score.append(a[0])

    for i in range(1, N):
        index = len(max_score)-1 if len(max_score) < i else i-1
        print(a[i], i, i-1, index, len(max_score))
        if a[i] < min_score[len(min_score)-1]:
            min_score.append(a[i])
            continue

        if a[i] > max_score[index]:
            if a[i] in min_score: continue
            if a[i] == max_score[index]: continue
            max_score.append(a[i])

    min_s = len(min_score[1:])
    max_s = len(list(set(max_score[1:])))

    print(min_score)
    print(list(set(max_score[1:])))
    print([max_s, min_s])
    return (max_s, min_s)

if __name__ == "__main__":
    breakingRecords(a2)