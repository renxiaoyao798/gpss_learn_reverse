import json
import random
import time
import string
import ddddocr
import requests
import execjs
from loguru import logger
ocr = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
session = requests.session()

cookies = {
    '_ga': 'GA.1.22e15bebfbc61.97fe7074837aad5a988c',
    'mp_versions_hubble_jsSDK': 'DATracker.globals.1.6.14',
    'Hm_lvt_4671c5d502135636b837050ec6d716ce': '1694746450',
    'hb_MA-93D5-9AD06EA4329A_source': 'www.baidu.com',
    '__root_domain_v': '.163.com',
    '_qddaz': 'QD.632094746450548',
    'Hm_lpvt_4671c5d502135636b837050ec6d716ce': '1694746453',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': '_ga=GA.1.22e15bebfbc61.97fe7074837aad5a988c; mp_versions_hubble_jsSDK=DATracker.globals.1.6.14; Hm_lvt_4671c5d502135636b837050ec6d716ce=1694746450; hb_MA-93D5-9AD06EA4329A_source=www.baidu.com; __root_domain_v=.163.com; _qddaz=QD.632094746450548; Hm_lpvt_4671c5d502135636b837050ec6d716ce=1694746453',
    'Referer': 'https://dun.163.com/',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

def get_image():
    get_image = open('get_image.js', encoding='utf-8').read()
    get_image_encrypt = execjs.compile(get_image)
    cb = get_image_encrypt.call('get_cb')
    fp_image = open('get_fp.js', encoding='utf-8').read()
    fp_image_encrypt = execjs.compile(fp_image)
    fp = fp_image_encrypt.call('get_fp')
    callback = "__JSONP_{}_1".format(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(7)))
    params = {
        'referer': 'https://dun.163.com/trial/jigsaw',
        'zoneId': 'CN31',
        'dt': 's7Bl8Jf72DlAQkAFBBaFzdI4oFzHvhiP',
        'acToken': '',
        'id': '07e2387ab53a4d6f930b8d9a9be71bdf',
        'fp': fp,
        'https': 'true',
        'type': '2',
        'version': '2.23.0',
        'dpr': '1',
        'dev': '1',
        'cb': cb,
        'ipv6': 'false',
        'runEnv': '10',
        'group': '',
        'scene': '',
        'lang': 'zh-CN',
        'sdkVersion': 'undefined',
        'iv': '2',
        'width': '320',
        'audio': 'false',
        'sizeType': '10',
        'smsVersion': 'v3',
        'token': "",
        'callback': callback,
    }

    # get_image_headers = {"Accept-Encoding": "gzip, deflate, br", "Host": "c.dun.163.com",
    #            "Cookie": "__root_domain_v=.163.com; _qddaz=QD.571790359664516"}
    # headers.update(get_image_headers)
    response = requests.get('https://c.dun.163.com/api/v3/get', params=params, cookies=cookies, headers=headers)
    if '''"msg":"ok"''' in response.text:
        logger.info("获取图片接口成功")
        data = json.loads(response.text[len(callback) + 1:len(response.text) - 2])
        json_data = data
        bg = json_data.get("data").get("bg")[0]
        front = json_data.get("data").get("front")[0]
        with open("bg.png", "wb") as bgf:
            bgf.write(session.get(bg).content)
        with open("front.png", "wb") as frontf:
            frontf.write(session.get(front).content)
        token = json_data.get('data').get("token")
        logger.success('图片下载成功返回token: {}'.format(token))
        return token

def loc_image(bg_path, block_path):
    try:
        # bg_img = Image.open(bg_path)
        # block_img = Image.open(block_path)
        target_content = open(bg_path, "rb").read()
        background_content = open(block_path, "rb").read()
        res = ocr.slide_match(target_content, background_content, simple_target=True)
        logger.success("识别成功: {}".format(res))
        return res.get('target')[0]
    except:
        logger.error("ddddd识别异常")

def guiji(offset):
    # break_flag = x + offset
    guiji_array = []
    start_time = random.randint(120, 150)
    array_one = [4, 0, start_time]
    guiji_array.append(array_one)
    x, y, time_x = 4, 0, start_time
    while x < offset:
        x += random.randint(0, 2)
        y = random.randint(-1, 1)
        time_x += random.randint(5, 10)
        i = [x, y, time_x]

        guiji_array.append(i)
    if guiji_array[-1][0] < offset:
        guiji_array.append([offset, y, time_x + random.randint(0, 5)])
        guiji_array.append([offset, y, time_x + random.randint(0, 15)])


    # logger.info(f"原轨迹长度: {len(guiji_array)}")
    # logger.info(f"原轨迹: {guiji_array}")
    return guiji_array


def verify_api(token, left, guiji):
    get_image = open('get_image.js', encoding='utf-8').read()
    get_image_encrypt = execjs.compile(get_image)
    verify = open('verify.js', encoding='utf-8').read()
    verify_encrypt = execjs.compile(verify)
    cb = get_image_encrypt.call('get_cb')
    data = verify_encrypt.call("get_data", token, str(left)+"px", guiji)
    params = {
        'referer': 'https://dun.163.com/trial/jigsaw',
        'zoneId': 'CN31',
        'dt': 's7Bl8Jf72DlAQkAFBBaFzdI4oFzHvhiP',
        'id': '07e2387ab53a4d6f930b8d9a9be71bdf',
        'token': token,
        'acToken': 'undefined',
        'data': data,
        'width': '320',
        'type': '2',
        'version': '2.23.0',
        'cb': cb,
        'extraData': '',
        'bf': '0',
        'runEnv': '10',
        'sdkVersion': 'undefined',
        'iv': '2',
        'callback': "__JSONP_{}_2".format(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(7))),
    }
    response = session.get('https://c.dun.163.com/api/v3/check', params=params, cookies=cookies, headers=headers )
    if '"result":true,' in response.text:
        logger.success("识别成功: {}".format(response.text))
        return True
    else:
        logger.error("识别失败: {}".format(response.text))
        return False



if __name__ == '__main__':
    for i in range(20):
        token = get_image()
        left_x = loc_image("bg.png", "front.png")
        guiji_array = guiji(left_x)
        a = verify_api(token, left_x, guiji_array)
