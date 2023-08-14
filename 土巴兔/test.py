import base64
import requests
import rsa

session = requests.session()
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'SL_G_WPT_TO=zh-CN; uid=CgoKUWTZ9ckQsWxGbsumAg==; act=freshen',
    'Origin': 'https://www.to8to.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.to8to.com/new_login.php',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
cookies = {
    'SL_G_WPT_TO': 'zh-CN',
    'uid': 'CgoKUWTZ9SAQsWxGbsgIAg==',
    'act': 'freshen',
}
def RSAString(text):
    publickeystr = """-----BEGIN PUBLIC KEY-----
    MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDhNhuAr4UjFv+cj99PbAQWWx9H
    X+3jSRThJqJdXkWUMFMTRay8EYRtPFIiwiOUU4gCh4ePMxiuZJWUBHe1waOkXEFc
    Kg17luhVqECsO+EOLhxa3yHoXA5HcSKlG85hNV3G4uQCr+C8SOE0vCGTnMdnEGmU
    nG1AGGe44YKy6XR4VwIDAQAB
    -----END PUBLIC KEY-----"""
    result = rsa.encrypt(text.encode('utf-8'),rsa.PublicKey.load_pkcs1_openssl_pem(publickeystr.encode('utf-8')))
    return requests.utils.quote(base64.b64encode(result).decode())

data = {
    'referer': 'https://www.to8to.com/',
    'msgCode': '',
    'val': RSAString('11111111111'),
    'password': RSAString('11111111'),
}

response = session.post('https://www.to8to.com/new_login.php',  headers=headers, data=data, cookies=cookies)
aa = session.get('https://www.to8to.com/my/', headers=headers)
print(aa.text)