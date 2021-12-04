import random
def YM():
    l = []
    for j in range(5):
        l.append(random.randrange(1, 101))
        for k in range(len(l)):
            min = k
            for i in range(k, len(l)):
                if l[min] > l[i]:
                    min = i
            l[k], l[min] = l[min], l[k]
    print(l)
YM()
