# -*- coding: utf-8 -*-
import scrapy


class Task3Spider(scrapy.Spider):
	name = 'task3'	
	allowed_domains = ['www.avvo.com']
	#with open("url.csv")as f:
	start_urls =['https://www.avvo.com/attorneys/10020-ny-elisabeth-mullen-1793038.html','https://www.avvo.com/attorneys/10004-ny-mirta-desir-3813985.html',
'https://www.avvo.com/attorneys/10111-ny-yalda-haery-4552309.html',
'https://www.avvo.com/attorneys/08830-nj-john-nachlinger-1602376.html',
'https://www.avvo.com/attorneys/10023-ny-robin-fleischner-836471.html',
'https://www.avvo.com/attorneys/11590-ny-alissa-vanhorn-1013255.html',
'https://www.avvo.com/attorneys/10007-ny-clifford-greenberg-895360.html',
'https://www.avvo.com/attorneys/11201-ny-marykatherine-brown-968292.html',
'https://www.avvo.com/attorneys/11215-ny-brian-esser-1017149.html',
'https://www.avvo.com/attorneys/11570-ny-anthony-brown-998056.html',
'https://www.avvo.com/attorneys/10017-ny-helen-dukhan-1227960.html',
'https://www.avvo.com/attorneys/10304-ny-karen-soren-941084.html',
'https://www.avvo.com/attorneys/10007-ny-darren-bleier-4353662.html',]
#[url.strip() for url in f.readlines()]
		
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

