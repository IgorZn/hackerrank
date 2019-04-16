flag = True
N = 10
x = 232

for i in range(N):
    flag = flag and x % 10 == 0
    print(flag)