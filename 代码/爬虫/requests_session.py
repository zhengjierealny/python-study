"""
图片验证码的打码
下载验证码
读取图片上验证码
登录
获取个人收藏
"""
import uuid

import requests
from lxml import etree

from utils.header import get_ua
from utils.chaojiying import rec_code

session = requests.session()


def download_code():
    resp = session.get('https://so.gushiwen.cn/RandCode.ashx',
                       headers={'User-Agent': get_ua()})
    with open('code.png', 'wb') as f:
        f.write(resp.content)


def get_code_str():
    download_code()
    return rec_code('code.png')


def login():
    resp = session.post('https://so.gushiwen.cn/user/login.aspx',
                        data={
                            'email': '2127475195@qq.com',
                            'pwd': 'hhhh123456',
                            'code': get_code_str()
                        })
    if resp.status_code == 200:
        collect()
    else:
        print('_' * 30)
        print(resp.text)


def collect():
    resp = session.get('https://so.gushiwen.cn/user/collect.aspx')
    parse(resp.text)


def parse(html):
    root = etree.HTML(html)  # 获取html的根元素
    divs = root.xpath('//div[@class="left"]/div[@class="sons"]/div[@class="cont"]')
    print(len(divs))
    item = {}
    for div in divs:
        item['id'] = uuid.uuid4().hex
        item['name'] = div.xpath('./a/text()')[0]
        item['author'] = ' '.join(div.xpath('./a/span//text()'))
        # item['content'] = ''.join(div.xpath('.//div[@class="contson"]/text()'))
        print(item)


if __name__ == '__main__':
    login()
