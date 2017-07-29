#### 1. URL管理器介绍
URL管理器：管理待抓取URL集合和已抓取URL集合<br/>
防止重复抓取、防止循环抓取<br/>
功能：
1. 判断待添加URL是否在容器中
2. 添加新URL到待爬取集合
3. 判断是否有待爬取URL
4. 获取待爬取URL
5. 将URL从待爬取移动至已爬取

![](https://github.com/vulcan-soundwave/Python-Web-Crawler/blob/master/pictures/3_0.jpg)

#### 2. URL管理器实现方法
  URL管理器的实现方式有三种：
- 适合个人的：内存
- 小型企业或个人：关系数据库（永久存储或内存不够用）
- 大型互联网公司：缓存数据库（高性能）

![](https://github.com/vulcan-soundwave/Python-Web-Crawler/blob/master/pictures/3_1.jpg)

- 选用set三因为可以自动去重<br/>
- is_crawled可以标志待爬取和已爬取URL，也就是说可以用一个表实现待爬取和已爬取URL集合
