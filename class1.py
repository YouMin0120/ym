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
#         id.append(esa)
#         ps.append(input("패스워드를 입력해주세요 :"))
# print(id)
# print(ps)} = id와 패스워드 입력
a=[]
for i in range(100):
    b = i % 10
    c = int(i / 10)
    if c == 3 or c == 6 or c == 9:
        a.append("*")
    elif b == 3 or b == 6 or b == 9:
        a.append("*")
    elif b % 3 == 0 and c % 3 == 0:
        a.append("**")
    else:
        a.append(i)
print(a)