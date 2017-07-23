#/usr/bin/env python3
#coding:utf-8

money = input("your monney :")
money = int(money)
things = [['iphone',4000],['meizu',2000],['xiaomi',3000]]
buy_things = []

for x in things:
    print ('{index}. {thing}(￥{values})'.format(index = things.index(x)+1,thing = x[0],values = x[1]))
while True:
    index = input('plesase input your bug thing index or input q quit:')
    if index.isdigit():
        index = int(index)
        if index > len(things) and index <0:
            print("product is not exist!")
        else:
            if money >= things[index-1][1]:
                money = money - things[int(index)-1][1]
                buy_things.append(things[index-1])
                print ('your remaining money is %s' % money)
                print ('Purchase success,please go to the shopping cart')
            else:
                print ('your money is %s not enough'%money)
    elif index == 'q':
        print  ('shopping list'.center(50,'-'))
        for x in buy_things:
            print (x)
        print ('your remaining money is %s' % money)

        exit()
    else :
        print("invalid option")

