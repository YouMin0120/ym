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
# heal을 쓰려할때 소모갑이 100이니깐 heal을 명령했을때 소모값이 100이기에 소모값과 a.mp 보다 크면 사용할수 없다
# import random
#
# class makeCh():
#
#     def __init__(self):
#         self.hp = random.randrange(400,500)
#         self.mp = random.randrange(170, 200)
#
#     def hit(self):
#         return 15
#
#     def heal(self):
#         self.mp = self.mp - 100
#         self.hp = self.hp + 70
#         return 70
#
#     def Ice_hit(self):
#         self.mp = self.mp - 170
#         return random.randrange(150,200)
# a = makeCh()
# b = makeCh()
# while True:
#     flag = 0
#     print("A의 HP계수: {} A의 MP계수: {} A의 주는 피해량: {}".format(a.hp , a.mp , a.hit()))
#     print("B의 HP계수: {} B의 MP계수: {} B의 주는 피해량: {}".format(b.hp , b.mp , b.hit()))
#     c = input()
#     if a.mp <= 100 and c == "heal":
#         print("플레이어의 mp가 부족하여 스킬을 사용할수 없습니다")
#         flag = 1
#     elif c == "heal":
#         a.heal()
#         print("플레이어가 skill.heal을 사용하였습니다 / {} 피가 회복되었습니다".format(70))
#     if a.mp <= 170 and c == "Ice_hit":
#         print("플레이어의 mp가 부족하여 스킬을 사용할수 없습니다")
#         flag = 1
#     elif c == "Ice_hit":
#         f = a.Ice_hit()
#         b.hp = b.hp - f
#         print("플레이어가 skill.Ice_hit을 사용하였습니다 / {} 데미지를 주었습니다".format(f))
#     if flag == 1:
#         print("플레이어의 mp가 부족해 AI의 턴이 스킵되었습니다")
#     if flag == 0:
#         g = random.randrange(3)
#     if g == 0:
#         a.hp = a.hp - b.hit()
#         print("AI가 skill.hit을 사용하였습니다 / {} 데미지를 주었습니다".format(b.hit()))
#     if b.mp <= 170 and g == 1:
#         a.hp = a.hp - b.hit()
#         print("Ai의 mp가 부족하여 스킬을 사용할수 없어 자동으로 일반공격으로 전환되었습니다")
#         print("AI가 skill.hit을 사용하였습니다 / {} 데미지를 주었습니다".format(b.hit()))
#     elif g == 1:
#         n = b.Ice_hit()
#         print("Ai가 skill.Ice_hit을 사용하였습니다 / {} 데미지를 주었습니다".format(n))
#     if b.mp <= 100 and g == 2:
#         a.hp = a.hp - b.hit()
#         print("Ai의 mp가 부족하여 스킬을 사용할수 없어 자동으로 일반공격으로 전환되었습니다")
#         print("AI가 skill.hit을 사용하였습니다 / {} 데미지를 주었습니다".format(b.hit()))
#     elif g == 2:
#         b.heal()
#         print("AI가 skill.heal을 사용하였습니다 / {} 피가 회복되었습니다".format(70))
#     if c == "hit":
#         b.hp = b.hp - a.hit()
#         print("플레이어가 skill.hit을 사용하였습니다 / {} 데미지를 주었습니다".format(a.hit()))
#     if a.hp <= 0:
#         print("Player가 패배하였습니다")
#         print("AI가 승리하였습니다")
#         break
#     if b.hp <= 0:
#         print("Player가 승리하였습니다")
#         print("AI가 패배하였습니다")
#         break