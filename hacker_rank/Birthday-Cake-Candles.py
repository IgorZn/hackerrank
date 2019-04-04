def birthdayCakeCandles(ar):
    max_v = []
    for _ in ar:
        max_v.append(ar.count(_))

    print(max(max_v))

ar = list(map(int, '3 2 1 3'.split()))
birthdayCakeCandles(ar)