from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

from lyricwiki.items import LyricWikiItem

class LyricWikiSpider(CrawlSpider):
    name = "oldirty"                                         #CHANGE NAME
    allowed_domains = ["lyrics.wikia.com"]
    start_urls = [
        "http://lyrics.wikia.com/Ol_Dirty_Bastard",     #CHANGE URL
    ]
    rules = (                                               #CHANGE REGEX
        Rule(SgmlLinkExtractor(allow=('/Ol.*',),restrict_xpaths=('//ol/li',)), callback='parse_item', follow=True),
        )

    def parse_item(self, response):
        sel = Selector(response)
        info = sel.xpath('//div[@class="mw-content-ltr"]')
        item = LyricWikiItem()
        item['title'] = sel.xpath('//header[@id="WikiaPageHeader"]/h1/text()').extract()
        item['artist'] = info.xpath('b/a/text()').extract()
        item['album'] = info.xpath('i/a/text()').extract()
        item['lyrics'] = sel.xpath('//div[@class="lyricbox"]/text()').extract()
        return item