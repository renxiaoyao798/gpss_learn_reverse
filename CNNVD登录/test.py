from hashlib import md5

import requests
import base64
import re
import ddddocr
session = requests.Session()


def analysis_base64(src):
    result = re.search("data:image/(?P<ext>.*?);base64,(?P<data>.*)", src, re.DOTALL)
    if result:
        ext = result.groupdict().get("ext")
        data = result.groupdict().get("data")
    else:
        raise Exception("Do not parse!")
    img = base64.urlsafe_b64decode(data)
    return img

def ddddocr_run(file_path):
    ocr = ddddocr.DdddOcr(show_ad=False)
    with open(file_path, 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    return res


def get_image_token():
    response = session.get('https://www.cnnvd.org.cn/web/verificationCode/getBase64Image')
    data = response.json()
    image = data.get('data').get('image')
    yzm_content = analysis_base64(image)
    with open('yzm.png', 'wb') as f:
        f.write(yzm_content)
    yzm_code = ddddocr_run('yzm.png')
    if len(yzm_code) != 4:
        print('验证码识别失败')
        return get_image_token()
    return yzm_code, data.get('data').get('verifyToken')


def password_encrypt(password):
    return md5(password.encode('utf-8')).hexdigest()


def login(json_data):
    response = session.post('https://www.cnnvd.org.cn/web/login',  json=json_data)
    print(response.json())


if __name__ == '__main__':
    yzm_code, image_token = get_image_token()
    json_data = {
        'username': '1231233123@qq.com',
        'password': password_encrypt('11111111'),
        'code': yzm_code,
        'verifyToken': image_token,
    }
    login(json_data)