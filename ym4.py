#for j in range(2, 10):
#    for i in range(1,10):
#        b = "{} * {} = {}".format(j , i , (j*i))
#        print(b)

#class GAME():
#    def gm(self):
#        print(1)
#a = GAME()
#a.gm()
import email.parser
import random

class makeCh():

    def __init__(self):
        self.hp = random.randrange(100,150)
        self.mp = random.randrange(170, 200)

    def hit(self):
        return 15

    def heal(self):
        self.mp = self.mp - 100
        self.hp = self.hp + 70
        return 70
a = makeCh()
b = makeCh()
while True:
    print("A의 HP계수: {} A의 MP계수: {} A의 주는 피해량: {}".format(a.hp , a.mp , a.hit()))
    print("B의 HP계수: {} B의 MP계수: {} B의 주는 피해량: {}".format(b.hp , b.mp , b.hit()))
    c = input()
    if c == "hit":
        b.hp = b.hp - a.hit()
        print("플레이어가 skill.hit을 사용하였습니다 / {} 데미지를 주었습니다".format(a.hit()))
    if c == "heal":
        a.heal()
        print("플레이어가 skill.heal을 사용하였습니다 / {} 피가 회복되었습니다".format(70))
    a.hp = a.hp - b.hit()
    print("AI가 skill.hit을 사용하였습니다 / {} 데미지를 주었습니다".format(b.hit()))
    if a.hp <= 0:
        print("Player가 패배하였습니다")
        print("AI가 승리하였습니다")
        break
    if b.hp <= 0:
        print("Player가 승리하였습니다")
        print("AI가 패배하였습니다")
        break