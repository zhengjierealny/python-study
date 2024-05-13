from urllib.request import urlopen, urlretrieve, Request
from urllib.parse import quote

import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def search_baidu(wd='千峰'):
    # 网络资源的接口url
    url = 'https://www.baidu.com/s?wd=%s'
    # 生成请求对象，封装请求的url和头header
    request = Request(url % quote(wd),
                      headers={
                          'Cookie': 'BAIDUID_BFESS=238139BFA01152047DAF3F3097C366E4:FG=1; __bid_n=1841284baca85b70fc4207; FPTOKEN=eaE6CP8igB9c/PAy3kfx/kkQUM0qri8ZU8F9W9mH1MJHYedgT6t9deFGH5XGYB2TDKowLueEgSKZiyPgQ3QaKeJeoJVMEMjoYGk2Y1Dudb5N3UywkbgllJyq2+krpsAo/7NcTlcbHJnoZEPOrcaR7GwTQzGygxcHdCd+RXAGwItsoENpyQMwZTZ+de4PG7L7hpOeoMh1SivOJ3zyqs0i2Ck3lAnhczNanLBtsrpKUulAh3Lyx3ThmPwdxdx4F19uScIvFBZgy5wEE5lZ9qdiOZkBMFHkZoD/ZLUS65hVO/Ai5SBUU3GpWzl5abtd5rbtT4c+hWwKlHUXyK+EyQmkTsKo0egLpuG70pJSVIiUiKGxNSKuXuqkGwQzv7ooMW4HhHS2G40TNlDuYiIEBKk5Nx6sG4EX2HncJ+ejaC8/PccXQ+bJlngHDqiNaKFASGHU|RtwGDfJf5vBVIPR1scWVJJ0D56QDes5t/luw0gvuXBw=|10|2f74ae8fe8ed2de2511c603a44ccce85; BAIDU_WISE_UID=wapp_1689332135655_483; BDUSS=lM4WjNkNUxHdW9uMG5PQ21GY1N4OUpCTGJWaWF1TFY1eVJGemFEeWJpNVF5VlZsSVFBQUFBJCQAAAAAAAAAAAEAAABTrivTs6y8tuDruf7g67n-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFA8LmVQPC5la; BDUSS_BFESS=lM4WjNkNUxHdW9uMG5PQ21GY1N4OUpCTGJWaWF1TFY1eVJGemFEeWJpNVF5VlZsSVFBQUFBJCQAAAAAAAAAAAEAAABTrivTs6y8tuDruf7g67n-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFA8LmVQPC5la; ZFY=Mt5PsI0wfdj4NpQSBW1xxfIAvdiT0:AAcgjxblUtQwl4:C; MCITY=-179%3A; PSTM=1712822787; H_PS_PSSID=40366_40376_40446_40300_40458_40457_39662_40510_40512_40397_60024_60036_60048; BIDUPSID=238139BFA0115204B70B976F6604E805; BA_HECTOR=ah2h0125a1000g2k2k01240k8ji6nq1j1f6f21t; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=3; delPer=0; BCLID=3959585062727078173; BCLID_BFESS=3959585062727078173; BDSFRCVID=_JIOJexroG3MGBvtQvoZEHtYogKK0gOTDYrEOwXPsp3LGJLVFIsMEG0Pt8yb6FI-jphvogKKKgOTHICtdm02LL1aokIQKJKJG3jGtf8g0M5; BDSFRCVID_BFESS=_JIOJexroG3MGBvtQvoZEHtYogKK0gOTDYrEOwXPsp3LGJLVFIsMEG0Pt8yb6FI-jphvogKKKgOTHICtdm02LL1aokIQKJKJG3jGtf8g0M5; H_BDCLCKID_SF=tJkfoIDhfIvDqTrP-trf5DCShUFs346iB2Q-XPoO3KOYspoC5hQ-hPFkyhOk2-biWbRM2Mbgy4op8P3y0bb2DUA1y4vp0fceBmTxoUJ2fPTDMlQVqt62MbKebPRiB-b9QgbA5-beaCtK8h4l-tnOyq_Uy4RZ05JB35nhVn0MBCK0hC06D5Lae5PVKgTa54cbb4o2WbCQXhcz8pcN2b5oQTtIQP5q-poqaaQ4aPbwab3vOIJTXpOUWJDkXpJvQnJjt2JxaqRC3qT58q5jDh3MebFVj4jAe4Tj2Tcy0hvcWb3cShnVLnOfhjOXX-kD54RWWG6iaqvF3KO8sPbIe-t2XjQh-p52f6LDtnAq3J; H_BDCLCKID_SF_BFESS=tJkfoIDhfIvDqTrP-trf5DCShUFs346iB2Q-XPoO3KOYspoC5hQ-hPFkyhOk2-biWbRM2Mbgy4op8P3y0bb2DUA1y4vp0fceBmTxoUJ2fPTDMlQVqt62MbKebPRiB-b9QgbA5-beaCtK8h4l-tnOyq_Uy4RZ05JB35nhVn0MBCK0hC06D5Lae5PVKgTa54cbb4o2WbCQXhcz8pcN2b5oQTtIQP5q-poqaaQ4aPbwab3vOIJTXpOUWJDkXpJvQnJjt2JxaqRC3qT58q5jDh3MebFVj4jAe4Tj2Tcy0hvcWb3cShnVLnOfhjOXX-kD54RWWG6iaqvF3KO8sPbIe-t2XjQh-p52f6LDtnAq3J',
                          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0'
                                        ' Safari/537.36 Edg/123.0.0.0'
                      })
    response = urlopen(request)  # 发起请求
    assert response.code == 200
    print('请求成功')

    # 读取响应数据
    bytes_ = response.read()
    with open('%s.html' % wd, 'wb') as file:
        file.write(bytes_)


def download_img(url):
    # 从url中获取文件名
    filename = url[url.rfind('/') + 1:]
    req = Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0'
                      ' Safari/537.36 Edg/123.0.0.0'
    })
    # urlretrieve(url, filename)
    resq = urlopen(req)
    with open(filename, 'wb') as file:
        file.write(resq.read())

    print(f'下载成功 {filename}')


if __name__ == '__main__':
    # search_baidu()
    download_img('https://img.dytt89.com/d/file/html/gndy/jddy/2024-04-11/5e5608dcafc0a985dc9e01316cc9a218.jpg')
