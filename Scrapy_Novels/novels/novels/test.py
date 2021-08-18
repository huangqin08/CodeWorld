import re

import requests
from bs4 import BeautifulSoup
from lxml import etree


# 获取资源
def get_resource(url, params=None, flag='html'):
    headers = {
        'Host': 'www.biquku.la',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'
    }
    response = requests.get(url=url, params=params, headers=headers)
    if response.status_code == 200:
        if flag == 'html':
            response.encoding = 'utf-8'
            return response.text
        elif flag == 'media':
            return response.content
    else:
        print('获取资源有误！')


# 获取所有小说
def get_novels(url):
    html = get_resource(url)
    # 方式一：用bs4
    soup = BeautifulSoup(html, 'lxml')
    li_list = soup.find_all('div', attrs={'class': 'novellist'})
    # 方式二：用xpath
    # e = etree.HTML(html)
    # li_list=e.xpath('//*[@id="main"]/div[1]/ul/li')
    novel_list = []
    for li in li_list:
        a_tag = li.select_one('a')
        novel_link = a_tag.get('href')
        novel_name = a_tag.text
        novel = [novel_link, novel_name]
        novel_list.append(novel)
    return novel_list


# 获取每本书的详情
def get_novel_detail(url, novel):
    html = get_resource(url=url)
    soup = BeautifulSoup(html, 'lxml')
    # 获取小说封面
    div_tag = soup.select_one('#fmimg')
    novle_img = div_tag.select_one('img').get('src')
    novel.append(novle_img)
    # 获取小说作者
    div_tag1 = soup.select_one('#info')
    author1 = div_tag1.select_one('p').text
    author2 = author1.split('：', 1)
    novle_author = author2[1]
    novel.append(novle_author)
    # 更新时间
    e = etree.HTML(html)
    updatetime = e.xpath('string(//*[@id="info"]/p[3])')
    updatetime1 = updatetime.split('：')
    novle_updatetime = updatetime1[1]
    novel.append(novle_updatetime)
    # 获取简介
    div_tag2 = soup.select_one('#intro')
    decs = div_tag2.select_one('p').text
    novel.append(decs)
    return novel


# 获取每本书的所有章节
def get_chapter(url, novel):
    html = get_resource(url=url)
    e = etree.HTML(html)
    chapter_list = []
    dd_list = e.xpath('//*[@id="list"]/dl/dd')
    for dd in dd_list:
        try:
            chapter_name = dd.xpath('a/text()')[0]
            chapter_link = dd.xpath('a/@href')[0]
            chapter = [chapter_name, chapter_link]
        except:
            continue
        else:
            chapter_list.append(chapter)
    return chapter_list


# 获取章节详情
def get_chapter_detail(url):
    html = get_resource(url)
    soup = BeautifulSoup(html, 'lxml')
    div_content = soup.select_one('#content').text
    content = re.sub(r'\s{4,}', '\r\n\t', div_content)
    print(content)


if __name__ == '__main__':
    url = 'http://www.biquku.la/xiaoshuodaquan/'
    novel_list = get_novels(url)  # [['链接','书名'],[],[]]
    # print(novel_list)
    # for novel in novel_list:
    novel_url = novel_list[0][0]
    novel = novel_list[0]
    novel_detail = get_novel_detail(novel_url, novel)  # ['链接','书名','封面图','作者','更新时间','简介']

    chapter_list = get_chapter(novel_url, novel)  # [['章节名','链接'],[],[],[]]
    # for chapter in chapter_list:
    chapter_url = novel_detail[0] + chapter_list[0][1]
    chapter_detail = get_chapter_detail(chapter_url)
