def gen_bin(M:int, prefix=''):
    print(M, prefix)
    if M == 0:
        print(prefix)
        return
    for digit in "0", "1":
        gen_bin(M-1, prefix+digit)


def gen_bumbers(N:int, M:int, prefix=None):
    """
    Генерирует все числа (с лидирующими незначащами нулями)
    в N-ричной системе счис. (N<=10) длины M
    :param N:
    :param M:
    :param prefix:
    :return:
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        gen_bumbers(N, M-1, prefix)
        prefix.pop()

if __name__ == "__main__":
    gen_bumbers(3, 10)
    #gen_bin(3)