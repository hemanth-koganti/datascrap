# -*- coding: utf-8 -*-
import scrapy
from ..items import IndeedItem


class IndeedSpider(scrapy.Spider):
	name = 'indeed'

	def __init__(self, query='', location='', *args, **kwargs):
		super(IndeedSpider).__init__(*args, **kwargs)

		query = query.replace(' ', '%20')
		location = location.replace(' ', '%20')

		self.start_urls = []
		url = f'https://www.indeed.com/jobs?q={query}&l={location}'
		self.start_urls.append(url)

	def parse(self, response):

		for div in response.xpath('.//td[@id="resultsCol"]/div[div[@class="title"]/a]'):
			url = div.xpath('./div[@class="title"]/a/@href').extract_first()
			url = response.urljoin(url)
			location = div.xpath('.//span[@class="location"]/text()').extract_first()
			salary = div.xpath('./div[@class="salarySnippet"]/span[contains(@class,"salary")]/text()').extract_first()
			company = div.xpath('.//span[@class="company"]/a/text()').extract_first()
			data = {'location': location,
					'salary' : salary,
					'company' : company,
					}

			yield scrapy.Request(url, meta=data, callback=self.parse_details)

		next_page = response.xpath(
			'.//div[@class="pagination"]/a[span/span[contains(text(), "Next")]]/@href').extract_first()
		if next_page:
			print("Going to the Next Page!!")
			yield scrapy.Request(
				response.urljoin(next_page), callback=self.parse)
		else:
			f = open("webpage.html", "w")
			f.write(response.body)
			f.close()


	def parse_details(self, response):

		location = response.meta['location']
		if location:
			location = location.strip()
		
		salary = response.meta['salary']
		if salary:
			salary = salary.strip()

		company = response.meta['company']
		if company:
			company = company.strip()

		title = response.xpath('.//h3[contains(@class, "title")]/text()').extract_first()
		if title:
			title = title.strip()

		description = response.xpath('.//div[contains(@class, "jobDescription")]//text()').extract()

		description_temp = []

		for text in description:
			text = text.strip()
			if text:
				text = text.replace('\n', '')
				description_temp.append(text)

		description = '\n'.join(description_temp)

		pageurl = response.url
		
		item = IndeedItem()
		item['title'] = title
		item['company'] = company
		item['location'] = location
		item['salary'] = salary
		item['description'] = description
		item['pageurl'] = pageurl

		yield item




















