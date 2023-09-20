import json
import math
import random

import cv2
import execjs
import numpy as np
from PIL import Image

import ddddocr
import requests
from loguru import logger
ocr = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)

session = requests.session()
def get_images():
    callback = 'sm_1695171179756'
    params = {
        'organization': 'd6tpAY1oV0Kv5jRSgxQr',
        'appId': 'default',
        'captchaUuid': '20230919090014anxDAkJEfmthx3YYZX',
        'lang': 'zh-cn',
        'channel': 'DEFAULT',
        'sdkver': '1.1.3',
        'model': 'slide',
        'rversion': '1.0.4',
        'data': '{}',
        'callback': callback,
    }
    response = session.get('https://captcha1.fengkongcloud.cn/ca/v1/register', params=params)
    if response.status_code == 200:
        data = response.text.replace(callback, "")[1:-1]
        json_data = json.loads(data)
        detail = json_data.get('detail')
        bg = 'https://castatic.fengkongcloud.cn' + detail.get('bg')
        fg = 'https://castatic.fengkongcloud.cn' + detail.get('fg')
        k = detail.get('k')
        rid = detail.get('rid')
        with open("bg.png", "wb") as f:
            f.write(session.get(bg).content)
        with open("fg.png", "wb") as f:
            f.write(session.get(fg).content)
        logger.info('获取图片成功返回k和rid: {} {}'.format(k, rid))
        return k, rid, bg, fg
    else:
        logger.error("获取图片接口失败.....")


def resize_iamge(bg_path, block_path):
    bg = Image.open(bg_path)
    block = Image.open(block_path)
    new_size_bg = (300, 150)
    bg_resized = bg.resize(new_size_bg)
    new_size_block = (45, 150)
    block_resized = block.resize(new_size_block)
    bg_resized.save("bg.png")
    block_resized.save("fg.png")


def loc_image(bg_path, block_path):
    try:
        # bg_img = Image.open(bg_path)
        # block_img = Image.open(block_path)
        target_content = open(bg_path, "rb").read()
        background_content = open(block_path, "rb").read()
        res = ocr.slide_match(target_content, background_content, simple_target=True)
        logger.success("识别成功: {}".format(res))
        return res.get('target')[0]
    except Exception as e:
        logger.error("ddddd识别异常")

