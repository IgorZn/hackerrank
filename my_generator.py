def func(N):
    for elem in range(N):
        yield elem
    return

a = [elem for elem in func(10)]


print(a)