import requests

url = 'https://hz.zu.anjuke.com/fangyuan/'


# resp = requests.get(url, params={'from': 'linanq'})

def download(url: str) -> str:
    # resp = requests.get(url, params={'from': 'linanq'})
    resp = requests.request('get', url, params={'from': 'linanq'})
    if resp.status_code == 200:
        return resp.text
    return '失败'


def get_douban_json():
    url = 'https://movie.douban.com/top250'  # post方法

    # page = 2
    # start = (page-1) * 20
    # limit = 20
    data = {
        'start': 1,
        'limit': 20,

    }
    params = {
        'type': 5,
        'interval_id': '100%3A90&',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
    }

    resp = requests.post(url, params=params, data=data, headers=headers)
    assert resp.status_code == 200
    if 'application/json' in resp.headers['content-type']:
        return resp.json()
    return resp.text


# r = download(url)
# print(r)
r = get_douban_json()
print(r)