def get_trace_and_times(distance):
    x = [0, 0]
    y = [0, 0, 0]
    z = [0]
    count = np.linspace(-math.pi / 2, math.pi / 2, random.randrange(20, 30))
    func = list(map(math.sin, count))
    nx = [i + 1 for i in func]
    add = random.randrange(10, 15)
    sadd = distance + add
    x.extend(list(map(lambda x: x * (sadd / 2), nx)))
    x.extend(np.linspace(sadd, distance, 3 if add > 12 else 2))
    x = [math.floor(i) for i in x]
    for i in range(len(x) - 2):
        if y[-1] < 30:
            y.append(y[-1] + random.choice([0, 0, 1, 1, 2, 2, 1, 2, 0, 0, 3, 3]))
        else:
            y.append(y[-1] + random.choice([0, 0, -1, -1, -2, -2, -1, -2, 0, 0, -3, -3]))
    for i in range(len(x) - 1):
        z.append((z[-1] // 100 * 100) + 100 + random.choice([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2]))
    trace = list(map(list, zip(x, y, z)))
    times = trace[-1][-1] + random.randint(1, 5)
    return trace, times

def guiji(offset):
    # break_flag = x + offset
    guiji_array = []
    start_time = random.randint(120, 150)
    array_one = [0, 0, start_time]
    guiji_array.append(array_one)
    x, y, time_x = 0, 0, start_time
    while x < offset:
        x += random.randint(10, 15)
        y = random.randint(-5, 5)
        time_x += random.randint(20, 60)
        i = [x, y, time_x]

        guiji_array.append(i)
    if guiji_array[-1][0] > offset:
        guiji_array.pop(-1)
        guiji_array.append([offset, y, time_x + random.randint(20, 60)])
        guiji_array.append([offset, y, time_x + random.randint(60, 120)])
        guiji_array.append([offset, y, time_x + random.randint(120, 180)])
        guiji_array.append([offset, y, time_x + random.randint(240, 300)])

    # logger.info(f"原轨迹长度: {len(guiji_array)}")
    logger.info(f"原轨迹: {guiji_array}")
    return guiji_array

def get_distance(fg, bg):
    fg_image = np.asarray(bytearray(requests.get(url=fg, verify=False).content), dtype='uint8')
    fg_image = cv2.imdecode(fg_image, 1)
    shape = fg_image.shape
    x_points, y_points = [], []
    for x_point in range(shape[0]):
        for y_point in range(shape[1]):
            if list(fg_image[x_point][y_point]) != [0, 0, 0]:
                x_points.append(x_point)
                y_points.append(y_point)
    fg_cut_image = fg_image[min(x_points):max(x_points), ]

    bg_image = np.asarray(bytearray(requests.get(url=bg, verify=False).content), dtype='uint8')
    bg_image = cv2.imdecode(bg_image, 1)
    bg_cut_image = bg_image[min(x_points):max(x_points), ]

    result = cv2.matchTemplate(bg_cut_image, fg_cut_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    distance = max_loc[0]
    return int(distance)

def verfiy(rid,k,guiji,leftx):
    check = open('check.js', encoding='utf-8').read()
    check_encrypt = execjs.compile(check)
    param_encrypt = check_encrypt.call('checkapi', rid,k,guiji,leftx)
    param_encrypt["callback"] = 'sm_1695179764348'
    param_encrypt["captchaUuid"] = '20230919154708F7yDbmdheayC64ATjk'
    # params = {
    #     'rj': 'LpMN9yrHH3I=',
    #     'rversion': '1.0.4',
    #     'sdkver': '1.1.3',
    #     'ee': '3i0thF8cJXhfvRzjsgzXc/ll850fm33q2wWkqNGHvP2Df7rXRxEtUGhcebPnMjMfoPam655sENCaUcplnigIKbs4iBC4ZlThYV/AvpPEQnLHmL9VAVlANCjgua/VucQQBzDH+aildJJz9ckiiCMdeQ==',
    #     'callback': 'sm_1695179764348',
    #     'ma': 'Ku1yrQmmWo8=',
    #     'organization': 'd6tpAY1oV0Kv5jRSgxQr',
    #     'xc': 'MPQBHp3MK74=',
    #     'rid': '2023092011140145ebb1a5fa5df947f7',
    #     'act.os': 'web_pc',
    #     'protocol': '179',
    #     'xy': 'xIAv2QAUoJA=',
    #     'ra': 'PvQ4gyi8WJs=',
    #     'ml': 'VH0ypuptH3Ah5oekvc4+3LvhaJ02yVSD',
    #     'us': 'zY8brT9SISY=',
    #     'jv': 'tnws0FUkt6c=',
    #     'qu': 'Q/IW6xhk8TI=',
    #     'ostype': 'web',
    #     'jn': 'w6ook9DZFNo=',
    #     'captchaUuid': '20230919154708F7yDbmdheayC64ATjk',
    #     'hd': 'w6ArMUdGI6s=',
    # }
    response = session.get('https://captcha1.fengkongcloud.cn/ca/v2/fverify', params=param_encrypt)
    if "PASS" in response.text:
        logger.success("滑动成功: {}".format(response.text))
    else:
        logger.error("滑动失败: {}".format(response.text))


if __name__ == '__main__':
    for _ in range(30):
        k, rid, bg, fg = get_images()
        resize_iamge("bg.png", "fg.png")
        loc = loc_image("bg.png", "fg.png")
        guiji_array = get_trace_and_times(loc)[0]
        verfiy(rid, k, guiji_array, loc)