import requests

cookies = {
    '_lxsdk_cuid': '189f6f7eab4c8-03b0f9301ae80c-26031c51-1fa400-189f6f7eab4c8',
    '_lxsdk': '189f6f7eab4c8-03b0f9301ae80c-26031c51-1fa400-189f6f7eab4c8',
    '_hc.v': '14a2cd21-cfb9-623c-ac1c-46057669e643.1692065590',
    'WEBDFPID': '2y69u7uv6z295uy00x1x5zw9152u3y53810u3u2vw6x9795814xy9369-2007425590219-1692065589840UGQUWCMfd79fef3d01d5e9aadc18ccd4d0c95071424',
    '_lx_utm': 'utm_source%3DBaidu%26utm_medium%3Dorganic',
    'SL_G_WPT_TO': 'zh-CN',
    'SL_GWPT_Show_Hide_tmp': '1',
    'SL_wptGlobTipTmp': '1',
    'qruuid': 'd4e4df1e-cecf-4cec-863e-b53c174b0fc1',
    '_lxsdk_s': '189f8c6fe65-28c-4d1-e07%7C%7C6',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': '_lxsdk_cuid=189f6f7eab4c8-03b0f9301ae80c-26031c51-1fa400-189f6f7eab4c8; _lxsdk=189f6f7eab4c8-03b0f9301ae80c-26031c51-1fa400-189f6f7eab4c8; _hc.v=14a2cd21-cfb9-623c-ac1c-46057669e643.1692065590; WEBDFPID=2y69u7uv6z295uy00x1x5zw9152u3y53810u3u2vw6x9795814xy9369-2007425590219-1692065589840UGQUWCMfd79fef3d01d5e9aadc18ccd4d0c95071424; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; SL_G_WPT_TO=zh-CN; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; qruuid=d4e4df1e-cecf-4cec-863e-b53c174b0fc1; _lxsdk_s=189f8c6fe65-28c-4d1-e07%7C%7C6',
    'Origin': 'https://account.dianping.com',
    'Pragma': 'no-cache',
    'Referer': 'https://account.dianping.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'mtgsig': '{"a1":"1.1","a2":1692095981459,"a3":"2y69u7uv6z295uy00x1x5zw9152u3y53810u3u2vw6x9795814xy9369","a5":"BxCkYXUevfHRwwgYqqiyiI9pu2l30jNlDc==","a6":"h1.5kMCrr3ii+jT9CcFUxnDmAPkClHnSOr7RnrGXZMsq/hnN9yFCLpJbBcIK1Cr+FZj4ax1EVjp+KM8iy2mTCbQ/FGQnzZmdKVoWBklIdPZ5Avf7QGTg57JwUq1Qo0LERaJXTFdzS3cJ06rJg2dwikSN8AI9oiHCIjv53MZ2ju3b9S9G9HQwZ0QhROtlTk37ZvY21gUQNzqH22af3Ex8e0iMROfru2nqARJHgQarfuvG50cjaAP1jUpTiPMDG5j32yUJQLjWASfLDvY5FYl5nwoYAJekIocWyTfpqaw9FC8/14Yxy66sy+5CpX3TTjgovQ3E2I3KcuwbMUWfAylRRPCqDiRiJr8rbcEgfiA0xvIHaZ1m2IFZu6q8QQp6JrRGn95kTRfLrhz5yyXnGvNnn1foTA==","x0":4,"d1":"8031406b2fc1f2198b2e022baff0b261"}',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'yodaReady': 'h5',
    'csecplatform': '4',
    'csecversion': '2.1.2',
}

data = {
    'encryptMobile': 'QfbOqcmtzn5nZPTOb3/N+KdwzF1/fWyTEsQS/6zDADo3iIt2Sn6/IAziDLWLPTRNWhI8J+UpuwzcPuIicDV51uk+ZxRm+gIq1WdnZU/Ly2asr3O+55acifNGabBOZbNczb7TAsjKfXRD6hguK8l9+i1mZdLvyLub5a+ZsueFhYNTKTVA7lrp20xC9NlD2PcoNPBjgqZYYlon6OhMSVZxZURYsIP/vbmQzyHLhXpIJ/dNDhfGEPWtylgcfRvoNvjUHHxMn3/ukmQc82gajYAU499Aj6ZQdQy9GhAN/KMLiB4MsOerIuN0JwCKWbAQYK0RGDi4cWU3HCvoue7gaVijEA==',
    'countryCode': '86',
    'encryptPassword': 'fjxmhO/MI0WTfMA9QdTeDE80dIo4y61gV+97iBv1P2YRpfJztdYajspXuAVUq7L1FSSd/FNu7kT123oKCt3xejrhKetF4uq5/U2uUBWh5iWcWO63PdIvY0b4z6XzkRfZ2p5aDG4zUN+E3VAjh9Fte4RAdFrCHvW6IDx2FbozaFY=',
    'uuid': '189f6f7eab4c8-03b0f9301ae80c-26031c51-1fa400-189f6f7eab4c8',
    'cx': 'cxcxcx',
    'setCookie': 'true',
    'platform': '1',
    'siteType': 'PC',
    # 'h5_fingerprint': 'H5dfp_2.1.2_tttt_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',
}

response = requests.post(
    'https://accountapi.dianping.com/mlogin/dp/api/v1/account/passwordlogin/login',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
print(response.text)