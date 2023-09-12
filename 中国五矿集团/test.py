import json
import time
import execjs
import requests
import hashlib

session = requests.session()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',

}


def get_public():
    response = session.post('https://ec.minmetals.com.cn/open/homepage/public', headers=headers)
    return response.text


def get_param():
    param = {
        "inviteMethod": "",
        "businessClassfication": "",
        "mc": "",
        "lx": "ZBGG",
        "dwmc": "",
        "pageIndex": 1
    }
    dump_data = json.dumps(param).replace(" ", "")
    sign = hashlib.md5(dump_data.encode()).hexdigest()  # 将字符串编码并进行 MD5 加密
    timestamp = str(time.time())[:14].replace(".", "")
    param['sign'] = sign
    param['timeStamp'] = int(timestamp)
    return json.dumps(param).replace(" ", "")

def encrypt(param, public):
    RSA_code = open('RSA.js', encoding='utf-8').read()
    RSA = execjs.compile(RSA_code)
    print(param)
    param = RSA.call('encryptLong', param, public)
    json_data = {
        'param': param,
    }
    response = session.post(
        'https://ec.minmetals.com.cn/open/homepage/zbs/by-lx-page',
        headers=headers,
        json=json_data,
    )

    print(response.text)


if __name__ == '__main__':
    public = get_public()
    param = get_param()
    encrypt(param, public)