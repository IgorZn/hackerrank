
def birthday(s, d, m):
    N = len(s)
    count = 0
    if max(s) == 1 and d > 1 and m > 1: return count
    for i in range(0, N-1):
        # print(sum(s[i:i+m]), s[i:i+m]) if sum(s[i:i+m]) == d else print('Мимо')
        if sum(s[i:i+m]) == d: count += 1
    print(count)
    return count

s = list(map(int, '2 3 4 4 2 1 2 5 3 4 4 3 4 1 3 5 4 5 3 1 1 5 4 3 5 3 5 3 4 4 2 4 5 2 3 2 5 3 4 2 4 3 3 4 3 5 2 5 1 3 1 4 2 2 4 3 3 3 3 4 1 1 4 3 1 5 2 5 1 3 5 4 3 3 1 5 3 3 3 4 5 2'.split()))
s1 = list(map(int, '1 2 1 3 2'.split()))
d, m = map(int,'3 2'.split())
birthday(s1, d, m)