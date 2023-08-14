import blackboxprotobuf
import requests
import json
from parsel import Selector

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/grpc-web+proto',
    # 'Cookie': 'zh_choose=n; Hm_lvt_838fbc4154ad87515435bf1e10023fab=1691981969; UM_distinctid=189f1fbf5571a0c-092aed6c1a2da-26031c51-1fa400-189f1fbf55811e8; CNZZDATA1281185085=753427800-1691979600-%7C1691979600; uv_token=wXzw1HHjdbB5Pt2LMF_S; SL_G_WPT_TO=zh-CN; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; Hm_lpvt_838fbc4154ad87515435bf1e10023fab=1691982524',
    'Cookies': 'CASTGC=;CASTGCSpecial=;',
    'Origin': 'https://s.wanfangdata.com.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://s.wanfangdata.com.cn/periodical?q=%E8%8B%B9%E6%9E%9C',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'X-Grpc-Web': '1',
    'X-User-Agent': 'grpc-web-javascript/0.1',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = '\x00\x00\x00\x00\x1f\n\x1b\n\nperiodical\x12\x06苹果(\x010\x14B\x01\x00\x10\x01'.encode()

response = requests.post(
    'https://s.wanfangdata.com.cn/SearchService.SearchService/search',
    headers=headers,
    data=data,
)
deserialize_data, message_type = blackboxprotobuf.protobuf_to_json(response.content)
json_data = json.loads(deserialize_data)
select = Selector(text=json_data['4'][0]['101'])
a = 1

with open('test.html', 'w', encoding='utf-8') as f:
    f.write(json_data['4'][0]['101'])
print(json_data['4'][0])