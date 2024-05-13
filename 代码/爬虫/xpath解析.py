import requests
from lxml import etree


class RequestError(Exception):
    # 请求异常
    pass


class ParseError(Exception):
    # 解析异常
    pass


def get(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        print(resp.text)
        parse(resp.text)
    else:
        raise RequestError('请求失败')


def parse(html):
    # 使用xpath解析
    root = etree.HTML(html)  # ELement元素对象
    divs = root.xpath('//div[@class="zu-itemmod clearfix"]')
    print(divs)
    for div in divs:
        cover_url = div.xpath('.//a/img/@src').extract()[0]
        title = div.xpath('.//div/h3/a/b/text()').extract()[0]
        print(cover_url, title)


if __name__ == '__main__':
    get('https://hz.zu.anjuke.com/fangyuan/linanq/')
