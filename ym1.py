import random
def map():
    print(a[1], a[2], a[3])
    print(a[4], a[5], a[6])
    print(a[7], a[8], a[9])
def player():
    while True:
        ip = int(input())
        if a[ip] == 0:
            a[ip] = "V"
            break
def draw():
    g = 0
    for j in range(1, 10):
        if a[j] != 0:
            g = g + 1
    if g == 9:
        print("무승부")
        return 1
def AI():
    while True:
        rd = random.randrange(1, 10)
        if a[rd] == 0:
            a[rd] = "X"
            break
def check():
    if (a[1] == "V" and a[2] == "V" and a[3] == "V") or (a[4] == "V" and a[5] == "V" and a[6] == "V") or (a[7] == "V" and a[8] == "V" and a[9] == "V"):
        print("승리했습니다")
        return 1
    elif (a[1] == "V" and a[4] == "V" and a[7] == "V") or (a[2] == "V" and a[5] == "V" and a[8] == "V") or (a[3] == "V" and a[6] == "V" and a[9] == "V"):
        print("승리했습니다")
        return 1
    elif (a[1] == "V" and a[5] == "V" and a[9] == "V") or (a[3] == "V" and a[5] == "V" and a[7] == "V"):
        print("승리했습니다")
        return 1
    elif (a[1] == "X" and a[2] == "X" and a[3] == "X") or (a[4] == "X" and a[5] == "X" and a[6] == "X") or (a[7] == "X" and a[8] == "X" and a[9] == "X"):
        print("패배했습니다")
        return 1
    elif (a[1] == "X" and a[4] == "X" and a[7] == "X") or (a[2] == "X" and a[5] == "X" and a[8] == "X") or (a[3] == "X" and a[6] == "X" and a[9] == "X"):
        print("패배했습니다")
        return 1
    elif (a[1] == "X" and a[5] == "X" and a[9] == "X") or (a[3] == "X" and a[5] == "X" and a[7] == "X"):
        print("패배했습니다")
        return 1
a=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
map()
for i in range(10):
    player()
    if check() == 1:
        break
    if draw() == 1:
        break
    AI()
    if check() == 1:
        break
    map()