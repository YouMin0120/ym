#a=int(input())
#   while a<11:
#       print("*"*a)
#           a=a+1
# for i in range():
# a=1
#  while a<11:
#      print("*"*(10-a))
#      a=a+1
# for i in range(11):
#     # print("*"*(10-i))
#a=[숫자와 문자를 여러가지 넣을수 있음]
#a.append(대괄호에 들어가는 문자 또는 숫자를 추가할수 있음)
# a=int(input())
# if a % 15 == 0:
#     print("**")
# elif a%5==0 or a%3==0:
#     print("*")
# a=[1,2,3,4]
#x=[]
#x[]
#x.append()
#
# import random
# x = []
# for i in range(1,102):
#     a=random.randrange(1,6)
#     x.append(a)
# print(x)
# b=0
# c=0
# d=0
# e=0
# f=0
# for i in range(1,101):
#     x[i]
#     if x[i]==1:
#         b=b+1
#     elif x[i]==2:
#         c=c+1
#     elif x[i] == 3:
#         d=d+1
#     elif x[i] == 4:
#         e=e+1
#     elif x[i] == 5:
#         f=f+1
# print(b,c,d,e,f)
# len(길이를 구하는 함수)
# {id=[]
# ps=[]
# for i in range(1,6):
#     flag=0
#     esa=input("ID를 입력해주세요 :")
#     for check in range(len(id)):
#         if id[check]==esa:
#             flag=1
#     if flag==1:
#         print("중복")
#     else:
# #         id.append(esa)
#         ps.append(input("패스워드를 입력해주세요 :"))
# print(id)
# print(ps)} = id와 패스워드 입력
# a=[]
# for i in range(1,101):
#     b = int(i % 10) # 1의 자리수
#     c = int(i / 10) # 10의 자리수
#     if (c != 0 and c % 3 == 0) and (b != 0 and b % 3 == 0):
#         a.append("**")
#     elif (c != 0 and c % 3 == 0) or (b != 0 and b % 3 == 0):
#         a.append("*")
#     else:
#         a.append(i)
# print(a)
# 21/10 = 소수를 포함함 / 21//10 = 소수를 버림
# a=1
# d=[]
# while a<101:
#     b = int(a % 10) # 1의 자리수
#     c = int(a / 10) # 10의 자리수
#     if (c != 0 and c % 3 == 0) and (b != 0 and b % 3 == 0):
#         d.append("**")
#     elif (c != 0 and c % 3 == 0) or (b != 0 and b % 3 == 0):
#         d.append("*")
#     else:
#         d.append(a)
#     a = a + 1
# print(d)
# random.randrange 를 실행시키기 위해서 사용하는 함수 = import 이 import 는 코드의 처음에 넣어야한다
# import random
# a=[]
# x=0
# i=0
# while i < 100:
#     a.append(random.randrange(1,101))
#     i=i+1
# for ck in range(100):
#     if a[ck] > x:
#         x=a[ck]
# print(a)
# print(x)
# import random
# a=[]
# x=101
# i=0
# while i < 100:
#     a.append(random.randrange(1,101))
#     i=i+1
# for ck in range(100):
#     if a[ck] < x:
#         x=a[ck]
# print(x)
# print(a)
# 함수를 def + 함수이름(): 으로 만들수 있다.
# 함수 return 을 사용하기 위해선 def test(): 에서 생성된 함수 값을 a=() 와 같은 함수로 지정해서 사용해야한다.
# import random
# def YM():
#     return input()
# def COM():
#     return b[random.randrange(3)]
# def GAME():
#     if (x == "가위" and c == "가위") or (x == "바위" and c == "바위") or (x == "보" and c == "보"):
#         print("비겼습니다")
#     elif (x == "가위" and c == "바위") or (x == "바위" and c == "보") or (x == "보" and c == "가위"):
#         print("패배하였습니다")
#     elif (x == "바위" and c == "가위") or (x == "보" and c == "바위") or (x == "가위" and c == "보"):
#         print("승리하였습니다")
# x=YM()
# b=["가위" , "바위" , "보"]
# c=COM()
# print(c)
# GAME()
