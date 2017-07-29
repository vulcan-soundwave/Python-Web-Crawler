#/usr/bin/env python
# -*- coding: utf-8 -*-

#调度程序
#from baike_spider import url_manager
#from baike_spider import html_downloader
#from baike_spider import html_parser
#from baike_spider import html_outputer
import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):
	def __init__(self):
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()

	def craw(self, root_url):
		count = 1
		self.urls.add_new_url(root_url)
		# spider loop --> 1000
		while self.urls.has_new_url():
			try:
				new_url = self.urls.get_new_url()
				print('craw %d : %s' % (count, new_url))
				html_cont = self.downloader.download(new_url)
				new_urls, new_data = self.parser.parse(new_url, html_cont)
				self.urls.add_new_urls(new_urls)
				self.outputer.collect_data(new_data)
				
				if count == 1000:
					break      
				count += 1
			#异常处理	
			#except:
			#	print('craw failed.')		
			except Exception as e:
				print(str(e)+'   '+'这里抓取失败')

		self.outputer.output_html()


if __name__ == '__main__':
	root_url = 'https://baike.baidu.com/item/Python'	#入口url
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)	#启动了爬虫

