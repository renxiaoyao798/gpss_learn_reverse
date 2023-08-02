import requests

a = requests.get('https://www.dongchedi.com/motor/searchapi/search_content_pc/?aid=1839&app_name=auto_web_pc&keyword=%E4%BA%94%E8%8F%B1%E5%AE%8F%E5%85%89MINIEV&city_name=%E6%9B%B2%E9%9D%96&search_mode=common&cur_tab=1&offset=0&count=32&motor_source=pc_new&format=json&motor_search_type=0')
x = 1

b = bb['data'][0]['display']['config_params']