# These are the possible items we are trying to get from the page
# to download.

from scrapy.item import Item, Field

class NotedownloaderItem(Item):
    lectures = Field()
    handouts = Field()
    discussion_problems = Field()
    assignments = Field()
    file_urls = Field()
    files = Field()