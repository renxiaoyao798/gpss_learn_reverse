import random

import execjs
import requests
from loguru import logger
import json
import cv2
from PIL import Image
import numpy as np
session = requests.session()
getImage_params = {
    "browserInfo": [
        {
            "key": "userAgent",
            "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        },
        {
            "key": "language",
            "value": "zh-CN"
        },
        {
            "key": "hardware_concurrency",
            "value": 16
        },
        {
            "key": "resolution",
            "value": [
                1920,
                1080
            ]
        },
        {
            "key": "navigator_platform",
            "value": "Win32"
        }
    ],
    "nativeInfo": None,
    "additions": {},
    "options": {
        "sdk": "https://www.yunpian.com/static/official/js/libs/riddler-sdk-0.2.2.js",
        "sdkBuildVersion": "1.5.0(2021111001)",
        "hosts": "https://captcha.yunpian.com"
    },
    "fp": "d4c42aa7f70f2c7796ac4d218bd9a093",
    "address": "https://www.yunpian.com",
    "yp_riddler_id": "4c5a02a5-2483-4961-b5f0-58784dbba086"
}
encrypt_code = open('encrypt.js', encoding='utf-8').read()
encrypt = execjs.compile(encrypt_code)
encrypt_key = encrypt.call('encrypt', getImage_params)

def hk(path):
    # 读取文件
    image = Image.open(path)
    img = image.copy()  # 复制
    img = np.array(img)  # 转化为numpy
    img = cv2.resize(img, (304, 152))  # 用cv2resize
    img = img[:, :, (2, 1, 0)]  # BGR图像转RGB
    img1 = img.copy()
    # 将通道值小于150的转变为黑色
    for h in range(img.shape[0]):
        for w in range(img.shape[1]):
            if img[h, w, 0] < 150 and img[h, w, 1] < 150 and img[h, w, 2] < 150:
                for c in range(3):
                    img[h, w, c] = 0
            else:
                for c in range(3):
                    img[h, w, c] = 255
    canny_img = cv2.Canny(img, 0, 100)  # 边缘检测
    counts, _ = cv2.findContours(canny_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 轮廓检测
    result_x = 0
    for c in counts:
        x, y, w, h = cv2.boundingRect(c)
        #  去除较小先验框
        if w < 30:
            continue
        if h < 30:
            continue
        cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 2)
        print(f"左上点的坐标为：{x, y}，右下点的坐标为{x + w, y + h}")
        result_x = x
    cv2.imwrite('bg_result.png', img1)
    return result_x
def guiji(x, y, offset):
    break_flag = x + offset
    guiji_array = []
    time_x = 102
    for j in range(100000):
        if x > break_flag:
            break
        i = [x, y, time_x]
        x += random.randint(1, 5)
        y += random.randint(-1, 1)
        time_x += random.randint(0, 60)
        guiji_array.append(i)
    logger.info(f"原轨迹长度: {len(guiji_array)}")
    logger.info(f"原轨迹: {guiji_array}")
    return guiji_array

def get_image():
    params = {
        'cb': encrypt.call('get_cb'),
        'i': encrypt_key.get('i'),
        'k': encrypt_key.get('k'),
        # 'token': '88a8c7cacbad46d9b731e1397abf6f39',
        'captchaId': '974cd565f11545b6a5006d10dc324281',
    }
    # 获取图片接口
    response = session.get('https://captcha.yunpian.com/v1/jsonp/captcha/get', params=params)
    if response.status_code == 200:
        logger.info("请求图片接口成功")
        # 获取图片
        imageApi = response.text.replace("ypjsonp(", "").replace(")", "")
        imageApi_load = json.loads(imageApi)
        image_token = imageApi_load.get('data').get('token')
        image_bg = requests.get(imageApi_load.get('data').get('bg'))
        logger.info("返回图片连接: {} 图片token: {}".format(image_bg, image_token))
        return image_bg, image_token
    else:
        logger.error("请求图片接口失败")
        return None, None

def save_identify_image(image_bg):
    """
    保存识别图片
    :param image_bg:
    :return: 返回识别坐标
    """
    with open('image_bg.png', 'wb') as f:
        f.write(image_bg.content)
    result_x = hk('image_bg.png')
    logger.info(f"识别坐标为: {result_x}")
    return result_x


def verify_image(image_token, result_x):
    guiji_array = guiji(1100, 1969, result_x)
    distanceX = (304 - 59) * (result_x / (304 - 42)) / 304
    verify_params = {
        "points": guiji_array,
        "distanceX": distanceX,
        "fp": "d4c42aa7f70f2c7796ac4d218bd9a093",
        "address": "https://www.yunpian.com",
        "yp_riddler_id": "4c5a02a5-2483-4961-b5f0-58784dbba086"
    }
    verify_encrypt = encrypt.call('encrypt', verify_params)
    verify_params = {
        'cb': encrypt.call('get_cb'),
        'i': verify_encrypt.get('i'),
        'k': verify_encrypt.get('k'),
        'token': image_token,
        'captchaId': '974cd565f11545b6a5006d10dc324281',
    }
    verify_response = session.get('https://captcha.yunpian.com/v1/jsonp/captcha/verify', params=verify_params)
    logger.info(f"验证结果:{verify_response.text}")


if __name__ == '__main__':
    image_bg, image_token = get_image()
    result_x = save_identify_image(image_bg)
    verify_image(image_token, result_x)