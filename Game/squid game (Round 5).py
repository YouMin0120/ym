import random
hp = 3
a=[0, 0, 0, 0, 0, 0, 0, 0, 0]
b=[0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(9):
    g = random.randrange(1, 3)
    player = input()
    if player == "a" or player == "b":
        if g == 1:
            a[i] = "진짜"
        else:
            a[i] = "가짜"
    if a[i] == "진짜":
        b[i] = "가짜"
    elif a[i] == "가짜":
        b[i] = "진짜"
    if player == "a" and a[i] == "가짜":
        print("생명이 하나 감소하였습니다")
        hp = hp - 1
    elif player == "b" and b[i] == "가짜":
        print("생명이 하나 감소하였습니다")
        hp = hp - 1
    print(a)
    print(b)
    print(hp)
    if hp == 0:
        print("게임에 패배하였습니다")
        break
    if i == 8  and hp != 0:
        print("게임에 승리하였습니다")
        break
