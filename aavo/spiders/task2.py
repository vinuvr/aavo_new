# -*- coding: utf-8 -*-
import scrapy


class task2Spider1(scrapy.Spider):
	name = 'task2'
	allowed_domains = ['www.avvo.com']
	start_urls = ['https://www.avvo.com/adoption-lawyer/ny/new_york.html?&page=%s&sort=relevancy'%page for page in xrange(1,13)]
	#rules = ( Rule(LinkExtractor(allow=('course-finder', ),restrict_xpaths=('//li[@class="pagination-page"]',)), callback='parse_items',follow=True), )

	def parse(self, response):
	        url=response.css(".row div.col-xs-8 a.v-serp-block-link::attr(href)").extract()
		a=open('url.csv','a')
		for item in url:
		
			ne=("https://www.avvo.com"+item+("\n"))
			a.write(ne)
	
		a.close()



'''
		next_page = response.xpath('.//a[@class="button next"]/@href').extract()
		if next_page:
			next_href = next_page[0]
			next_page_url = 'http://sfbay.craigslist.org' + next_href
			request = scrapy.Request(url=next_page_url)
			yield request

class Vinu2Spider2(scrapy.Spider):

	#with open("vv.csv")as f:
	start_urls = ['https://www.avvo.com/attorneys/10036-ny-rosanne-felicello-1320313.html']
		

	def parse(self, response):
        	url=response.xpath('//div[2]/h1/span/text()').extract()
		na={'url':url}
		yield na

'''
