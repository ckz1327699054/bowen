
# print("你好，中国")
# print("你好，世界")
# print("你好，博文")
# print(2 + 3)
# print(10/3)
# print(3**2)
# print(10%3)
# print(14 // 3)

# '''
# a = 5
# b = 4
# c = a + b
# print(c)
# '''

# qq_number = 123456
# qq_password = 654321
# print(qq_password)

# jiage =8.5
# zhongliang = 7.5
# jinge = jiage * zhongliang
# jinge= jinge-5
# print(jinge)

# a = int(input("请输入单价:"))
# b = int(input("请输入重量:"))
# c = a * b
# print("苹果的单价:%.d,苹果的重量:%.d,花费金额:%.d"%(a,b,c))

# name = "小明"
# age = 18
# sex = True
# hight = 1.75
# weight =75.0

# a = 10
# b = True
# c = 8.8
# d = "zhangsan"
#
# print(a*b)

# name =  "小明"
# print("我的名字叫%s，请多多关照!" %name)
#
# student_no = 1
# print("我的学号是 %06d" %student_no)

# name = "小明"
# print("我的名字叫%s,请多多关照!"%name)




# price = 9
# weight = 5
# money = price*weight
# print("苹果的价格:%.2f 元/斤,购买了:%.2f/斤,需要支付:%.2f元" %(price,weight,money))

# age = int(input("请输入你的年龄: "))
# if age>=18:
#     print("可以进网吧嗨皮")
# else:
#     print("回家玩吧")
# age = int(input("请输入你的年龄: "))
# if age>0 and age<120:
#     print("你好")



# python_score = 70
# c_score = 50
# if python_score >60 or c_score>60:
#     print("合格")



# holiday_name = (input("输入你的节日"))
# # if holiday_name == "情人节":
# #     print("买玫瑰/看电影")
# # elif holiday_name =="平安夜":
# #     print("买苹果/吃大餐")
# # elif holiday_name =="生日":
# #     print("买蛋糕")
# # else:
# #     print("每天都是节日")


# while 1:
#     core = int(input("输入你的分数"))
#     if core>90 and core<100:
#         print("优秀")
#     elif core>70 and core<90:
#         print("一般")
#     elif core>60 and core<70:
#         print("及格")
#     elif core>0 and core<60:
#         print("不及格")
#     else:
#         print("请输入有效成绩！")

# a = int(input("请出入一个整数："))
# if a % 2 == 0:
#     if a % 3 == 0:
#         print("hello world")
#     else:
#         print("hello")
# elif a % 3 == 0:
#     print("word")
# else:
#     print("123")
# import random
# while 1:
#     a = int (input("输入玩家要出的拳,石头1,剪刀2,布3"))
#     b = random.randint(1,3)
#     print ("电脑出的是: %d"%b)
#     if (a == 1 and b == 2) or (a == 2 and b ==3) or(a == 3 and b ==1):
#         print("玩家赢")
#     elif a == b:
#         print("平局")
#     else:
#         print("电脑赢")

# has_ticket = int(input("请出示车票(1代表有，2代表没有:"))
# if has_ticket == True:
#     print("可以进行安检")
#     knife_length = int(input("请输入刀的长度"))
#     if knife_length > 20:
#          print("刀的长度 %d cm 不允许上车" % knife_length)
#     else:
#         print("安检通过")
# else:
#     print("请先购买车票")


# i = 0
# a = 0
# while i<= 100:
#     a = a + i
#     i = i + 1
# print(a)

# i = 1
# a = 1
# while i<=10:
#     a = a * i
#     i = i + 1
# print(a)




# a = 1
# while a <= 9:
#     i = 1
#     while i <= a:
#         c = a * i
#         print("%d * %d = %d" %(a,i,c),end="\t")
#         i += 1
#     print("")
#     a += 1




# a = 2
# c = 0
# while a <= 100:
#     b = 2
#     while b < a:
#         if a % b == 0:
#             break
#         b = b + 1
#     else:
#         c = c + a
#     a = a + 1
# print(c)






# c = 0
# for a in range (100)"
#     for b in range(2,a):
#         if a % b

# a = 1
# while a <=4:
#     b = 1
#     while b <=4:
#         c = 1
#         while c <=4:
#             if a!=b and b!=c and c!=a:
#                 print("%d%d%d" % (a,b,c))
#             c = c + 1
#         b = b + 1
#     a = a + 1
# #
#
# a = 100
# while a <= 999:
#     b = a // 100
#     c = (a - b*100) // 10
#     d = a - b*100 - c*10
#     if b**3 + c**3 + d ** 3 ==a:
#         print(a,end=" ")
#     a += 1

#
# a = ["zhangshan","lisi","wangwu"]
# for i in a:
#     print("恭喜%s毕业"%i)

# b = ["郑梦玲","张表","王昆"]
# a = 0
# while a <= len(b)-1:
#     print("恭喜%s顺利毕业" %b[a])
#     a +=1


# for a in range(1,4):
#     for b in range(1,4):
#         for c in range(1,4):
#                 if (a!=b) and (b!=c) and (c!=a):
#                         print(a, b, c)

# 冒泡法
# a=[30,28,77,16,98]
# for i in  range(len(a)-1):
#     for j in range(len(a)-1):
#         if a[j] < a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j]
# print(a)
# 选择法排序
# a = [30,28,77,16,98]
# for i in range(len(a)-1):
#     for j in range(i+1,len(a)):
#         if a[i] < a [j]:
#             a[i],a[j] = a[j], a[i]
# print(a)


