import requests

Strhtml = requests.get(url='https://hao.360.com/?src=lm&ls=n76150e7e9b')  # GET方式，获取网页数据
print(Strhtml.text)
