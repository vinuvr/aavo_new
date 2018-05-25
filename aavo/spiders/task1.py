# -*- coding: utf-8 -*-
import scrapy
import math


class Task1Spider(scrapy.Spider):
	name = 'task1'
	allowed_domains = ['www.avvo.com']
	with open("event.csv")as fs:
			
    		start_urls =[event_url.strip() for event_url in fs.readlines()]

	def parse(self, response):
		a1=open("pages.csv",'a')
		pages=response.xpath('//*[@id="title-total-count"]/text()').extract()
		url=response.url
		for item in pages:
			a2=float((item[2:6]))
			a3=math.ceil(a2/10)
			for k in xrange(1,int(a3+1)):
				a4=url+'?&page=%s&sort=relevancy'%k+('\n')
			
				a1.write(a4)
		a1.close()
