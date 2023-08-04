import requests
import execjs
import json
from loguru import logger
decrypt = open('decrypt.js', encoding='utf-8').read()
decrypt_exc = execjs.compile(decrypt)
headers = {
    'authority': 'api.zzzmh.cn',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': '__gads=ID=a0a456270f45d5ef-22c5ba9aaae200a9:T=1691118983:RT=1691119347:S=ALNI_MYRiA2TY6stgMeH7dwQpgoaDhtu3A; __gpi=UID=00000c26d29b4017:T=1691118983:RT=1691119347:S=ALNI_MZRf6ytU1pGzurBG6gfaD8eRc9xTA; SL_G_WPT_TO=zh-CN; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1',
    'pragma': 'no-cache',
    'referer': 'https://bz.zzzmh.cn/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}
json_data = {
    'size': 24,
    'current': 4,
    'sort': 0,
    'category': 0,
    'resolution': 0,
    'color': 0,
    'categoryId': 0,
    'ratio': 0,
}
session = requests.session()
session.headers = headers
response = session.post('https://api.zzzmh.cn/bz/v3/getData', json=json_data)
if response.status_code == 200:
    result = response.json().get('result')
    image_list = json.loads(decrypt_exc.call('get_image_id', result))
    for info in image_list.get('list'):
        id = info.get('i')
        t = str(info.get('t'))
        try:
            response_image = session.get('https://api.zzzmh.cn/bz/v3/getUrl/' + id + t + "9")
            if response_image.status_code == 200:
                with open(f'./壁纸/{id}.jpg', 'wb') as f:
                    f.write(response_image.content)
                logger.info(f'下载成功: {id}')
        except Exception as e:
            logger.error(f'下载失败: {id}')
            logger.error(e)