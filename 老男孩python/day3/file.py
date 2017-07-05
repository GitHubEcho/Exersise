#/usr/bin/env python3
#coding:utf-8

f = open('hello','r')  #注意w模式会重新创建文件，会删除原文件

f_new = open('hello2','w')
for line in f:
    #print(line)
    if '不知为何' in line:
        line = line.replace('不知为何','不知所以')
    f_new.write(line)
f.close()
f_new.close()


with open('hello','r',encoding='utf-8') as f ,open('hello2','w',encoding='utf-8') as f_new:
    for line in f:
        print(line)
        if '不知为何' in line:
            line = line.replace('不知为何','不知所以')
        f_new.write(line)




# f.write('\nworrld!')
# print(f.read())
# print('--------')
# print(f.read())  #指针已到结尾



# print(f.readline())
# count = 0
# for line in f:
#     if count == 9:
#         print(line)
#     count +=1