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

response = requests.get('https://gcaptcha4.geetest.com/load', params=params)
print(response.text)