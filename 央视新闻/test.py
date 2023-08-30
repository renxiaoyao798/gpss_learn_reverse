import base64

import requests
import hmac
import hashlib
import time


def encrypt_md5(text):
    # 创建MD5对象
    md5 = hashlib.md5()
    # 使用MD5对象的update()方法更新要加密的文本
    md5.update(text.encode('utf-8'))
    # 使用MD5对象的hexdigest()方法获取加密后的结果
    encrypted_text = md5.hexdigest()
    return encrypted_text

def get_headers(id):
    key = "emasgatewayh5"
    h = '20000009'
    g = str(int(time.time()))
    msg = "&".join(["&&", h, encrypt_md5(f"articleId={id}"), g, 'emas.feed.article.server.getArticle', '1.0.0', "&&&&"])
    m = hmac.new(bytes(key, encoding='utf-8'), bytes(msg, encoding='utf-8'), hashlib.sha256).hexdigest()
    headers = {
        "x-emas-gw-appkey": h,
        "x-emas-gw-pv": "6.1",
        "x-emas-gw-t": g,
        "x-emas-gw-sign": m
    }
    return headers

def convertTostring(base64Info):
    try:
        tmpBytes=base64.b64decode(base64Info)
        tmpStr=tmpBytes.decode()
        return tmpStr
    except Exception as e:
        print('异常：',e)

def main():
    params = {
        'articleId': '11164798948572306830',
    }
    headers = get_headers('11164798948572306830')
    response = requests.get(
        'https://emas-api.cctvnews.cctv.com/h5/emas.feed.article.server.getArticle/1.0.0',
        params=params,
        headers=headers,
    )
    print(response.json())
    if response.status_code == 200:
        resposne_result = response.json().get("response")
        tmpStr = convertTostring(resposne_result)
        print(tmpStr)


if __name__ == '__main__':
    main()