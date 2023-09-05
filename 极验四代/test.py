import json
import re
import time

import execjs
import requests
from loguru import logger
import cv2
encrypt = open('encrypt.js', encoding='utf-8').read()
encrypt = execjs.compile(encrypt)
session = requests.Session()


def get_image_api():
    params = {
        # 'callback': 'geetest_1693278287410',
        'captcha_id': '54088bb07d2df3c46b79f80300b0abbe',
        # 'client_type': 'web',
        # 'lot_number': '608c3a27a039458cac4311f4164aac16',
        # 'risk_type': 'slide',
        # 'pt': '1',
        # 'lang': 'zho',
        # 'payload': 'xSJqOy81RFro17RrPzpVa-Q6ptDiPRqrN6so5KOwhB3Na5_TIiWwuKwe_f2_rdZDyHOxncyItK0Lo6-G91bpmW5jg7qiTHiySYIYTisu2dpZUIJJuvDjit1vj1IJJVqU0Kw9a0h7wSMyv1AsLjTsrPybxtEFBZRd1xKnDBqzOPHlp8-ynj3m939n2WcQ-9oqFGTfDA2QWhWYJVJs1R1pe9CPYfAP-Niun08wcnYgzOPXfGqe8_GE3PgrScAcTaKGM045H-A73aQbJ1f4DsLZNEf3XnOuzoCiD3V4z_mLEAztHIfAUhhWty2UrN44gmKZfQGr3IdnJKB1vqPmud4evJmAdGnNWUEfD2b6byyfNZKkGp5sOWpbxqFw4V49w5mL0gzQiyXbn5hH38SrVo6fTFhmiaX8vfv14vQazLpoRzxU5cuBpLw0AWxBtwvr9JARBcYJ8qScbaNbJJmxQZTMk-5BVwheDCfegn6pa7kSAHVOxRiZw0FDaf0Kx5XzdQezOeS6lpvvOiIcvvuAFe8FP68ZwSD4TJV6FNUOW51FNHlvS6aYZpaR3OQZErJ2ex4Yf4c9apruigTpwMdz0ZwrhJdk-m3btKWdhskiDRNvwAQgUkDLCsndwyAuYkYTGG3hhy54w1Cp8qcoEVv6YoJUyssmPHTSkGiuMJIymnOu8WlZ4bEoIgokP916uc1SYkfqkjSsOtKCN4MxgZ90pzXsfjaTHMoV-UEYJPcJoovuG7Wwb1lPPCq1nzA-YSerYqelPWfujbHt2_QmVZ3vzLtlFqomwSyxww4D660GAFrkM2F9Wp7bHwieX0_M70aCDAKOQAX4bBaenzytvzClSNtlHm4vXREarWP1ynsnFuPTeIzKg7V9lJQbkbwsTsfG53ieZRFjQ_h489XgLL9iAacLIIZZ3C65NhAioQnjxk2fiC2S67uo71OQda_oulbP2t-ZetGS0LaiIugGtIfKN1ojSqeIw1JT1xeuqvvxJlXe8bjoRmdcCuZpDH2AxE9_bEGJGgUPa3V7NSaoVgNep1tujFf0nlwJbsUDyHPZP9z85jWNiXOIjEbIoUg9jlxkPyBYSXr9ZUOF3EAsxBZnx66DQETIlrG3fVp91Os9NZsmUDgwcsC63-Cn0xHOEM1p_aiWp-kpqvQAIi_jfUs9eF2G6BJY2JeNRFXOXh--ulQC-9mNsB_Pim5S8MxtYR4wvkbcVonr52kgQojSd1dV7q0xb3rtyTNqnGiCNxhd29EVZjcpLc5T9n8j4x80FCJvpRq5_OAZ4lXAES5bLK0HVFn067ooSghFv0uaNw6kMo02KYlFkOXNjaEtgVskzpVgc0ftRGhTqg0mpEkJic8yirTfXcnyXCum-UqOQNjRjXTpQHUvtK_INVt3xMdJu6ZhGV8U-LYuJai_mB_YCnXfGEPdN_E2dGIc_vJW1ejQhLXOeSHlwTSUOlwRnztFzlE4J3weQvt_Na4k1DELxzA3qEM5b7jYrDHs4j-9xgR2QPCLLdHxfwdTdB36MuMKcF8Hltf8xDRzFQ1Bt1TTW5q60dHOJiBKNo-pxBNowUYlFfCGOnvLrZmoXkaLc85sB2RZBztmfPuTyLOxoJ2YvG6doIo_MJ5zUoZhL7UdzneFP4SsOghVp22scTYJQ5amQB1eDFhJ02Zp4qi6zqSbghIAQAp9qYooNBHPYAWJnPDZYgMEKVTX_LJaAdo_T5S0q2UxRVWoQ3gg8V7oyTFM6xATYuqNZH3VnkgMNgpaROe5g8iYeMLrYBx4ypKEnf7HsB3qVU5fYih2Yfq-x4kbcm8tXG1UTsKSk-T7PUD4Wu_teWW3GViAABwGgXEbix7selniI621Gn73QgqGdBI3XjePQBIV7UHrivlKSOxCYhW-tqeHAIQR6kdpDgGeD-c_dA4IoOkexbco-JSi45n9FQraMiHWgrKtFw2rkq5qXfsASo17PkBpOuZ9Gbubcwkme8O1C_cppWS57Ch0dIbGiD-vl23RKVMCJvhcRU5AJUxrB7zLcrYvriIfQNJmvI3kusHAQgU4SearsppmFWmF5OEDae_0chmKTi9BIHeibcL5PmrmbGOt4EMbLH5DpyOAy9Zz3gklcKSMvSLsRSCvybU8vGxsEoe5rVhalUJYMqcBIP5P64valjg6BbCYn4rV1QbX-hKPLBHvpFWoykZjtu4z3s0841h3tyXy0N3cxbRjbW41hMIOCpNpxGQc7gAvYxlIYKZuFTPxixtBgtby5v0AhVB-3COFt_LhiSiakGJWyHLfM4Nh3b7V-D1tG0ji7OiJvi7aJ1LSxOp4kVeEBL8ZIcQDX3p2AiidKIDpo9ozejA9QkBmvAv9iqO7hKa42yCK5UWur3BUBj5K_Gl10_lLdxKaGFTj9hWizr4OIutRrMWiDg1NATvknMtnhfnI1o5fIpA5rwt94K36r9PpYtG7qYN_T0mXQU_XArG5aSxrnTxaNIAuVaqIifpptfjGXgzykEMHjeYZpkHOISU4-6zVi39kb87IhR3utw8_20j-D5CMe8IYbloAKa9hCB2Ke_Qx59tro8EAfxP2jzGI8OjPjNhfyv9A0P8KHp468sxrw1hiK5cwSxJ03iN9Ld7tvbvbWF_7ZOwQW3rrzrNPTgq90xnyHHx5U4UIABm6RO_kWJvzWxVxjr3GnwgEs22jkwoXAD3QBedpHkfZFXWAKMSQ_76_11rIKOWea5nzhSMsuuceSLq68zhXjWPjpNn7XbXxFf0I12oRvebuvQpZFGit1NbAkqjL_B3vgowX32GifxuOa_tmZvBZLsTZ5cfi6CBaeh_jgn6sI2tmq78tvQeyIMJL_YXitnm9LyFxmK2r-HtbBhplZR7Y9OPep7XxRrllScPKLOvpeBezJqFSl5Qa7ptq0zYo8Jjy-ajL_MEHPafvW1699uPco74wH0fo2n9v0IWLx14aH3uV_3J3rbVyoctVOUUOax_R2e4DYfJVkH8pEdSQxY8llrpb3riKOxu3dZCFtldDFx_Mw5FIAK7SaXRHl0U_OlelowE0o2l4lrngI0i-vG4A9utcIiZvgda2bMvur4Xm2Qf-plDHsLTQKfXgcv9n2tSDJj_ATVVhrZVlmFI=',
        # 'process_token': '207d67dac7c9a76bfde79d6f675afd3b4318c84301331b3d7fb9c5260fbbfd0f',
        # 'payload_protocol': '1',
    }
    response = session.get('https://gcaptcha4.geetest.com/load', params=params)
    if response.status_code == 200:
        result_data = response.text
        result_data = result_data[1:]
        result_data = result_data[:-1]
        result_json = json.loads(result_data)
        if result_json.get('status') == "success":
            data = result_json.get('data')
            logger.info(f"图片data: {data}")
            lot_number = data.get('lot_number')
            slice_url = 'https://static.geetest.com/' + data.get('slice')
            bg_url = 'https://static.geetest.com/' + data.get('bg')
            try:
                # 保存图片
                with open("hk\slice.png", 'wb') as fh:
                    fh.write(requests.get(slice_url).content)
                with open(r"hk\bg.png", 'wb') as fh:
                    fh.write(requests.get(bg_url).content)
                logger.info("Geetest image loaded successfully")
                return lot_number
            except Exception:
                logger.error("Geetest image load failed")
        else:
            logger.error("Geetest resullt Error failed")
    else:
        logger.error('获取图片接口失败')

