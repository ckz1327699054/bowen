#！/usr/bin/python
#-*-coding:utf8-*-
a= int(input("输入总钱数："))
gw=[]
goods=[{'name':'电脑','price':1999},
   {'name':'显示器','price':500},
   {'name':'餐桌','price':100},
   {'name':'游艇','price':999},
   {'name':'凳子','price':10}]
for b,c in enumerate(goods):
   print(b,c)
while 1:
    d = int(input("输入商品号："))
    print(goods[d]["name"])
    e = int(input("是否将此商品添加到购物车 1（是） 0（否）："))
    if e == 1:
       gw.append(goods[d]["name"])
       print("添加成功")
       f = int(input("是否继续添加物品到购物车 1（是） 0（否）:"))
       if f == 1:
          d = int(input("输入商品号："))
          gw.append(goods[d]["name"])
          print("添加成功")
       else:
          print("不在添加")
    else:
       print("添加失败")
    h = goods[d]["price"]
    g = int(input("是否付款 1（是） 0（否）："))
    if g == 1:
       if a > h:
          print("付款成功")
       else:
          print("您的余额不足")
          k = int(input("余额不足，是否将购物车商品移除 1（是） 0（否）:"))
          if k == 1:
              gw.remove(goods[d]["name"])
              print("移除成功")
          else:
             print("移除失败")
          i = int(input("是否要充值 1（是） 0（否）:"))
          if i == 1:
             j = int(input("请输入充值金额："))
             a += j
             print("充值成功你已经充值:%d,现在剩余%d"%(j,j+a))
          else:
             print("放弃充值")
    l=int(input("是否要继续购物 1(是)0(不是)："))
    if l==1:
        d = int(input("输入商品号："))
        print(goods[d]["name"])
        if l==0:
            print("谢谢惠顾")
        break















