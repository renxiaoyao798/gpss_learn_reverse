import execjs
import requests
from urllib.parse import urlencode
jrtt = open('sign.js', encoding='utf-8').read()
jrtt_exc = execjs.compile(jrtt)


params = {
    'offset': '0',
    'channel_id': '0',
    'max_behot_time': '0',
    'category': 'pc_profile_channel',
    'disable_raw_data': 'true',
    'aid': '24',
    'app_name': 'toutiao_web',
}
params_url_encode = "https://www.toutiao.com/api/pc/list/feed?" + urlencode(params)
sign = jrtt_exc.call('get_sign', params_url_encode)
params.update({'_signature': sign})
response = requests.get('https://www.toutiao.com/api/pc/list/feed', params=params)
if response.status_code == 200:
    a = response.json()

print(response.json())