# b = ["郑梦玲","张标","王昆","张标"]
# b.remove("王昆")
# print(b)


# a = 1
# while a<=4:
#     b = 1
#     while b<=4:
#         c = 1
#         while c<=4:
#             if a!=b and b!=c and c!=a:
#                 print("%d%d%d" % (a,b,c))
#             c = c+1
#         b = b+1
#     a = a+1


# for i in range (100,999):
#     a = i//100
#     b = (i-a*100)//10
#     c = i-a*100-b*10
#     if a**3+b**3+c**3 == i:
#         print(i, end=" ")


# a = 1
# while a<=9
#     i = 1
#     while i<=a
#         c=a*i
#         print("%d*%d=%d" % (a,i,c),end="\t")
#         i=i+1
#     print(" ")
#     a=a+1

# b = input("输入一个字符串:")
# if b == "a":
#     print("123")
# else:
#     print("456")
#
# 123(int) 判断以1开头3结尾 type

# a='123'
# print(type(a))
# a=123
# a=str(a)
# print(a[1])

# 转义字符
# a="i'm a \"boy\""
# print(a)

# a='abc'+'sgaegag'
#
# d = 'abc'
# print(d[2])
#
# a = 'abcdefgh'
# print(a[2::3])
# a=11
# a%=6
# print(a)

# a = '123'
# if '3' in a:
#     print('张龙超')
# else:
#     print("张龙超112123")

# fs = int(input("请输入一个分数 :"))
# if fs >= 90 and  fs<= 100:
#     print("优秀")
# elif fs >=70 and fs<=90:
#     print("一般")
# elif fs >=60 and fs<=70:
#     print("及格")
# elif fs >=0 and fs <=60:
#     print("不及格")
# else:
#     print("请重新输入")
#
# i = int(input("判断地瓜熟了没有: "))
# if i>=0 and i<=2:
#     print("是生的")
# elif i>=3 and i<=4:
#     print("半生不熟")
# elif i==5:
#     print("是熟的")
# elif i>=8:
#     print("焦了")

# a = '123'
# b = '123'
# i= input("输入一个字符串")
# if a == '123'and b=='123':
#     print("123")
# elif a!= '123':
#     print('456')
#     if b =='123':
#         print('789')
# elif a!='123'and b!='123':
#         print('没了')
#
# b = input("请输入一串小写字符")
# a = b.swapcase()
# print(a)
#
# a ='qqqq'
# b =a.replace('q','123',4)
# print(b)

# print(input('请输入一串小写字符：').swapcase())\
# a = 'asdfga-sdfgas-dfga-sdfg'
# b = a.split('-')
# print(b)
# c = 'sadfdsaasdfgfgfgf'
# a = c.split('d')
# b='-'.join(a)
# print(b)

# a = 'addd'.endswith('b')
# print(a)
# '%'%填的字符  %s：通过str()将输入的字符转化成字符串  %d只能填整数  %f只能填浮点数
# a = '%s%s'%(123,123)
# print()
# '{}'.format():格式化字符串
# a='{}*{}={}'.format(1,2,1*2)
# print(a)


# # f'{}'
# a='abc'
# b='def'
# print(f'{a}{b}')
# a='qwertqwertqwertqwerq'
# b=a.strip('qwer')
# print(b)

# b='fawfwafaegf'.index('a',2,10)
# print(b)wh

# a='sdafsafa'
# b=len(a)
# print(b)


# for i in 'abc':
#     print(i)
# for i in ['faefeaf'],['fafeeaf'],['faefeafe']:
#     print(i)
# 奇数和
# a = 0
# for i in range(0,101,2):
#     a = a +i
#     print(a)

# a = 1
# for i in range(0,100,):
#     a = a+i
#     i=2+1
#     print(a)

# for i in 'abcfeafa':
#     if i=='c':
#         break
#     else:
#         print('abc')
#     print(i,end=" ")
# else:
#     print('循环结束')
# #
# for i in ('abc'):
#     print(i,end=" ")
#     for a in ('bcd'):
#         print(a,end=" ")
# 将列表中以a或者A开头，并且以c结尾的打印出来
#
# a=['abc','ABC','abb','cda']
# for i in a:
#     if i.startswith('a') or i.startswith('A'):
#         if i.endswith('c'):
#             print(i)

# b=[11,22,33,44,55,66,77,88,99]
# a=[ ]
# c=[ ]
# for a in b:
#     if  a >b[4]:
#         print(a,end=" ")
# for c in b:
#     if  c <b[4]:
#         print(c,end=" ")

# b = input('请输入一个小写字符串')
# a = b.title()
# c = b.replace(a,123)
# print(b)
# 1.把列表中的每个数据取出来
# 2.判断这个数据在列表中的个数
# 3.如果统计出来的结果大于1，删除此数据
#去除列表中重复的数据


# a = [143,456,134,616,12,12,12]
# b = []
# for i in a :
#     if i in a:
#         if i not in b:
#             b.append(i)
# print(b)

# a = [143,456,134,616,12,12,12]
# for j in a :
#     for i in a :
#         b = a.count(i)
#         if b > 1:
#             a.remove(i)
# print(a)

# b = [11,22,33,44,55,66,77,88,99]
# for i in b:
#     if i
# c = 0
# for a in range(2,101):
#     for b in range(2,a):
#         if a%b==0:
#             break
#     else:
#         c=c+a
# print(c)
import ccccc.day
