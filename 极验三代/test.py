import hashlib
import json
import io
import random

import ddddocr
from PIL import Image
import execjs
import requests
import time

from loguru import logger
session = requests.session()
encrypt = open('encrypt.js', encoding='utf-8').read()
encrypt = execjs.compile(encrypt)
encrypt_param = open('encrypt_param.js', encoding='utf-8').read()
encrypt_param = execjs.compile(encrypt_param)
ocr = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)


def _img_restore(img: bytes) -> bytes:
    """
    底图还原
    """
    image = Image.open(io.BytesIO(img))
    standard_img = Image.new("RGBA", (260, 160))
    position = [39, 38, 48, 49, 41, 40, 46, 47, 35, 34, 50, 51, 33, 32, 28, 29, 27, 26, 36, 37, 31, 30, 44, 45, 43,
                42, 12, 13, 23, 22, 14, 15, 21, 20, 8, 9, 25, 24, 6, 7, 3, 2, 0, 1, 11, 10, 4, 5, 19, 18, 16, 17]
    s, u = 80, 10
    for c in range(52):
        a = position[c] % 26 * 12 + 1
        b = s if position[c] > 25 else 0
        im = image.crop(box=(a, b, a + 10, b + 80))
        standard_img.paste(im, box=(c % 26 * 10, 80 if c > 25 else 0))
    temp_io = io.BytesIO()
    standard_img.save(temp_io, format='png')
    return temp_io.getvalue()


def register_slide():
    params = {
        't': str(time.time()).replace(".", "")[:13],
    }
    print(params)
    url = 'https://www.geetest.com/demo/gt/register-slide-official'
    response = session.get(
        url,
        params=params,
    )
    if response.status_code == 200:
        if response.json().get('success') == 1:
            gt = response.json().get('gt')
            challenge = response.json().get('challenge')
            logger.success(f"注册成功: gt {gt} challenge {challenge}")
            return gt, challenge
        else:
            logger.error(f"注册失败")
    else:
        logger.error(f"{url} 接口异常非200状态码")


def get_image(gt, challenge):
    params = {
        'is_next': 'true',
        'type': 'slide3',
        'gt': gt,
        'challenge': challenge,
        'lang': 'zh-cn',
        'https': 'true',
        'protocol': 'https://',
        'offline': 'false',
        'product': 'embed',
        'api_server': 'api.geevisit.com',
        'isPC': 'true',
        'autoReset': 'true',
        'width': '100%',
        'callback': 'geetest_1693994409960',
    }

    # url = 'https://api.geetest.com/get.php'
    url = 'https://api.geevisit.com/get.php'
    response = session.get(url, params=params)
    # print(response.content.decode("unicode_escape"))
    if response.status_code == 200:
        if 'bg' in response.text and 'fullbg' in response.text:
            data = response.text.replace('geetest_1693994409960(', "")[:-1]
            json_Data = json.loads(data)
            bg = 'https://static.geetest.com/' + json_Data.get('bg').replace(".jpg", '.webp')
            slice = 'https://static.geetest.com/' + json_Data.get('slice').replace(".jpg", '.webp')
            challenge = json_Data.get("challenge")
            try:
                bg_reponse = session.get(bg)
                slice_reponse = session.get(slice)
                hy_image = _img_restore(bg_reponse.content)
                with open("底图还原.png", "wb") as f:
                    f.write(hy_image)
                with open("小滑块.png", "wb") as f:
                    f.write(slice_reponse.content)
                logger.success('成功获取混淆底图')
                logger.success(f"返回新的challenge: {challenge}")
                return challenge, json_Data.get('s')
            except:
                logger.error('保存混淆底图失败')
    else:
        logger.error(f"{url} 接口异常非200状态码")


def ajax(gt, challenge):
    response = session.get(
        f'https://api.geevisit.com/ajax.php?gt={gt}&challenge={challenge}&lang=zh-cn&pt=0&client_type=web',
    )
    # print(response.text)

def _track(distance: int):
    def __ease_out_expo(step):
        return 1 if step == 1 else 1 - pow(2, -10 * step)
    if not isinstance(distance, int) or distance < 0:
        raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
        # 初始化轨迹列表
    slide_track = [[random.randint(-50, -10), random.randint(-50, -10), 0], [0, 0, 0],]
    # 共记录count次滑块位置信息
    count = 30 + int(distance / 2)
    # 初始化滑动时间
    t = random.randint(50, 100)
    # 记录上一次滑动的距离
    _x, _y = 0, 0
    for i in range(count):
        # 已滑动的横向距离
        x = round(__ease_out_expo(i / count) * distance)
        # 滑动过程消耗的时间
        t += random.randint(10, 20)
        if x == _x:
            continue
        slide_track.append([x, _y, t])
        _x = x
    slide_track.append(slide_track[-1])
    passTime = slide_track[-1][-1]
    return slide_track, passTime

def guiji(offset):
    # break_flag = x + offset
    guiji_array = []
    array_one = [-31, -31, 0]
    guiji_array.append(array_one)
    x, y, time_x = 0, 0, 0
    while x < offset:
        i = [x, y, time_x]
        x += random.randint(0, 2)
        y += random.randint(-1, 1)
        time_x += random.randint(0, 15)
        guiji_array.append(i)
    guiji_array.append(i)  #
    logger.info(f"原轨迹长度: {len(guiji_array)}")
    logger.info(f"原轨迹: {guiji_array}")
    return guiji_array


def slide_verify(gt, challenge, guiji, t, passtime, s):
    encrypt_params = encrypt_param.call("get_aes_params", guiji, t, gt, challenge, passtime, s)
    encrypt_params['rp'] = hashlib.md5(encrypt_params.get('rp').encode()).hexdigest()
    w = encrypt.call('get_w', json.dumps(encrypt_params))

    params = {
        'gt': gt,
        'challenge': challenge,
        'lang': 'zh-cn',
        '%24_BCX': '0',
        'client_type': 'web',
        "w": w,
        'callback': 'geetest_1694058231021'
    }
    response = session.get(
        'https://api.geevisit.com/ajax.php', params=params
    )
    print(response.text)

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


if __name__ == '__main__':
    for i in range(5):
        gt, challenge = register_slide()
        ajax(gt, challenge)
        challenge, s = get_image(gt, challenge)
        loc = loc_image('底图还原.png', '小滑块.png')
        guiji_array, passtime = _track(loc)
        slide_verify(gt, challenge, guiji_array, loc, passtime, s)






