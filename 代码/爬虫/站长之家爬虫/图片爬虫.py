"""
基于正则re模块分析数据
"""
import re
import os
import requests

from utils.header import get_ua

url = 'https://sc.chinaz.com/tupian/shuaigetupian.html'
headers = {
    'User-Agent': get_ua()
}

if os.path.exists('mn.html'):
    with open('tupian.html', encoding='utf-8') as f:
        html = f.read()
else:
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    assert resp.status_code == 200
    html = resp.text
    with open('tupian.html', 'w', encoding=resp.encoding) as f:
        f.write(html)
# print(html)
# compile = re.compile(r'<img src="(.*?)" alt="(.*?)"> ')
# compile = re.compile(r'<img src="(.*?)" style="(.*?)" data-original="(.*?)" class="(.*?)" alt="(.*?)">')
compile = re.compile(r'<img\b[^>]*>')
imgs = compile.findall(html)
print(len(imgs),imgs,sep='\n')
