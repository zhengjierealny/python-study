"""
复杂的GET请求，多页面请求下载
"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode

url = 'https://www.baidu.com/s?'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'Cookie': 'BAIDUID_BFESS=238139BFA01152047DAF3F3097C366E4:FG=1; __bid_n=1841284baca85b70fc4207; FPTOKEN=eaE6CP8igB9c/PAy3kfx/kkQUM0qri8ZU8F9W9mH1MJHYedgT6t9deFGH5XGYB2TDKowLueEgSKZiyPgQ3QaKeJeoJVMEMjoYGk2Y1Dudb5N3UywkbgllJyq2+krpsAo/7NcTlcbHJnoZEPOrcaR7GwTQzGygxcHdCd+RXAGwItsoENpyQMwZTZ+de4PG7L7hpOeoMh1SivOJ3zyqs0i2Ck3lAnhczNanLBtsrpKUulAh3Lyx3ThmPwdxdx4F19uScIvFBZgy5wEE5lZ9qdiOZkBMFHkZoD/ZLUS65hVO/Ai5SBUU3GpWzl5abtd5rbtT4c+hWwKlHUXyK+EyQmkTsKo0egLpuG70pJSVIiUiKGxNSKuXuqkGwQzv7ooMW4HhHS2G40TNlDuYiIEBKk5Nx6sG4EX2HncJ+ejaC8/PccXQ+bJlngHDqiNaKFASGHU|RtwGDfJf5vBVIPR1scWVJJ0D56QDes5t/luw0gvuXBw=|10|2f74ae8fe8ed2de2511c603a44ccce85; BAIDU_WISE_UID=wapp_1689332135655_483; BDUSS=lM4WjNkNUxHdW9uMG5PQ21GY1N4OUpCTGJWaWF1TFY1eVJGemFEeWJpNVF5VlZsSVFBQUFBJCQAAAAAAAAAAAEAAABTrivTs6y8tuDruf7g67n-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFA8LmVQPC5la; BDUSS_BFESS=lM4WjNkNUxHdW9uMG5PQ21GY1N4OUpCTGJWaWF1TFY1eVJGemFEeWJpNVF5VlZsSVFBQUFBJCQAAAAAAAAAAAEAAABTrivTs6y8tuDruf7g67n-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFA8LmVQPC5la; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1702609044; ZFY=Mt5PsI0wfdj4NpQSBW1xxfIAvdiT0:AAcgjxblUtQwl4:C; MCITY=-179%3A; PSTM=1712822787; H_PS_PSSID=40366_40376_40446_40300_40458_40457_39662_40510_40512_40397_60024_60036_60048; BIDUPSID=238139BFA0115204B70B976F6604E805; BA_HECTOR=ah2h0125a1000g2k2k01240k8ji6nq1j1f6f21t; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ab_sr=1.0.1_MmIyOTM2OTZlMTg1YzlkOTY2MzBkNTRhMmU4MmI3NDliNjZjMDM5OWY3NDgzNGFmYTkwZDY0MTE4OTVkZTJkY2I2ZGU5ZTgxZmFjNWI3MTdlZDY0YWU0YTkyNWZlMjJjYzUyNjA5ZGY0NTkyZTI0NjlkODcyZDVkODYxN2ViOTkwN2MzOTg2MDJiNzAyMTIxNzk5MjJlMmI4MjM5MDQ3NGQ4YzY4M2FmZTM2Y2Y4MTAyZjZjNGVjZGFlMGFmNDNkMzBlZDUyNmQzMDgxODQ3MmE1Yzg3MGYyZDM4NjMxOGU=; RT="z=1&dm=baidu.com&si=rnvoe647y6&ss=luw20k9b&sl=1&tt=169&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1ya"',

}
params = {
    'wd': '',
    'pn': 0
}


def pages_get(wd):
    params['wd'] = wd
    for page in range(1, 11):
        params['pn'] = (page - 1) * 10
        page_url = url + urlencode(params)
        resp = urlopen(Request(page_url, headers=header))

        assert resp.code == 200
        file_name = 'baidu_pages/%s-s%s.html' % (wd, page)
        with open(file_name, 'wb') as f:
            bytes_ = resp.read()
            f.write(bytes_)
            print(f'{file_name}写入成功')

    print('下载 %s 10页成功' % wd)


if __name__ == '__main__':
    print(pages_get('LOL'))


# 豆瓣电影排行页面
