import requests
import re
import execjs
import json
from loguru import logger
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': '__jsluid_s=139b7306937b8d477070c455ea3dd291; SL_G_WPT_TO=zh-CN; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; __jsl_clearance_s=1689159001.783|0|g2qceC43dcLXkiwnq2LA0%2BkViVw%3D; JSESSIONID=EDA6D0B7B7429FD5F38AD2DC9634E98B',
    'Origin': 'https://www.cnvd.org.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://www.cnvd.org.cn/flaw/list?flag=true',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def get_cookie_session():
    cookies = {}
    session = requests.session()
    # 第一次请求 获取cookie: __jsl_clearance_s
    response = session.get('https://www.cnvd.org.cn/flaw/list', headers=headers).text
    re_result = re.findall(r'document.cookie=(.*?);location', response)[0]
    clearance = execjs.eval(re_result)
    jsl_clearance_s = clearance.split(';')[0].split("=")[1]
    cookies['__jsl_clearance_s'] = jsl_clearance_s
    session.cookies.update(cookies)
    # 第二次请求加密文件保存到本地, 获取go函数中的参数
    response = session.get('https://www.cnvd.org.cn/flaw/list', headers=headers).text
    go_func_params = re.findall(r';go\((.*?)\)</script>', response)[0]
    go_func_params = json.loads(go_func_params)
    encrypt_type = go_func_params['ha']
    if encrypt_type == 'md5':
        encrypt_path = 'cnvd_md5_js.js'
    elif encrypt_type == 'sha1':
        encrypt_path = 'cnvd_sha1_js.js'
    elif encrypt_type == 'sha256':
        encrypt_path = 'cnvd_sha256_js.js'
    else:
        raise Exception('未知的加密类型')
    js_code = open(encrypt_path, encoding='utf-8').read()
    cnvd_jd = execjs.compile(js_code)
    jsl_ckearance_s_two = cnvd_jd.call('go', go_func_params)  # 执行go函数
    cookies['__jsl_clearance_s'] = jsl_ckearance_s_two  # 更新cookie
    session.cookies.update(cookies)
    return session


def go():
    session = get_cookie_session()
    for _ in range(30):
        response = session.get('https://www.cnvd.org.cn/flaw/list', headers=headers)
        if response.status_code == 200:
            logger.success('请求成功')
        elif "如果您是网站管理员，请登录知道创宇云防御" in response.text:
            logger.error('如果您是网站管理员, 请登录知道创宇云防御, 被封了')
            break
        else:
            logger.error('请求失败: {}'.format(response.status_code))
            session = get_cookie_session()
            continue


if __name__ == '__main__':
    go()