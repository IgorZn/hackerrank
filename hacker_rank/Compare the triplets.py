
a = [3, 6, 10]
b = [5, 6, 7]


alice_score = []
bob_score = []

def compareTriplets(a, b):
    c = list(zip(a, b))
    for a, b in c:
        if a > b:
            alice_score.append(1)
        if a < b:
            bob_score.append(1)
    return " ".join(map(str, alice_score+bob_score))

print(compareTriplets(a, b))


# def compareTriplets(a, b):
#     alice_score = []
#     bob_score = []
#     for a1 in a:
#         print(".."+a1.__str__())
#         for b1 in b:
#             print("...."+b1.__str__())
#             if a1 > b1:
#                 alice_score.append(1)
#             if a1 < b1:
#                 bob_score.append(1)
#
#
#     return sum(alice_score), sum(bob_score)
#
#
# print(compareTriplets(a, b))
