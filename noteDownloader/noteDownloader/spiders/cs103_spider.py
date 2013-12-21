# This is what the cs103spider will do to get what you need.
# add more comments later explaining what we will do.
# also add better docstrings
# This spider so far can extract the urls for the notes. 
# IMPORTANT everythign has handout in url find a way to classify handouts specifically
# actually do you need the hadnouts? 
# for now i just created a list of the links (if my syntax is correct)
# later add in how to download using pdf
# everytime you tell the spider to crawl delete excel file. 
# run the command scrapy crawl cs103 -o items.csv -t csv to create excel file. 
# also there is probably a more efficient way to do this. 
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
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
		category = sel.select("//p")
		items = []
		for obj in category:
			lecture = obj.select('//a[contains(@href, "lectures")]')
			handout = obj.select('//a[contains(@href, "handouts")]')
			discussion_problem = obj.select('//a[contains(@href, "Discussion Problems")]')
			assignment = obj.select('//a[contains(@href, "Problem Set")]')

			for l in lecture:
				item = NotedownloaderItem()
				item["lectures"] = l.select('@href').extract()
				items.append(item)
			for h in handout:
				item = NotedownloaderItem()
				item["handouts"] = h.select('@href').extract()
				items.append(item)
			for d in discussion_problem:
				item = NotedownloaderItem()
				item["discussion_problems"] = d.select('@href').extract()
				items.append(item)
			for a in assignment:
				item = NotedownloaderItem()
				item["assignments"] = a.select('@href').extract()
				items.append(item)

			return items



