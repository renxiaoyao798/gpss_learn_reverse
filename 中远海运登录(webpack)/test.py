import requests

cookies = {
    'HMF_CI': 'eade3cd2ba8de2af5bb5ce3c2d47c7a5601db16dba3b2107abfbd8954f13b964a537125f12b2fb39b5c7519f860b2ff24dadf405d8dae5d941c0b262aa9f66df4a',
    'SL_G_WPT_TO': 'zh-CN',
    'django_language': 'zh-cn',
    'sessionid': 'onhz06qdnxr6nxm7prqvz419bmdgh80w',
    'SL_GWPT_Show_Hide_tmp': '1',
    'SL_wptGlobTipTmp': '1',
    'cookiePolicy': 'Accepted',
    'cookiePreference': 'Accepted',
    'Hm_lvt_d16e4336470e6b4d88aa16ff927d7daf': '1690276182',
    'unified_account_switch': 'true',
    'FECW': '346ed6dd4e474ae409617d84449486574213db9e99e07a24acc56a40656bb5d4b60c356fccfe5f63af862ecde04fc28b638cbd6e8483eda2124aa0059667abf7a87ecd0febeb842479f6c4f11b7923ab4c',
    'FECN': '346ed6dd4e474ae409617d84449486574213db9e99e07a24acc56a40656bb5d4ad9e2481eec861349a3f8db79fc5544471194d81544250dabe18f3286b2139216dca63352d88a1f77eabf18d771d12676c',
    'session': 'Ld3ojXa9gTP-TTj0umh21A..|1690284905|jFqkIgnVX62NafkVT_eicpEUyIU.',
    'ECTIMGCAPTCHA': 'c5fbb1f0-f89d-435a-abba-a7cd4412d957',
    'Hm_lpvt_d16e4336470e6b4d88aa16ff927d7daf': '1690281472',
    'FECA': '2oAvnR4mw33VNFa/7kr0M0bsgftcy5b/W4IT+n7TSjIucMMQRmiv1okcAttADYjchTJj8Vy/k1Lek7gnCKWgw3mw9OcFhw6mp1zsdgRRPh0oxYjNatHb333rxkhEO7uqGcVIDFVwklPpgHwzW2H3b8xVSluviitT5p0qoK2iVh8XnESgUa+letrNwAgYVlfzAc',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'HMF_CI=eade3cd2ba8de2af5bb5ce3c2d47c7a5601db16dba3b2107abfbd8954f13b964a537125f12b2fb39b5c7519f860b2ff24dadf405d8dae5d941c0b262aa9f66df4a; SL_G_WPT_TO=zh-CN; django_language=zh-cn; sessionid=onhz06qdnxr6nxm7prqvz419bmdgh80w; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; cookiePolicy=Accepted; cookiePreference=Accepted; Hm_lvt_d16e4336470e6b4d88aa16ff927d7daf=1690276182; unified_account_switch=true; FECW=346ed6dd4e474ae409617d84449486574213db9e99e07a24acc56a40656bb5d4b60c356fccfe5f63af862ecde04fc28b638cbd6e8483eda2124aa0059667abf7a87ecd0febeb842479f6c4f11b7923ab4c; FECN=346ed6dd4e474ae409617d84449486574213db9e99e07a24acc56a40656bb5d4ad9e2481eec861349a3f8db79fc5544471194d81544250dabe18f3286b2139216dca63352d88a1f77eabf18d771d12676c; session=Ld3ojXa9gTP-TTj0umh21A..|1690284905|jFqkIgnVX62NafkVT_eicpEUyIU.; ECTIMGCAPTCHA=c5fbb1f0-f89d-435a-abba-a7cd4412d957; Hm_lpvt_d16e4336470e6b4d88aa16ff927d7daf=1690281472; FECA=2oAvnR4mw33VNFa/7kr0M0bsgftcy5b/W4IT+n7TSjIucMMQRmiv1okcAttADYjchTJj8Vy/k1Lek7gnCKWgw3mw9OcFhw6mp1zsdgRRPh0oxYjNatHb333rxkhEO7uqGcVIDFVwklPpgHwzW2H3b8xVSluviitT5p0qoK2iVh8XnESgUa+letrNwAgYVlfzAc',
    'ECTIMGCAPTCHA': 'c5fbb1f0-f89d-435a-abba-a7cd4412d957',
    'Origin': 'https://synconhub.coscoshipping.com',
    'Pragma': 'no-cache',
    'Referer': 'https://synconhub.coscoshipping.com/bid/?language=zh',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Auth-Token': 'undefined',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'username': '12345678910',
    'password': 'TxPd02fei+3lY+bnkqbxabQYwGPnx7wrBzTinWUp6oO7U/SOZYo51OSbr/uBql5Z+5kCsrRq5LTMHFYai3ZUTmSOF3nLuFIrA+MhL9ITNvRR9oNIWXnyJtcWe2reQMPjtpZlOT450EcUHiw2tlO6fJfIgLnUFUl+hiXtaNuDU4hdBcz8VZrApk+TYAe/Vq+7QRqLTNcBM2+rN8iXB91GMoQFWC+eHbrGot1sWhnHfIiQcKBqO31mzsjxhUrqHcTdPUA7y+OYWX8T5yATCznDQX9uHqHRwb3+/Vs6nYpIDgNa/erY6K98ybS/9FL7vX13PjYBzqnJIvZd21ejxlVxyA==',
}

response = requests.post(
    'https://synconhub.coscoshipping.com/api/bid/user/login',
    # params=params,
    # cookies=cookies,
    # headers=headers,
    json=json_data,
)

print(response.json())