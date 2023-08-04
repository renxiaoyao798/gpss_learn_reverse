import requests



headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'FSSBBIl1UgzbN7N80T=4YrcEohLJqD0_IU8HGg1zb5_2.cMZKkWQ9JsK6e9seKHqw0ONA2jX_SsuvdSeQgJFTW9VmGuM84Itn1wom2IZoSsCkhS9La7_JCXwut7ugYAF49CmDFpyVmJwNSltapA4ybu_ETLwqM3prLA0xz3PGckAeEvaSRGbO9KbNqQkcD9TSDoQoUlOPJQAOa0qV5grnQvof4hX66tKMOS9QfBl9Y0_r5MVOzDKWs7ONGAHhUF9fYz0LX8BxLII58dqydIkmXmn9Am39m25nLdsa8JDt1kBmBTqCokpSajQyt4jCcrvIH.LeIE_Eh9yo0PiurI4nt_NVKvyQ5SEG2.0H1HmsayAks633qKbS1ZiFe0coVBwId3V4m6fBBrhopprJV4RIU0; SL_G_WPT_TO=zh-CN',
    'Pragma': 'no-cache',
    'Referer': 'http://www.fangdi.com.cn/old_house/old_house.html',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

response = requests.get('http://www.fangdi.com.cn/new_house/new_house.html', headers=headers, verify=False)
with open('test.html', 'w', encoding='utf-8') as f:
    f.write(response.text)