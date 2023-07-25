import requests

cookies = {
    'd_c0': 'AJCYYIbxHRePTibbsmQRmq3AFEYwBSFdLn0=|1689926462',
}

headers = {

    'x-zse-93': '101_3_3.0',
    'x-zse-96': '2.0_HW+2PBfk/9=MTzhJi9aFLjcJ==N8vw7J2PWgqDdzn=4+HSAsWnxKoAZIgaar+/Re',
}

params = {
    'gk_version': 'gz-gaokao',
    't': 'general',
    'q': '结账时发现东西很贵咋办',
    'correction': '1',
    'offset': '0',
    'limit': '20',
    'filter_fields': '',
    'lc_idx': '0',
    'show_all_topics': '0',
    'search_source': 'Normal',
}

response = requests.get('https://www.zhihu.com/api/v4/search_v3', params=params, cookies=cookies, headers=headers)
print(response.json())