### 1. 网页下载器简介
python 3.x中urllib库和urilib2库合并成了urllib库，其中
```
urllib2.urlopen()变成了urllib.request.urlopen()
urllib2.Request()变成了urllib.request.Request()
```
urllib2 - python基本库，支持直接的URL下载、需要登陆网页的cookie处理、需要代理访问的代理处理等<br/>
request - 第三方，更多功能

![](https://github.com/vulcan-soundwave/Python-Web-Crawler/blob/master/pictures/4_0.jpg)

### 2. urllib2下载网页的三种方法
网页HTTP状态码：表示HTTP协议所返回的响应状态<br/>
常用两种：<br/>
200：请求成功，请求所希望的响应头或者数据体随此响应返回。<br/>
404：Not Found，请求失败，表示请求的资源未被在服务器上发现。整个状态可能是暂时的，也可能是永久的。所以，要做好该状态下的处理。

#### 1. urllib下载网页方法1：最简洁方法

![](https://github.com/vulcan-soundwave/Python-Web-Crawler/blob/master/pictures/4_1.jpg)

```
# python 2
import urllib2
url = 'https://baidu.com'

#直接请求
response1 = urllib2.urlopen(url)
#获取状态码，如果是200则获取成功
print response1.getcode()
#读取内容
cont = response1.read()
#返回的网页内容的长度
print len(response1.read())
```
```
# python 3.6.2
import urllib.request
url = 'https://baidu.com'

#直接请求
response1 = urllib.request.urlopen(url)
#获取状态码，如果是200则获取成功
print(response1.getcode())
#读取内容 #cont是很长的字符串就不输出了
cont = response1.read()
#返回的网页内容的长度
print(len(response1.read()))
```
#### 2. urllib下载网页方法2：添加data、http header

![](https://github.com/vulcan-soundwave/Python-Web-Crawler/blob/master/pictures/4_3.jpg)

```
# python 2
import urllib2
url = 'https://baidu.com'

#创建Request对象
request = urllib2.Request(url)
#添加数据
request.add_data('a','1')
#添加http的header #将爬虫伪装成Mozilla浏览器
request.add_header('user-agent', 'Mozilla/5.0')
#发送请求获取结果
response2 = urllib2.urlopen(request)
```
```
# python 3.6.2
import urllib.request
url = 'https://baidu.com'

#创建Request对象
request = urllib.request.Request(url)
#添加数据
request.data = 'a'  #???
#添加http的header #将爬虫伪装成Mozilla浏览器
request.add_header('user-agent', 'Mozilla/5.0')
#发送请求获取结果
response2 = urllib.request.urlopen(request)
```

#### 3. urllib下载网页方法3：添加特殊情景的处理器

![](https://github.com/vulcan-soundwave/Python-Web-Crawler/blob/master/pictures/4_5.jpg)

```
# python 2
import urllib2
import cookielib
url = 'https://baidu.com'

#创建cookie容器
cj = cookielibCookieJar()
#创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#给urllib安装opener
urllib2.install_opener(opener)
#使用带有cookie的urllib访问网页
response3 = urllib2.urlopen(url)
```
```
# python 3.6.2
import urllib.request
import http.cookiejar
url = 'https://baidu.com'

#创建cookie容器
cj = http.cookiejar.CookieJar()
#创建一个opener
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
#给urllib安装opener
urllib.request.install_opener(opener)
#使用带有cookie的urllib访问网页
response3 = urllib.request.urlopen(url)
```
### 3. urllib实例代码演示
- 代码：
![](https://github.com/vulcan-soundwave/Python-Web-Crawler/blob/master/pictures/4_7.png)
- 结果：

![](https://github.com/vulcan-soundwave/Python-Web-Crawler/blob/master/pictures/4_8.png)
