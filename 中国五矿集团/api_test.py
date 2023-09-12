import requests

cookies = {
    'SUNWAY-ESCM-COOKIE': '4518fb1d-b3fe-4868-a5fb-2ab604739704',
    '__jsluid_s': 'feb208ef8ee2ceea8991c682a9f6f549',
    'JSESSIONID': '1F877A838DAD79D47EDAAF12BBC9C1B2',
    'SL_G_WPT_TO': 'zh-CN',
    'SL_GWPT_Show_Hide_tmp': '1',
    'SL_wptGlobTipTmp': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

json_data = {
    'param': 'qPlFIQzTxJeosjo1ByHdbdKs0KXmWEPh8HpWZIHS1uLNrc2DZfKhOULAu5H0BOimy3XaXi/Zt/VMPVthXxIvElT/UxwBcXkkJ4zmKEsU3mPpa9Cjzvbr8ZMfuXuK61yYr+B5DlrwXzGHFIFWhZJpQsLPdXWaUQ65EqIwfzd/ID+L+oGjtVo8VMPzEhLEJgtbAdDkq7UFjGFhOeFgsLYj70y39zhBcKPswYUuO7UgGH3vxVuw56M6/3H7qOAU96yAIsI926q9Ie+poZDfk4ZPCo+U94dVi2HxBbUmH0j1Cu96m93pyL3SJ+/Zxkjk/M3bGSK6muAJNESXP6cirvLlGDCIljLrB/yc9HH6hx8XjRGt51ygF/T6xdWtBXYuFwMfKfRB10ULcx49lUBEQ1SMR1XSVgVNA3ccknnbgTou9QTVyj2MaKDXZP68Bc6114gLLKvTEOwHyYy2homC7vINH1IHjpwVOy4E36Xen7pv9PhZv14dnn0H7RlUTley3uIjBlPU+LgugwzmIW5r2L+104uvglwjWQ+o9zlJfkic2Y8mWTP0G0UsFTUeEEregE/lKs03ddmtRStZv+zaVKHDKQ9IDgogTIlZO5nbMowpHPgfzLxi7q0JUGl067WK3lDGmn/+pVUCxZDCUjOo8Rq9ukwcoD5oycd0SbFHytpIvEA=',
}

response = requests.post(
    'https://ec.minmetals.com.cn/open/homepage/zbs/by-lx-page',
    headers=headers,
    json=json_data,
)
print(response.text)
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"param":"qPlFIQzTxJeosjo1ByHdbdKs0KXmWEPh8HpWZIHS1uLNrc2DZfKhOULAu5H0BOimy3XaXi/Zt/VMPVthXxIvElT/UxwBcXkkJ4zmKEsU3mPpa9Cjzvbr8ZMfuXuK61yYr+B5DlrwXzGHFIFWhZJpQsLPdXWaUQ65EqIwfzd/ID+L+oGjtVo8VMPzEhLEJgtbAdDkq7UFjGFhOeFgsLYj70y39zhBcKPswYUuO7UgGH3vxVuw56M6/3H7qOAU96yAIsI926q9Ie+poZDfk4ZPCo+U94dVi2HxBbUmH0j1Cu96m93pyL3SJ+/Zxkjk/M3bGSK6muAJNESXP6cirvLlGDCIljLrB/yc9HH6hx8XjRGt51ygF/T6xdWtBXYuFwMfKfRB10ULcx49lUBEQ1SMR1XSVgVNA3ccknnbgTou9QTVyj2MaKDXZP68Bc6114gLLKvTEOwHyYy2homC7vINH1IHjpwVOy4E36Xen7pv9PhZv14dnn0H7RlUTley3uIjBlPU+LgugwzmIW5r2L+104uvglwjWQ+o9zlJfkic2Y8mWTP0G0UsFTUeEEregE/lKs03ddmtRStZv+zaVKHDKQ9IDgogTIlZO5nbMowpHPgfzLxi7q0JUGl067WK3lDGmn/+pVUCxZDCUjOo8Rq9ukwcoD5oycd0SbFHytpIvEA="}'
#response = requests.post('https://ec.minmetals.com.cn/open/homepage/zbs/by-lx-page', cookies=cookies, headers=headers, data=data)