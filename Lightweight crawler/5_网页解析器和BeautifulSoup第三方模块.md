### 1. Python爬虫网页解析器简介
网页解析器：从网页中提取有价值数据的工具<br/>
网页解析器以Html网页字符串为输入提取出价值数据和新URL列表<br/>
Python网页解析器：
1. 正则表达式
2. html.parser
3. BeautifulSoup（可使用html.parser和lxml作为解析器，较强大）
4. lxml<br/>
正则表达式采取模糊匹配<br/>
后三者采取结构化解析

- 结构化解析-DOM树-通过树可以定位到元素，访问其属性和自身文本
![](5_1.jpg)#pass

### 2. BeautifulSoup模块介绍和安装
官方文档：https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#id5

####安装 Beautiful Soup

> 如果你用的是新版的Debain或ubuntu,那么可以通过系统的软件包管理来安装:

> $ apt-get install Python-bs4

> Beautiful Soup 4 通过PyPi发布,所以如果你无法使用系统包管理安装,那么也可以通过 easy_install 或 pip 来安装.包的名字是 beautifulsoup4 ,这个包兼容Python2和Python3.

> $ easy_install beautifulsoup4
> $ pip install beautifulsoup4

> (在PyPi中还有一个名字是 BeautifulSoup 的包,但那可能不是你想要的,那是 Beautiful Soup3 的发布版本,因为很多项目还在使用BS3, 所以 BeautifulSoup 包依然有效.但是如果你在编写新项目,那么你应该安装的 beautifulsoup4 )

> 如果你没有安装 easy_install 或 pip ,那你也可以 下载BS4的源码 ,然后通过setup.py来安装.

> $ Python setup.py install

> 如果上述安装方法都行不通,Beautiful Soup的发布协议允许你将BS4的代码打包在你的项目中,这样无须安装即可使用.

> 作者在Python2.7和Python3.2的版本下开发Beautiful Soup, 理论上Beautiful Soup应该在所有当前的Python版本中正常工作

##安装完成后的问题

> Beautiful Soup发布时打包成Python2版本的代码,在Python3环境下安装时,会自动转换成Python3的代码,如果没有一个安装的过程,那么代码就不会被转换.

>如果代码抛出了 ImportError 的异常: “No module named HTMLParser”, 这是因为你在Python3版本中执行Python2版本的代码.

> 如果代码抛出了 ImportError 的异常: “No module named html.parser”, 这是因为你在Python2版本中执行Python3版本的代码.

> 如果遇到上述2种情况,最好的解决方法是重新安装BeautifulSoup4.

> 如果在ROOT_TAG_NAME = u’[document]’代码处遇到 SyntaxError “Invalid syntax”错误,需要将把BS4的Python代码版本从Python2转换到Python3. 可以重新安装BS4:

> $ Python3 setup.py install

> 或在bs4的目录中执行Python代码版本转换脚本

> $ 2to3-3.2 -w bs4

出现错误：
> \>>from bs4 import BeautifulSoup
>ImportError: cannot import name 'HTMLParseError'

原因是BeautifulSoup4版本过低，提供两种方法：<br/>
1)在官网下载更新版本的BeautifulSoup4的源码，重新执行<br/>
```
# tar -xvf beautifulsoup4-4.x.0.tar.gz
# python setup.py install
```
2)利用pip命令升级<br/>
whereis pip 查看pip是否在path中<br/>
没有的话，<br/>
```
# yum -y install python-pip
# pip install --upgrade beautifulsoup4
```
然后提示，<br/>
```
Successfully installed beautifulsoup4-4.6.0
You are using pip version 8.1.2, however version 9.0.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
# pip install --upgrade pip 升级pip成功
Successfully installed pip-9.0.1
```
执行完发现，还是不行，这是为什么呢，原来默认是使用的pip是指系统自带的python2中的升级命令，那么我们要升级python3的呢，很明显，使用pip3呀<br/>
而python3安装自带pip3
```
# ln -s /usr/python/Python3.6.2/bin/pip3 /usr/bin/pip3
# pip3 install --upgrade beautifulsoup4
```
ok了

### 3. BeautifulSoup的语法
####BeautifulSoup语法：
根据一个HTML网页字符串创建BeautifulSoup对象，创建的同时就将整个文档字符串下载成一个DOM树，后根据这个DOM树搜索节点。find_all方法搜索出所有满足的节点，find方法只会搜索出第一个满足的节点，两方法参数一致。搜索出节点后就可以访问节点的名称、属性、文字。因此在搜索时也可以按照以上三项搜索。
- 创建BeautifulSoup对象
```
from bs4 import BeautifulSoup
#根据HTML网页字符串创建BeautifulSoup对象
soup = BeautifulSoup(
	html_doc,			#HTML文档字符串
	'html.parser',		#HTML解析器
	from_encoding='utf-8')	#HTML文档的编码
```
- 搜索节点(find_all, find)/搜索DOM树
```
#方法：find_all(name, attrs, string)
	find_all(节点名字，节点属性，节点文字)

#查找所有标签为a的节点
soup.find_all('a')

#查找所有标签为a，链接符合/view/123.html形式的节点
soup.find_all('a', href='/view/123.htm')
soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))	#正则表达式

#查找所有标签为div，class为abc，文字为Python的节点
soup.find_all('div', class_='abc', string='Python')
class_为了避免和关键字class冲突
```
- 访问节点信息
```
#假设得到节点： <a href='1.html'>Python</a>
#获取查找到的节点的标签名称
	node.name
#获取查找到的a节点的href属性
	node['href']
#获取查找到的a节点的链接文字
	node.get_text()
```
### 4. BeautifulSoup实例测试
	[../python/2_parser.py]

