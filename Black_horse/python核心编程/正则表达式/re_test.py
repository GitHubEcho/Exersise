import re

# 电话号码匹配
res = re.match("1[7]/d{9}", "13110097076")
print(res)

# 匹配0-100之间的数
for x in range(101):
    if re.match(r'[1-9]\d?$|100$|0$', str(x)):
        pass
    else:
        print(x)
        print('False')

for x in range(101):
    if re.match(r'[1-9]?\d?$|100$', str(x)):
        pass
    else:
        print(x)
        print('False')

# 匹配HTML标记
s = '<html><h1>hello</h1></html>'
re.match(r'<(.+)><(.+)>(.*)</\2></\1>', s)


# 按需替换


def repalece(result):
    result = result.group()
    result = int(result)
    if result == 500:
        return str(result + 50)
    elif result == 300:
        return str(result - 30)


res = re.sub(r'\d+', repalece, 'cost : 500,python :300')
print(res)

# 从html中提取文本信息
s = '''
    <div>
            <p>岗位职责：</p>
    <p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
    <p><br></p>
    <p>必备要求：</p>
    <p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
    <p>&nbsp;<br></p>
    <p>技术要求：</p>
    <p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
    <p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
    <p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
    <p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
    <p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
    <p>&nbsp;<br></p>
    <p>加分项：</p>
    <p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>

    </div>

     '''
res = re.sub(r'</?\w+>', '', s)
print(res)

res = re.sub(r'</?\.+>', '', s)  # 默认是贪婪模式
print(res)

# 提取网址
html = '''<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg"
          src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">
       '''
re.search(r'https.+?\.jpg', html).group()
# Out[24]:
'https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg'

# 网址替换
url = 'http://www.baidu.com/messageinfo.asp?id=35'

re.sub(r'http://.+?/','',url )
# Out[13]:
'messageinfo.asp?id=35'

re.sub(r'(http://.+?/).*',lambda x:x.group(1),url )
# Out[24]:
'http://www.baidu.com/'
