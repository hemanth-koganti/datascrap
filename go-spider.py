from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from indeed.spiders.indeed_spidier import IndeedSpider


process = CrawlerProcess(get_project_settings())
process.crawl(IndeedSpider(), query='full stack', location='' )
#process.crawl(IndeedSpider)
process.start()

