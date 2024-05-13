"""
模拟浏览器，增加不同的处理器Handler
"""

from urllib.request import HTTPHandler, build_opener
from collections import namedtuple

# 声明一个类 属性包含：headers->dict  code-> int text 文本 body 字节码等相关属性
Response = namedtuple('Response',
                      field_names=['headers', 'code', 'text', 'body', 'encoding'])


def get(url):
    opener = build_opener(HTTPHandler())
    resp = opener.open(url)

    headers = dict(resp.getheaders())
    try:
        encoding = headers['Content-Type'].split('=')[-1]
    except:
        encoding = 'utf-8'
    code = resp.code
    body = resp.read()
    text = body.decode(encoding)
    return Response(headers=headers,
                    encoding=encoding,
                    code=code,
                    body=body,
                    text=text)


if __name__ == '__main__':
    resp: Response = get('https://jd.com')
    print(resp.code)
    print(resp.text)
