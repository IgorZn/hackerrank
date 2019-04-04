my_str = "python java c c++ javascript pascal php BABAscript"
listWords = my_str.split()

id = 0
print(len(listWords))


for i in range(1, len(listWords)):
    print('i:%s, %s ___ %s' % (i, len(listWords[id]), len(listWords[i])))
    print('%s ___ %s' % (listWords[id], listWords[i]))
    if len(listWords[id]) <= len(listWords[i]):
        id = i
        print(id)

print(listWords[id])
