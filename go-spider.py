from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from indeed.spiders.indeed_spidier import IndeedSpider
import sys

#print("hasjdhakdhkahd")
#print(sys.argv[1])
process = CrawlerProcess(get_project_settings())
process.crawl(IndeedSpider(), query=sys.argv[1], location=sys.argv[2] )
#process.crawl(IndeedSpider)
process.start()

