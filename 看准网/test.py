# import json
#
# import requests
# import re
# cookies = {
#     '__c': '1691380457',
#     '__lh_v1': '2_10402',
#     'wd_guid': '7e38d16f-bd1e-456e-aace-a03ba478b1a7',
#     '__g': '-',
#     'historyState': 'state',
#     'W_CITY_S_V': '7',
#     'Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e': '1691380453',
#     'AB_T': 'abvb',
#     'SL_G_WPT_TO': 'zh-CN',
#     'SL_GWPT_Show_Hide_tmp': '1',
#     'SL_wptGlobTipTmp': '1',
#     'R_SCH_CY_V': '10402',
#     '__l': 'r=&l=%2Fapi_to%2Fci.json%3Fb%3DIvfbQ5lpXSP0rYBQwpGphfe7zAYs9Ia-h65Kq4bPEd1voCh8o4LC-k69dlUKTO7Ty_6X_-BBYbI8qML4fZh-cVt4OMpK5w_YdaIOerzx38dQjNUY-JMs6mfXIhVrK7G4PSPgk8SHiXy7CaIvUyljqw~~%26kiv%3D2QgGWL9lKJwumd2V',
#     'Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e': '1691388292',
#     'pageType': '2',
#     'lasturl': '"https://www.kanzhun.com/firm/interview/1nR-298~.html?ka=com-interview-module-expose"',
#     'wbrwsid': '37620371',
#     '__a': '97571704.1691380457..1691380457.6.1.6.6',
# }
#
# headers = {
#     'authority': 'www.kanzhun.com',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     'cache-control': 'no-cache',
#     # 'cookie': '__c=1691380457; __lh_v1=2_10402; wd_guid=7e38d16f-bd1e-456e-aace-a03ba478b1a7; __g=-; historyState=state; W_CITY_S_V=7; Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e=1691380453; AB_T=abvb; SL_G_WPT_TO=zh-CN; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; R_SCH_CY_V=10402; __l=r=&l=%2Fapi_to%2Fci.json%3Fb%3DIvfbQ5lpXSP0rYBQwpGphfe7zAYs9Ia-h65Kq4bPEd1voCh8o4LC-k69dlUKTO7Ty_6X_-BBYbI8qML4fZh-cVt4OMpK5w_YdaIOerzx38dQjNUY-JMs6mfXIhVrK7G4PSPgk8SHiXy7CaIvUyljqw~~%26kiv%3D2QgGWL9lKJwumd2V; Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e=1691388292; pageType=2; lasturl="https://www.kanzhun.com/firm/interview/1nR-298~.html?ka=com-interview-module-expose"; wbrwsid=37620371; __a=97571704.1691380457..1691380457.6.1.6.6',
#     'pragma': 'no-cache',
#     'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'none',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
# }
#
# params = {
#     'ka': 'com-interview-module-expose',
# }
#
# response = requests.get('https://www.kanzhun.com/firm/interview/1nR-298~.html', params=params,  headers=headers)
# data = re.findall(r'window.context = (.*?)</script>', response.text)
# data = json.loads(data[0])
# a = 1

# Path: 看准网\test.py
import execjs
import requests
decrypt = open('decrypt.js', encoding='utf-8').read()
decrypt_exc = execjs.compile(decrypt)
encrypt = open('encrypt.js', encoding='utf-8').read()
encrypt_exc = execjs.compile(encrypt)
key = encrypt_exc.call('p')
data = {
    "encCompanyId": "1nR-298~",
    "positionId": 3626,
    "cityCode": "",
    "sortType": 1,
    "keywordId": "",
    "pageNum": 1
}
parmas = {
    "b": encrypt_exc.call('l', data, key),
    "kiv": key
}
headers = {
    'authority': 'www.kanzhun.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    # 'cookie': '__c=1691380457; __lh_v1=2_10402; wd_guid=7e38d16f-bd1e-456e-aace-a03ba478b1a7; __g=-; historyState=state; W_CITY_S_V=7; Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e=1691380453; AB_T=abvb; SL_G_WPT_TO=zh-CN; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; R_SCH_CY_V=10402; __l=r=&l=%2Fapi_to%2Fci.json%3Fb%3DIvfbQ5lpXSP0rYBQwpGphfe7zAYs9Ia-h65Kq4bPEd1voCh8o4LC-k69dlUKTO7Ty_6X_-BBYbI8qML4fZh-cVt4OMpK5w_YdaIOerzx38dQjNUY-JMs6mfXIhVrK7G4PSPgk8SHiXy7CaIvUyljqw~~%26kiv%3D2QgGWL9lKJwumd2V; pageType=2; lasturl="https://www.kanzhun.com/firm/interview/1nR-298~.html?ka=com-interview-module-expose"; __a=97571704.1691380457..1691380457.19.1.19.19; Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e=1691394159',
    'href': 'https://www.kanzhun.com/firm/interview/j24_1nR-298~.html?ka=com-interview-module-expose',
    'pragma': 'no-cache',
    'referer': 'https://www.kanzhun.com/firm/interview/j24_1nR-298~.html?ka=com-interview-module-expose',
    'reqsource': 'fe',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
encrypt_data = requests.get('https://www.kanzhun.com/api_to/ci.json', params=parmas, headers=headers).text

decrypt_data = decrypt_exc.call('c', encrypt_data, key)
print(decrypt_data)
