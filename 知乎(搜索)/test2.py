import execjs
import requests
from urllib.parse import urlencode
ZhiHuFunction = open('ZhiHuFunction.js', encoding='utf-8').read()
ZhiHuFunction_exc = execjs.compile(ZhiHuFunction)
cookies = {
    'd_c0': 'AMDWa-7nIRePTpKNqMyPT-fcTBwDvAxRMY4=|1690192383',
}
# TODO: "未完成"
headers = {

    'x-zse-93': '101_3_3.0',
    'x-zse-96': '2.0_N7CUducBG7p7dcVzxan8N=7wqb94FcFcx52n/+sggpPgQoJvyNMOI0Ken73YPtLI',

}

params = {
    'gk_version': 'gz-gaokao',
    't': 'general',
    'q': '结账时发现东西很贵咋办',
    'correction': '1',
    'offset': '20',
    'limit': '20',
    'filter_fields': '',
    'lc_idx': '0',
    'show_all_topics': '0',
    'search_source': 'Normal',
}
params_url_encode = urlencode(params)

response = requests.get('https://www.zhihu.com/api/v4/search_v3', params=params, cookies=cookies, headers=headers)
a = response.json()['data']
print(response.json())