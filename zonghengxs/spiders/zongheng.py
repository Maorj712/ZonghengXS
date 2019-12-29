# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from zonghengxs.items import ZonghengxsItemLoader, ZonghengxsItem


class ZonghengSpider(scrapy.Spider):
    name = 'zongheng'
    allowed_domains = ['book.zongheng.com/']

    def start_requests(self):
        for i in range(1, 6):
            url = "http://book.zongheng.com/store/c0/c0/b0/u0/p"+str(i)+"/v0/s9/t0/u0/i1/ALL.html"
            yield Request(url=url, callback=self.get_book_page, dont_filter=True)

    def get_book_page(self, response):
        book_urls = response.xpath("//div[@class='bookname']/a/@href").extract()
        for book_url in book_urls:
            yield Request(url=book_url, callback=self.to_read, dont_filter=True)

    def to_read(self, response):
        read_url = response.css(".btn.read-btn::attr(href)").extract()[0]
        yield Request(url=read_url, callback=self.parse_chapter, dont_filter=True)

    def parse_chapter(self, response):
        itemloader = ZonghengxsItemLoader(item=ZonghengxsItem(), response=response)
        itemloader.add_xpath("name", "//div[@class='reader_crumb']/a[3]/text()")
        itemloader.add_css("title", ".title_txtbox::text")
        itemloader.add_xpath("details", "//div[@class='content']")
        novel_item = itemloader.load_item()
        yield novel_item

        next_chapter_url = response.xpath("//a[@class='nextchapter']/@href").extract()[0]
        if next_chapter_url:
            yield Request(url=next_chapter_url, callback=self.parse_chapter, dont_filter=True)
