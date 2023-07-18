import execjs
import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Authorization': 'Basic cGlnOnBpZw==',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Content-Length': '0',
    # 'Cookie': 'Hm_lvt_c9a26c70c3ece738350147d4b957374d=1689672765; Hm_lpvt_c9a26c70c3ece738350147d4b957374d=1689672765; SL_G_WPT_TO=zh-CN; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1',
    'Origin': 'https://www.youshiyun.com.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://www.youshiyun.com.cn/login/index',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'isToken': 'false',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}



aes_code = open('aes.js', encoding='utf-8').read()
aes = execjs.compile(aes_code)
data = {
    "data": {
        "username": "13011111111",
        "password": "123456",
        "redomStr": ""
    },
    "key": "password.yunjy.y",
    "param": [
        "password"
    ]
}
password = aes.call('o', data).get('password')
params = {
    'username': '13011111111',
    'password': password,
    'grant_type': 'password',
    'scope': 'server',
}

response = requests.post('https://www.youshiyun.com.cn/api/auth/user/login', params=params, headers=headers)
print(response.json())