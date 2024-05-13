import os.path
import time
import uuid
from csv import DictWriter
import requests
from lxml import etree

from utils import header
from mysql import MysqlTool

import random

# user_agents = [
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.160 Safari/537.36',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
# ]
#
#
# def get_ua():
#     return random.choice(user_agents)


msql = MysqlTool()


def itempipeline(item):
    print(item)
    # values占位字符串：%(id)s,%(name)s,%(author)s,%(content)s,%(tags)s
    sql = 'insert into dushuwang(%s) values(%s)'
    fields = ','.join(item.keys())
    value_palaceholds = ','.join(['%%(%s)s' % key for key in item])
    with msql as db:
        db.execute(sql % (fields, value_palaceholds), item)


has_header = os.path.exists('dushuwang.csv')  # 是否第一次写入csv的头
header_fields = ('id', 'name', 'author', 'content')


def itempipeline4csv(item):
    global has_header
    with open('dushuwang.csv', 'a') as f:
        writer = DictWriter(f, fieldnames=header_fields)
        if not has_header:
            writer.writeheader()  # 写入标题
            has_header = True
        writer.writerow(item)  # 写入数据


base_url = 'https://so.gushiwen.cn'


def parse(html):
    root = etree.HTML(html)  # 获取html的根元素
    divs = root.xpath('//div[@class="left"]/div[@id="leftZhankai"]/div[@class="sons"]')
    print(len(divs))
    item = {}
    for div in divs:
        item['id'] = uuid.uuid4().hex
        item['name'] = div.xpath('./div[@class="cont"]//p[1]//text()')[0]
        item['author'] = ' '.join(div.xpath('.//p[2]/a/text()'))
        item['content'] = ''.join(div.xpath('.//div[@class="contson"]/text()'))
        # tags = ','.join(div.xpath('./div[last()]/a/text()'))
        # print(name, author, content)
        # itempipeline(item)  # 写入数据库
        itempipeline4csv(item)  # 写入文件
    next_url = base_url + root.xpath('//a[@class="amore"]/@href')[0]
    print(next_url)
    time.sleep(1)
    get(next_url)
#https://so.gushiwen.cn/shiwens/default.aspx?page=2&tstr=&astr=&cstr=&xstr=


def get(url):
    resp = requests.get(url, headers={'User-Agent': header.get_ua()})

    if resp.status_code == 200:
        parse(resp.text)
    else:
        raise Exception('请求失败')


if __name__ == '__main__':
    get('https://so.gushiwen.cn/shiwens/')
