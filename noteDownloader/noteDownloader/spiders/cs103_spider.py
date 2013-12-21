# This is what the cs103spider will do to get what you need.
# add more comments later explaining what we will do.
# also add better docstrings
# my path syntax might not be correct. check later. 
# handouts and discussion problems both have handouts in HTML p
# robably should either group those or find a way to categorize the handouts.
# for now i just created a list of the links (if my syntax is correct)
# later add in how to download using pdf
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from noteDownloader.items import NotedownloaderItem

class cs103spider(BaseSpider):
	'''Starts the spider crawling at cs103 site'''
	name = "cs103"
	allowed_domains = ["stanford.edu"]
	start_urls = ["http://www.stanford.edu/class/cs103/"]

	def parse(self, response):
		'''Will go through everything and get the pdf urls to save into
		a file.'''
		sel = HtmlXPathSelector(response)
		title = sel.xpath("//p")
		items = []
		for obj in title:
			item = NotedownloaderItem()
			item["lectures"] = title.xpath('a[contains(@href, "lectures")/@href]').extract() 
			item["handouts"] = title.xpath('a[contains(@href, "handouts")/@href]').extract() 
			item["discussion_problems"] = title.xpath('a[contains(@href, "Discussion Problems")/@href]').extract()
			item["assignments"] = title.xpath('a[contains(@href, "Problem Set")/@href]').extract()
			items.append[item]
		return items



