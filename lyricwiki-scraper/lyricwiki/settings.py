# Scrapy settings for lyricwiki project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'lyricwiki'

SPIDER_MODULES = ['lyricwiki.spiders']
NEWSPIDER_MODULE = 'lyricwiki.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lyricwiki (+http://www.yourdomain.com)'
