import datetime as dt
import os
import random
import re
import time
import uuid

import scrapy
from scrapy.spiders import CrawlSpider

from novels.items import NovelsItem, NovelsChapterItem, TypeItem
from savenovelsdate.models import NovelsChapter


class StartnovelsSpider(scrapy.Spider):
    name = 'startnovels'
    allowed_domains = ['www.biquku.la']
    start_urls = ['http://www.biquku.la/xiaoshuodaquan/']

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Referer': 'http://www.biquku.la/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'
        }
    }

    # 获取所有小说
    def parse(self, response):
        li_list = response.xpath('//*[@id="main"]/div[1]/ul/li')
        # novel = li_list[0]
        for i in li_list[4:6]:
            novel_url = i.xpath('./a/@href').get()
            yield scrapy.Request(novel_url,
                                 callback=lambda response, novel_url=novel_url: self.get_novel_detail(response, novel_url))

    # 获取小说详情
    def get_novel_detail(self, response, novel_url):
        item = {}
        typeitem = TypeItem()
        novelsitem = NovelsItem()

        # 小说uid
        novelsitem['uid'] = str(uuid.uuid1().hex)
        # 小说书名
        novelsitem['novel_name'] = response.xpath('//*[@id="info"]/h1/text()').get()
        novel_name = novelsitem['novel_name']
        path_name = 'file/' + novel_name
        os.mkdir(path_name)
        novelsitem['status'] = 1
        novelsitem['is_delete'] = 0
        aa = dt.datetime.now().strftime('%F %T')
        novelsitem['add_time'] = aa
        # 获取小说类型
        div_type = response.xpath('//*[@class="con_top"]').get()
        div_type1 = div_type.split('&gt;')
        div_type2 = div_type1[-2]
        div_type3 = div_type2.split('小说')
        div_type4 = div_type3[0]
        type = div_type4.replace(' ', '')
        typeitem['typename'] = type
        # 获取小说封面图
        novle_img1 = response.xpath('//*[@id="fmimg"]/img/@src').get()
        novelsitem['image'] = 'http://www.biquku.la' + novle_img1
        # 获取小说作者
        div_tag = response.xpath('//*[@id="info"]/p[1]/text()').get()
        author = div_tag.split('：', 1)
        novelsitem['author'] = author[1]
        # 更新时间
        updatetime = response.xpath('//*[@id="info"]/p[3]/text()').get()
        updatetime1 = updatetime.split('：')
        novelsitem['update_time'] = updatetime1[1]
        # 获取简介
        novelsitem['desc'] = response.xpath('//*[@id="intro"]/p[1]/text()').get()
        # 获取每本书的所有章节
        dd_list = response.xpath('//*[@id="list"]/dl/dd')
        # chapter = dd_list[0]
        for i in dd_list: #循环不结束代码是到不了94行的
            novelschapteritem = NovelsChapterItem()
            novelschapteritem['uid'] = str(uuid.uuid1().hex)
            novelschapteritem['chaptername'] = i.xpath('./a/text()').get()
            chaptername = novelschapteritem['chaptername']
            chapter_url = i.xpath('./a/@href').get()
            url = novel_url + chapter_url
            novelschapteritem['add_time'] = aa
            # 构建本地文件夹 先暂时不存
            novelschapteritem['path'] = 'file/' + novel_name + '/' + chaptername + '.txt'
            path = novelschapteritem['path']
            # time.sleep(5)
            item['novelschapteritem'] = novelschapteritem
            item['novelsitem'] = novelsitem
            item['typeitem'] = typeitem
            yield item
            # yield scrapy.Request(url, callback=lambda response, path=path: self.get_chapter_detail(response, path))
            # yield novelsitem
            # yield novelschapteritem

              #存库的操作在这，这个yield开始运行，会调用item,item的类1
            #item的类运行实例化，会将数据序列化成json,json数据会传递到pip中
            #1、yield item运行 2，调用items 3,数据传递到pip

    # 获取章节详情   你这个方法有什么用？
    def get_chapter_detail(self, response, path): #循环一旦开始 这个函数会一直执行调用，可以尝试在这进行存库，每个章节都能存了
        div_content1 = response.xpath('//*[@id="content"]').get()
        # div_content = re.sub(r'\s{4,}', '\r\n\t', div_content1)
        div_content2=div_content1.replace('<div id="content">', '')
        div_content3 = div_content2.replace('</div>', '')
        with open(path, mode='w', newline='', encoding='utf-8') as fw:
            content1 = div_content3.replace('<br>', '\n')
            content = content1.replace('&nbsp;', ' ')
            fw.write(content)
