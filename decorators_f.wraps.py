from functools import wraps


# Example without WRAPS from FUNCTOOL
def dec(func):
    "Dec func"
    print("Inside Dec 1 func aka decorator")
    return func

def dec_2(func):
    "Dec 2 func"
    print("Inside Dec 2 func aka decorator")
    return func


# foo: was called
# 4
# my_wrap
# None

# #   Example WITH WRAPS from FUNCTOOL
# def dec(func):
#     @wraps(func)
#     def my_wrap(*args, **kwargs):
#         print(func.__name__ + ": was called")
#         return func(*args, **kwargs)
#     return my_wrap

# foo: was called
# 4
# foo
# does some math


@dec
@dec_2
def foo(x):
    """does some math"""
    return x+x

print(foo(2))
print(foo.__name__)
print(foo.__doc__)