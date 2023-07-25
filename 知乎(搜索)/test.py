import requests


def get_d_c0():
    response = requests.post('https://www.zhihu.com/udid')
    print(response.headers)


if __name__ == '__main__':
    get_d_c0()