# Scrapy settings for noteDownloader project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'noteDownloader'

SPIDER_MODULES = ['noteDownloader.spiders']
NEWSPIDER_MODULE = 'noteDownloader.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'noteDownloader (+http://www.yourdomain.com)'
