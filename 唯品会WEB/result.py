import time
from loguru import logger
import requests
import json
import re
headers = {
    'authority': 'mapi.vip.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'vip_cps_cuid=CU1689560643045fd3cfb53526c5e1e2; vip_cps_cid=1689560643049_a8f4f5d727c5491854df0aeabb344e20; cps_share=cps_share; cps=adp%3Antq8exyc%3A%40_%401689560643048%3Amig_code%3A4f6b50bf15bfa39639d85f5f1e15b10f%3Aac014miuvl0000b5sq8cb95w94i9e028; PAPVisitorId=575a70985e786d5de83a2f816c97a8c2; vip_new_old_user=1; vip_city_name=%E5%B9%BF%E5%B7%9E%E5%B8%82; user_class=a; mars_cid=1689560645356_a32a1ebe2e979bd3db337d566225e71d; mars_sid=bbd8c693127b514dc05db057b13cccc3; mars_pid=0; visit_id=297B4D25F7337126B1147CA331039B94; VipUINFO=luc%3Aa%7Csuc%3Aa%7Cbct%3Ac_new%7Chct%3Ac_new%7Cbdts%3A0%7Cbcts%3A0%7Ckfts%3A0%7Cc10%3A0%7Crcabt%3A0%7Cp2%3A0%7Cp3%3A1%7Cp4%3A0%7Cp5%3A1%7Cul%3A3105; vip_address=%257B%2522pname%2522%253A%2522%255Cu5317%255Cu4eac%255Cu5e02%2522%252C%2522pid%2522%253A%2522101101%2522%252C%2522cname%2522%253A%2522%255Cu5e7f%255Cu5dde%255Cu5e02%2522%252C%2522cid%2522%253A%2522101101101%2522%257D; vip_province=101101; vip_province_name=%E5%8C%97%E4%BA%AC%E5%B8%82; vip_city_code=101101101; vip_wh=VIP_BJ; vip_ipver=31; vip_tracker_source_from=; pg_session_no=6; vip_access_times=%7B%22list%22%3A3%7D',
    'pragma': 'no-cache',
    'referer': 'https://list.vip.com/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

session = requests.session()  # 创建session对象
session.headers = headers  # 设置请求头


def get_tabs():
    """
    获取品类id
    :return: 所有品类id
    """
    # 1.获取品类id
    tabs_params = {
        'callback': 'getTopCategory',
        'app_name': 'shop_pc',
        'app_version': '4.0',
        'warehouse': 'VIP_BJ',
        'fdc_area_id': '101101101',
        'client': 'pc',
        'mobile_platform': '1',
        'province_id': '101101',
        'api_key': '70f71280d5d547b2a7bb370a529aeea1',
        'hierarchy_id': '117',
    }
    tabs_response = session.get('https://mapi.vip.com/vips-mobile/rest/shopping/pc/category/index/get_tab/v1',
                                params=tabs_params).text
    tabs_json = json.loads(re.findall(r'getTopCategory\((.*?)\)', tabs_response)[0])
    tags = tabs_json['data']['data']['tabs']
    return tags


def get_category(tabs_id):
    """
    获取子品类id
    :param tabs_id:
    :return: 所有子品类id
    """
    call_back = f'getSubCategory{tabs_id}'
    category_params = {
        'callback': call_back,
        'app_name': 'shop_pc',
        'app_version': '4.0',
        'warehouse': 'VIP_BJ',
        'fdc_area_id': '101101101',
        'province_id': '101101',
        'api_key': '70f71280d5d547b2a7bb370a529aeea1',
        'hierarchyId': '117',
        'categoryId': str(tabs_id),
        'clientFrom': 'PC',
        'client': 'pc',
        'net': 'wifi',
        'width': '1920',
        'height': '1080',
        'pcmpWidth': '750',
        'mobile_channel': 'nature',
        'functions': 'jumper',
    }
    category_response = session.get('https://mapi.vip.com/vips-mobile/rest/shopping/pc/category/index/get_tab_data/v1',params=category_params).text
    category_json = json.loads(re.findall(rf'{call_back}\((.*?)\)', category_response)[0])
    return category_json['data']['data']['sectionList']


def get_product_id(category_id, page=1):
    """
    获取商品id
    :param category_id: 子品类id
    :param page: 页数
    :return: 产品id
    """
    pageOffset = (page - 1) * 120
    product_params = {
        'callback': 'getProductIdsListRank',
        'app_name': 'shop_pc',
        'app_version': '4.0',
        'warehouse': 'VIP_BJ',
        'fdc_area_id': '101101101',
        'province_id': '101101',
        'api_key': '70f71280d5d547b2a7bb370a529aeea1',
        'abtestId': '1872',
        'mtmsRuleId': {category_id},
        'scene': 'rule_stream',
        'filterStock': '0',
        'sort': '0',
        'pageOffset': str(pageOffset),
        'salePlatform': '1',
    }
    product_response = session.get('https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/list/rank/rule/v2',
                                   params=product_params).text
    product_json = json.loads(re.findall(r'getProductIdsListRank\((.*?)\)', product_response)[0])
    product_ids = [i.get('pid') for i in product_json['data']['products']]
    return product_ids


def get_merchandise(product_ids):
    """
    获取商品信息
    :param product_ids: 商品id列表
    :return:
    """
    for i in range(0, len(product_ids), 50):  # 一次请求50个商品
        product_cut = product_ids[i:i + 50]
        productIds = ','.join(product_cut)
        params = {
            'callback': 'getMerchandiseDroplets1',
            'app_name': 'shop_pc',
            'app_version': '4.0',
            'warehouse': 'VIP_BJ',
            'fdc_area_id': '101101101',
            'api_key': '70f71280d5d547b2a7bb370a529aeea1',
            'productIds': productIds,
            'scene': 'rule_stream',
            'standby_id': 'nature',

        }

        response = session.get('https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/module/list/v2',
                               params=params)
        time.sleep(5)
        if response.status_code != 200:
            continue
        try:
            data = response.text.replace('getMerchandiseDroplets1(', '')[:-1]
            json_data = json.loads(data)
            products = json_data['data']['products']
            for product in products:
                logger.info(f"店名:{product['brandShowName']},商品名:{product['title']},价格:{product['price']['salePrice']}")
        except Exception as e:
            logger.error(response.text)
            logger.error(f"解析错误:{e}")


if __name__ == '__main__':
    # tags = get_tabs()  # 获取大品类id
    # for tag in tags:
    #     get_category(tag['categoryId'])  # 获取小品类id
    for i in range(1, 10):
        logger.debug(f"=====================正在请求第{i}页========================")
        product_ids = get_product_id(53986307, i)  # 连衣裙id 这里图方便直接复制了
        get_merchandise(product_ids)