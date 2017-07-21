#!/usr/bin/env python3
#coding:utf-8

import shelve

with shelve.open('shelve.data') as f:
    print(f.get('test'))
    print(f.get('time'))
    f.get('test')()


'''
shelve是一个简单的数据存储方案，类似key-value数据库，可以很方便的保存python对象，其内部是通过pickle协议来实现数据序列化。
shelve只有一个open()函数，这个函数用于打开指定的文件（一个持久的字典），然后返回一个shelf对象。shelf是一种持久的、类似字典的对象。
它与“dbm”的不同之处在于，其values值可以是任意基本Python对象--pickle模块可以处理的任何数据。
这包括大多数类实例、递归数据类型和包含很多共享子对象的对象。keys还是普通的字符串。

五、总结
1. 对比

json模块常用于编写web接口，将Python数据转换为通用的json格式传递给其它系统或客户端；也可以用于将Python数据保存到本地文件中，缺点是明文保存，保密性差。另外，如果需要保存非内置数据类型需要编写额外的转换函数或自定义类。

pickle模块和shelve模块由于使用其特有的序列化协议，其序列化之后的数据只能被Python识别，因此只能用于Python系统内部。另外，Python 2.x 和 Python
3.x 默认使用的序列化协议也不同，如果需要互相兼容需要在序列化时通过protocol参数指定协议版本。除了上面这些缺点外，pickle模块和shelve模块相对于json模块的优点在于对于自定义数据类型可以直接序列化和反序列化，不需要编写额外的转换函数或类。

shelve模块可以看做是pickle模块的升级版，因为shelve使用的就是pickle的序列化协议，但是shelve比pickle提供的操作方式更加简单、方便。shelve模块相对于其它两个模块在将Python数据持久化到本地磁盘时有一个很明显的优点就是，它允许我们可以像操作dict一样操作被序列化的数据，而不必一次性的保存或读取所有数据。

2. 建议

需要与外部系统交互时用json模块；
需要将少量、简单Python数据持久化到本地磁盘文件时可以考虑用pickle模块；
需要将大量Python数据持久化到本地磁盘文件或需要一些简单的类似数据库的增删改查功能时，可以考虑用shelve模块。
3. 附录

要实现的功能	可以使用的api
将Python数据类型转换为（json）字符串	json.dumps()
将json字符串转换为Python数据类型	json.loads()
将Python数据类型以json形式保存到本地磁盘	json.dump()
将本地磁盘文件中的json数据转换为Python数据类型	json.load()
将Python数据类型转换为Python特定的二进制格式	pickle.dumps()
将Python特定的的二进制格式数据转换为Python数据类型	pickle.loads()
将Python数据类型以Python特定的二进制格式保存到本地磁盘	pickle.dump()
将本地磁盘文件中的Python特定的二进制格式数据转换为Python数据类型	pickle.load()
以类型dict的形式将Python数据类型保存到本地磁盘或读取本地磁盘数据并转换为数据类型	shelve.open()
http://www.cnblogs.com/yyds/p/6563608.html
'''