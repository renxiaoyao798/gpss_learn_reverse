import json
from loguru import logger
import requests
import json
import execjs
from parsel import Selector
code = open('test.js', encoding='utf-8').read()
encseckey_exc = execjs.compile(code)
headers = {
    'authority': 'music.163.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'NMTID=00OkS-Cyps3mpNHW0m2nnYdxK8V47QAAAGJa-lRrw; _iuqxldmzr_=32; _ntes_nnid=76e6b50aa23014cc3337a3c7f237bd62,1689732600095; _ntes_nuid=76e6b50aa23014cc3337a3c7f237bd62; WEVNSM=1.0.0; WNMCID=vmbzji.1689732602479.01.0; SL_G_WPT_TO=zh-CN; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; WM_TID=HScNNhfVkNtBAVRVRReAxyja%2BNZ5mP3P; ntes_utid=tid._.vadNh47KS%252FFEU0BAUBLB0ziK6ZJpy3o4._.0; sDeviceId=YD-N1%2BvslyLYSFAVlUUBRKAligGoYjqHnGN; WM_NI=zFHtczRlPoit2LvqPtq%2BnSrFT0u%2Bj1Zvt0Tl4nPYrEfgdmGDffXCzx22BipmM7g3KMW%2FSq8UDCp48HsypTTrvHwxLYqcgZQ%2Fan46AMhGsVYJUBf8nsFO%2F4Rsd3vcLGGENGU%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed2f93f86bc848df345ba968ea7d14b839f9eadd16daaec9db7e45bf1b0fbd0dc2af0fea7c3b92aba9a8895e27292b4a090ec80f294ba92d380b3f5a2b4f14e98f0bbcce93b9aaabcd1d768f8b2a0baf14fa6b9ac8ec650a6ba98a4f974f2ee8e8af3678fe9a9d4ca4795f19d92bb5f889dc0d5bb44b1a7c0b5d77ab698b999cf53b3bda9bbd425a3b2fcd7c447ac99bdb7dc42979eaad9ed798691e1d5d179a8edba84cf4d859b82a8d837e2a3; JSESSIONID-WYYY=1P0p7xG6GaZ5Tc0wU5jFY1ibH%2B0mFz0gK32oNymIKmxrVPYxgiy1VuMQVfherSFBN6X20NRC11q9SxugzcoYTl7fWzF1SPnyYoizIpXYvk%5CvlUg5TaW8AxiO2yiYV%2Buba9%2FSqFjtmDrVOYQNTZOgxMfZoE%2BBeP9SROVnGgeHImJekxhk%3A1689829046470; playerid=86277018',
    'pragma': 'no-cache',
    'referer': 'https://music.163.com/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}


def get_music_toplist():
    response = requests.get('https://music.163.com/discover/toplist',  headers=headers)
    select = Selector(response.text)
    data = select.xpath('//textarea[@id="song-list-pre-data"]/text()').get()
    load_data = json.loads(data)
    result_data = []
    for i in load_data:
        id = i['id']
        name = i['name']
        artists = i['artists']
        author_list = []
        for j in artists:
            author_list.append(j['name'])
        author = '、'.join(author_list)
        result_data.append({'id': id, 'name': name, 'author': author})
    return result_data


def get_music_file(data):
    id = data['id']
    name = data['name']
    author = data['author']
    encseckey_data = {
            'ids': f'[{id}]',
            'level': 'standard',
            'encodeType': 'aac',
            'csrf_token': ''
        }
    encseckey_result = encseckey_exc.call("gpss", encseckey_data)
    params = {
        'csrf_token': '',
    }
    data = {
        'params': encseckey_result['encText'],
        'encSecKey': encseckey_result['encSecKey'],
    }
    response = requests.post(
        'https://music.163.com/weapi/song/enhance/player/url/v1',
        params=params,
        data=data,
    )
    if response.json()['data'][0]['url']:
        logger.info(f"音乐id: {id}, 音乐名: {name}, 歌手:{author}, 音乐链接: {response.json()['data'][0]['url']}")
    else:
        logger.warning(f"音乐id: {id}, 音乐名: {name}, 歌手:{author}, 音乐链接: 无或者为vip音乐")


if __name__ == '__main__':
    music_data = get_music_toplist()
    for music_info in music_data:
        get_music_file(music_info)