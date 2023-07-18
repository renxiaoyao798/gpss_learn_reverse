import execjs
import requests



rsa_code = open('RSA.js', encoding='utf-8').read()
rsa = execjs.compile(rsa_code)
aes_code = open('AES.js', encoding='utf-8').read()
aes = execjs.compile(aes_code)


def get_privakey():
    privakey = aes.call('getAesKey', 16)
    return privakey


def get_rsa_key(privakey):
    rsa_key = rsa.call('getRsaResult', privakey)
    return rsa_key


def get_aes_key(login_data, privakey):
    aes_key = aes.call('aes_encryt', login_data, privakey)
    return aes_key

login_data = {
    "body": {
        "loginMethod": "1",
        "name": "13933566015",
        "password": "woshitiancai666"
    },
    "head": {
        "userCode": None,
        "channelCode": "101",
        "transTime": 1689648799335,
        "transToken": "",
        "customerId": None,
        "transSerialNumber": ""
    }
}
def simulate_request(login_data):
    privakey = get_privakey()
    rsa_key = get_rsa_key(privakey)
    aes_key = get_aes_key(login_data, privakey)
    headers = {
        'key': rsa_key,
    }
    params = {
        'jsonKey': aes_key,
    }
    json_data = {
        'jsonKey': aes_key
    }
    response = requests.post(
        'https://tianaw.95505.cn/tacpc/tiananapp/customer_login/taPcLogin',
        params=params,
        # cookies=cookies,
        headers=headers,
        json=json_data,
    )
    if response.json().get('returns'):
        encryctReturns = response.json().get('returns').get('encryctReturns')
        aes_decryt = aes.call('aes_decryt', encryctReturns, privakey)
        print(aes_decryt)


if __name__ == '__main__':
    simulate_request(login_data)