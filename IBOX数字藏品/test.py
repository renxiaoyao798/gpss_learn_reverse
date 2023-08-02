import execjs
import requests

aes_code = open('ibox_aes.js', encoding='utf-8').read()
aes = execjs.compile(aes_code)
rsa_code = open('ibox_rsa.js', encoding='utf-8').read()
rsa = execjs.compile(rsa_code)

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'JSESSIONID=0a099dda16907856602078198edc210c8b46b3f715579ff0f8cdd270eb0a96; SL_G_WPT_TO=zh-CN; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218996f3f1ea102-0bb3841bcff5e3-26031d51-2073600-18996f3f1eb1e74%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg5OTZmM2YxZWExMDItMGJiMzg0MWJjZmY1ZTMtMjYwMzFkNTEtMjA3MzYwMC0xODk5NmYzZjFlYjFlNzQifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218996f3f1ea102-0bb3841bcff5e3-26031d51-2073600-18996f3f1eb1e74%22%7D; acw_tc=0bdd344e16909637964352518e2d92c6067bec046a6bc1a84850cbb27c1799',
    'IB-DEVICE-ID': '5cef47e7ad8148798f2b86ace0f00b07',
    'IB-PLATFORM-TYPE': 'web',
    'IB-TRANS-ID': '361f36f5a4bb45399a1706463b3dba38',
    'Origin': 'https://www.ibox.art',
    'Pragma': 'no-cache',
    'Referer': 'https://www.ibox.art/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-cloudbase-phone': '',
}

params = {
    'type': '0',
    'origin': '0',
    'sort': '0',
    'page': '1',
    'pageSize': '50',
}

response = requests.get(
    'https://api-h5.ibox.art/nft-mall-web/v1.2/nft/product/getResellList',
    params=params,
    headers=headers,
)
if response.status_code == 200:
    data = response.json().get('data')
    encryptKey = response.json().get('encryptKey')
    key = rsa.call('decodeRSA', encryptKey)
    data = aes.call('aes', data, key)
    print(data)