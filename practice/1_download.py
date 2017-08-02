#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import http.cookiejar
url = 'https://baidu.com'

print('方法1111111：')
response1 = urllib.request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))

print('方法2222222：')
request = urllib.request.Request(url)
request.add_header('user-agent', 'Mozilla/5.0')
response2 = urllib.request.urlopen(request)
print(response2.getcode())
print(len(response2.read()))

print('方法3333333：')
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
print(response3.getcode())
print(cj)
print(response3.read())
