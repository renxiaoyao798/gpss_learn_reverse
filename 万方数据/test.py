# import blackboxprotobuf
# data = '''
# 
# 
#
# periodical苹果(0B
# '''.encode()
# deserialize_data, message_type = blackboxprotobuf.protobuf_to_json(data)
# print(deserialize_data)
# print(message_type)


import blackboxprotobuf
# 1、得到消息类型message_type
with open(r"data_test.bin", "rb") as fp:
    data = fp.read()
    deserialize_data, message_type = blackboxprotobuf.protobuf_to_json(data)

    print(f"原始数据: {deserialize_data}")
    print(f"消息类型: {message_type}")  # 消息类型
    serialize_data = blackboxprotobuf.protobuf_to_json(deserialize_data.encode(), message_type.encode())
    print(f"序列化数据: {serialize_data}")

param = {
  "0": "31",
  "1": {
    "1": "periodical",
    "2": "苹果",
    "5": "1",
    "6": "20",
    "8": "\u0000"
  },
  "2": "1"
}

param_type = {
    '0': {'type': 'int', 'name': ''},
    '1': {'type': 'message',
          'message_typedef':
              {'1': {'type': 'bytes', 'name': ''},
               '2': {'type': 'bytes', 'name': ''},
               '5': {'type': 'int', 'name': ''},
               '6': {'type': 'int', 'name': ''},
               '8': {'type': 'bytes', 'name': ''}},
          'name': ''},
    '2': {'type': 'int', 'name': ''}}

# ————————————————
# 版权声明：本文为CSDN博主「普通网友」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/m0_67393593/article/details/123423619