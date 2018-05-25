# -*- coding: utf-8 -*-
import scrapy


class Task0Spider(scrapy.Spider):
	name = 'task0'
	allowed_domains = ['www.avvo.com']
	start_urls = ['https://www.avvo.com/find-a-lawyer/all-practice-areas/ny/']

	def parse(self, response):
		v=open("event.csv",'wb')
        	event=response.xpath('//a[@title]/@href').extract()
		for item in event:
			
			ni=("https://www.avvo.com"+item+("\n"))
			v.write(ni)
			
		v.close()

		
