# -*- coding: utf-8 -*-
import scrapy


class Some_spider(scrapy.Spider):
    """定义蜘蛛的类 继承scrapy Spider类"""

    """ 可以直接调用
    [s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
    [s]   crawler    <scrapy.crawler.Crawler object at 0x0000025830967280>
    [s]   item       {}
    [s]   request    <GET http://www.worldrobotconference.com/html/jiqirendasai/dasaigonggao/>
    [s]   response   <200 http://www.worldrobotconference.com/html/jiqirendasai/dasaigonggao/>
    [s]   settings   <scrapy.settings.Settings object at 0x0000025830967310>
    [s]   spider     <DefaultSpider 'default' at 0x25830e49c40>
     """
         
    name = 'wangwei'
    # 必须要有名字
    # 必须要有这个网址列表，要不然后台为空表
    start_urls = ['http://www.worldrobotconference.com/html/jiqirendasai/dasaigonggao/']

    def parse(self, response):
        """ the parse method as callback function for the Requests. """
        """
        response的方法
        'body',
        'body_as_unicode',
        'cb_kwargs',
        'certificate',
        'copy',
        'css',
        'encoding',
        'flags',
        'follow',
        'follow_all',
        'headers',
        'ip_address',
        'json',
        'meta',
        'replace',
        'request',
        'selector',
        'status',
        'text',
        'url',
        'urljoin',
        'xpath']
        1.你可以使用选择器（自带）处理这些 网页内容 ：page content
        ag 
            >>> response.selector.xpath('//span/text()').get()
            'good'

            >>> response.xpath('//span/text()').get()
            'good'
            >>> response.css('span::text').get()
            'good'
            
        2.使用你喜欢的处理方式
            from bs4 import beautsoup 
            等等
        
        存储获取的网页content
        1 管道下载
            todo
        2 直接保存
            json
            csv
            txt
            xml
            html
                     """
        # with open('jieguo.html', 'wb') as f:
        #     f.write(response.body)
        for li in response.xpath('//ul[@class="news-list"]/li'):
            yield {
                'time' : li.xpath('./div[@class="time"]//text()').extract(),
                'name' : li.xpath('./div[@class="name"]/a/text()').extract(),
                'content' : li.xpath('./div[@class="content"]/text()').extract_first()
            }