# -*- coding: utf-8 -*-
import scrapy


class Task3Spider(scrapy.Spider):
	name = 'task3'	
	allowed_domains = ['www.avvo.com']
	with open("url.csv")as f:
		start_urls =[url.strip() for url in f.readlines()]
		
	def parse(self, response):

		
        	

		about_more=response.xpath('//a[@class="btn btn-link js-v-profile-more-about-me-cta"]/@href').extract_first()
		url=response.url
		name=response.xpath('//div[2]/h1/span/text()').extract()
		licence=response.xpath('//li[2]/time/text()').extract()
		reviews= response.xpath('//span[@class="small"]/text()').extract()
		avvorating=response.xpath("//span[@class='h3']/span/span/span/text()").extract()

		about=response.xpath('//*[@id="js-truncated-aboutme"]/text()').extract_first()
		area=response.xpath('//ol/li/a/text()').extract()
		img=response.xpath('//img[@class="v-js-headshot img-responsive u-bg-cool-gray"]/@src').extract_first()
		address= response.xpath('//address/span/p/span/text()').extract()
		phone= response.xpath('//a[@class="js-v-phone-replace-link"]/@href').extract_first()
		fax=response.xpath('//address/span/div[2]/span[2]/a/span/text()').extract()
		longitude=response.xpath('//address[@class="js-context js-address js-v-address"]/@data-longitude').extract_first()
		latitude=response.xpath('//address[@class="js-context js-address js-v-address"]/@data-latitude').extract_first()
		



		if img==None and about_more==None:
			m1={"url":url,"name":name,"licence":licence,"reviews":reviews,"avvo_rating":avvorating,"about":about,"work_area":area,"img":img,"address":address,"phone":phone,"fax":fax,"longitude":longitude,"latitude":latitude}
			yield m1
		elif about_more==None:
			m2={"url":url,"name":name,"licence":licence,"reviews":reviews,"avvo_rating":avvorating,"about":about,"work_area":area,"img":"https:"+img,"address":address,"phone":phone,"fax":fax,"longitude":longitude,"latitude":latitude}
			yield m2

		elif  img==None:
			m3={"url":url,"name":name,"licence":licence,"reviews":reviews,"avvo_rating":avvorating,"about":about+' for more information https://www.avvo.com'+ about_more,"work_area":area,"img":"https:"+img,"address":address,"phone":phone,"fax":fax,"longitude":longitude,"latitude":latitude}
			yield m3

		else:
			
			m4={"url":url,"name":name,"licence":licence,"reviews":reviews,"avvo_rating":avvorating,"about":about+' for more information https://www.avvo.com'+ about_more,"work_area":area,"img":"https:"+img,"address":address,"phone":phone,"fax":fax,"longitude":longitude,"latitude":latitude}
			yield m4

