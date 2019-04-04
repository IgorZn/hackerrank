def add_two(n):
    x = 2

    def add_some():
        print("x =", x)
        print("x + N =", n+x)
        return n + x

    return add_some()


add_two(2)