my_dict = {"a": 1, "b": 2, "c": 3}

try:
    value = my_dict["a"]
except KeyError:
    print("A KeyError occurred!")
else:
    print("No error occurred!")
finally:
    print("This part is a final and always run, no matter what was in previous.")