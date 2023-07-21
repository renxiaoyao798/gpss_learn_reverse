import execjs
import requests
import time
encryp_code = open('test.js', encoding='utf-8').read()
encryp_call = execjs.compile(encryp_code)
# 获取13位时间戳
timestamp = str(int(time.time() * 1000))
encrypt_time = timestamp + "9527" + timestamp[0:6]
code = encryp_call.call('encryp', encrypt_time)
params = {
    'pages': '1,1',
    'sizes': '100,100',
    'subject': 'market_cap',
    'language': 'en_US',
    'timestamp': timestamp,
    'code': code,
    'platform': 'web_pc',
    'v': '0.1.0',
    'legal_currency': 'USD',
    'international': '1',
}

response = requests.get('https://api.mytokenapi.com/ticker/currencylistforall', params=params)
print(response.json())