def identify_gaps(img_path, tm_path):
    # 导入图片，灰度化
    img_rgb = cv2.imread(img_path)
    template_rgb = cv2.imread(tm_path)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    tm_gray = cv2.cvtColor(template_rgb, cv2.COLOR_BGR2GRAY)
    # 缺口图去除背景
    h, w = tm_gray.shape
    w_start_index, h_start_index = 0, 0
    w_end_index, h_end_index = w, h
    # 缺口图去除背景
    # 算出高起始位置
    for i in range(h):
        if not any(tm_gray[i, :]):
            h_start_index = i
        else:
            break
    # 算出高的结束位置
    for i in range(h - 1, 0, -1):
        if not any(tm_gray[i, :]):
            h_end_index = i
        else:
            break
    # 算出宽的起始位置
    for i in range(w):
        if not any(tm_gray[:, i]):
            w_start_index = i
        else:
            break
    # 算出宽的起始位置
    for i in range(w - 1, 0, -1):
        if not any(tm_gray[:, i]):
            w_end_index = i
        else:
            break
    # 取出完整的缺口图
    tm_gray = tm_gray[h_start_index:h_end_index + 1, w_start_index:w_end_index + 1]
    # 自适应阈值话
    img_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 0)
    tm_thresh = cv2.adaptiveThreshold(tm_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 0)

    # 边缘检测
    img_canny = cv2.Canny(img_thresh, 0, 500)
    tm_canny = cv2.Canny(tm_thresh, 0, 500)
    # cv2.imshow("img_canny", img_canny)
    # cv2.imshow("tm_canny", tm_canny)
    h, w = tm_gray.shape[:2]
    # 模板匹配
    res = cv2.matchTemplate(img_canny, tm_canny, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    right_bottom = (max_loc[0] + w, max_loc[1] + h)  # 右下角
    # 圈出矩形坐标
    cv2.rectangle(img_rgb, max_loc, right_bottom, (0, 0, 255), 2)

    # 保存处理后的图片
    cv2.imwrite('res.png', img_rgb)
    logger.info("左上坐标: {}, 右下坐标: {}".format(max_loc, right_bottom))
    # 显示图片 参数：（窗口标识字符串，imread读入的图像）
    # cv2.imshow("test_image", img_rgb)
    return max_loc[0]



def verify_api(loc, lot_number):
    encrypt_params = {
        "setLeft": loc - 12,
        "userresponse": loc - 12 / 1.0059466666666665 + 2,
        # "lot_number": lot_number,
        # "passtime": 185,
        # "device_id": "5d25317d91fd2c612ee3c2ec316f90b0",
        # "pow_msg": "1|0|md5|2023-09-04T21:36:15.906420+08:00|54088bb07d2df3c46b79f80300b0abbe|dfb3952f54d04f5797871d28c5675736||08e20cac83ce79ff",
        # "geetest": "captcha",
        # "lang": "zh",
        # "ep": "123",
        # "biht": "1426265548",
        # "O00n": "WNu0",
        # "em": {
        #     "ph": 0,
        #     "cp": 0,
        #     "ek": "11",
        #     "wd": 1,
        #     "nt": 0,
        #     "si": 0,
        #     "sc": 0
        # }
    }
    w = encrypt.call('get_w', json.dumps(encrypt_params))

    params = {
        'captcha_id': '54088bb07d2df3c46b79f80300b0abbe',
        'lot_number': lot_number,
        'w': w,
    }

    response = session.get('https://gcaptcha4.geetest.com/verify', params=params)
    if response.status_code == 200:
        result_data = response.text
        result_data = result_data[1:]
        result_data = result_data[:-1]
        result_json = json.loads(result_data)

        if result_json.get('status') == "success":
            data = result_json.get('data')
            logger.info(f"验证data: {data}")
            if data.get('result') == "success":
                logger.success('Verified Success 滑动验证成功')
            else:
                logger.error('Verified Failed 滑动验证失败')
    else:
        logger.error('Error request')


if __name__ == '__main__':
    for i in range(100):
        lot_number = get_image_api()
        loc = identify_gaps('hk/bg.png', 'hk/slice.png')
        verify_api(loc, lot_number)
        # time.sleep(20)