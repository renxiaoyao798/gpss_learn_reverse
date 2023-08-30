import requests

cookies = {
    'captcha_v4_user': '1e45c63aaaa84876bf5e64eaf370836a',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'captcha_v4_user=1e45c63aaaa84876bf5e64eaf370836a',
    'Pragma': 'no-cache',
    'Referer': 'https://gt4.geetest.com/',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    # 'callback': 'geetest_1693278954122',
    'captcha_id': '54088bb07d2df3c46b79f80300b0abbe',
    # 'client_type': 'web',
    'lot_number': 'd0640efc9a494563b8c5dd4d49af6f09',
    # 'risk_type': 'slide',
    # 'payload': 'xSJqOy81RFro17RrPzpVazZRIxU1Fw2O9byeoXMcr-hfL6ZLmZuo3jdaAx7kceM9l-RjPte-x7MkPL-BqirBOSRne6Ux5-eqn73FKGOpRueOSG6delN3X-6FYWOPw7oRp7m-Aw6HYKQ0aTefHzlmXX1cEGaxqDO2VrV6z4LkQA1CXeLKKaZ_PQrd2fgsgAU8BV_eyCxf_OBRa0Rivvt3gFeFs_pew5sVfP2RyHIlRPV0pGSMhJgvXcOVxsspwd5RKJmFnzHLkO7K_85fUDEuJ9MXerX2LfXsn3E4_NrABTr3WVa3PU4yupEgPBL6PBnm8WCKKsmB5L0eM9JqmPbFVLVRJ6XgS4jbwvQ_ftbabe2A3UC5fnR-OmMfH6YSYpPbJ9GTrJKLHN5fLIEiPgiWGPo5zzcNlkpLnKJn4asr_R_GQwhon5m6IeWuu1p5vZw1iuocpNj4zA2H41Pfac5hBcJG0kGJWQmL12JsrFHAQGEECveQvGxCLOo2MNyqmSB6OnZahXrKJi1PLHsT9sBY7yydTaLset2rKLtB471qc0pmHGuoDdzsy9HhaHVYUGkKnYJnGBsgHWf8fzpEr3u-KaVzuMDfunS5qvgXhTCo4cJj2DirPCK_9A4Ajz5eDoF1DyuqlGl9emOpWUmXtRqEwQK3bVbl3G7lCv6tQsJXjCUOyCZtK9H0ftSpf5Ax6Khwm0Dd2CSukcPKUcLQXWq9HQ==',
    # 'process_token': '8cb5d4deae3d0bee97fd88219b8c94ec30ca3da34a0df5e8796d40153017177a',

    'w': 'f946adb117f7af3ca5514bac0c2e556127afdd4e53b325163cdfbf5d626bf2b146cfd4e2d2fad732a984338884f8158943b915037ceb234788024f21a8a6c96588094df671e65e0f376fff6e0bcc9555c776c3c213c4b746fab4dd713e1af51ec158dc3f561e63f1423282d89579b10cf3532077c6e5c5f57d675ee6d41e5e396cfb035a4a691d7af087cf13bdf83075e5a08c065d51ffbca8367e90239d260135a337b7e82469b17b246eac380620cfd06c65847a0d79ac3dcded55e9a6f3e57fe333bdd79b27cda8a80ed51435f1751868c0be54fe62647f24cad15142e77dbf10361e3d9fa5de731c682ea6645d201cc1164e1f6ae0639464b378f439a5ec50adb2b0a7f6c08e9605aae55aead09aa2a2af6010a88070c99c210fe900b94dee2f7eb9b03f95802329953c4ee87796815a3ce586011c2d0a24e92f8690af1132d66958ed716ce882fdebc08f308bbc694745c2567b370fbc2e55bb4ed4fced1299da8aa14f043580cc88ac09fee586d0675b25052962d8b09cc8e3823f851bafe3a8d4d5ed4e3ff59eef13e3357bfe7adea2fff6fa12c91228e51c2d64f94c671b6363b81983a2deee15b048d575719477f5c222666fb27a0074c1e7883ae4ca6f108471017b328f02bd3ef689d63560412e94852bfeb1b2e8a88c47d67a0d51dad9731093a97dde1dda827c31beb0d0d4e2e757dc1bfb1b781f19592156d7493d37439758840caa2610ccd381c9a061b55fb9483adcac9d60da4f555029dfcc168623778612a05aed0c4d0e547dcd1626385e3b32b9ac62505fb12f7212c385150acc36262e723e0076b61d79329cb010d052a063f5269e18044ea646d5ff',
}

response = requests.get('https://gcaptcha4.geetest.com/verify', params=params)
print(response.text)