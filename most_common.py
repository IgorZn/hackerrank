from random import random

a = [int(random()*5) for i in range(15)]
print(a)

a_set = set(a)

most_common = None
qty_most_common = 0
vals = []
count = []


for item in a_set:
    qty = a.count(item)
    if qty > qty_most_common:
        vals.append(item)
        count.append(qty)
        qty_most_common = qty
        most_common = item
foo = list(zip(vals, count))
print(most_common)
print(foo)