def staircase(n):
    for item in range(1, n+1):
        a = n - item
        print(a*' '+item*'#')


staircase(33)