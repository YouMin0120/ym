# import random
# l = []
# for h in range(5):
#     l.append(random.randrange(1,101))
#
# def YM():
#     for j in range(len(l)):
#         b = len(l) - j
#         for i in range(1, b):
#             if l[i-1] >= l[i]:
#                 l[i-1] , l[i] = l[i] , l[i-1]
#     print(l)
# YM()
# import random
# l = []
# for i in range(5):
#     l.append(random.randrange(1,101))
# min = l[0]
# for j in range(len(l)):
#     b = len(l) - j
#     for h in range(1, b):
#         if min > l[h]:
#             min = l[h]
# print(l)
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