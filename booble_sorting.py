from random import randint

def sort_bubble(N):
    a = [randint(1, 99) for x in range(N)]
    N = len(a)
    print(a, '<- unsorted')

    for i in range(N - 1):
        for j in range(N - i - 1):
            # print(a, 'i:', i, ' a[j]=', a[j],'inx j=', j, ', a[j + 1]:', a[j + 1], ' j + 1:', j + 1, 'N - i - 1:', N - i - 1)
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    print(a, '<- sorted')
    return a

print(*sort_bubble(10)[-2:])

