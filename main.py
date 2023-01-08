# pip install wudao 请先在终端进行安装，或者到开放平台用户手册中--》》新手指南下载平台调用工具包。
# -*- coding:utf-8 -*-
from wudao.api_request import executeEngineV2, getToken, queryTaskResult

# 接口API KEY
API_KEY = "c8ca83fc49a6469db090c1a9c5ab4f4c"
# 公钥
PUBLIC_KEY = "MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAJcQeIuNq2yYlkDxoU1qJi9P5sCJkpDhnwb2RpnKQ2aSIZi/FruXOWFSypIR9HwUcXw7ae2S9SNG0JzYPRey/fMCAwEAAQ=="

# 能力类型
ability_type = "poem"
# 引擎类型
engine_type = "poem-generate"
# 请求参数样例
data = {
    "requestTaskNo": "45",
    "author": "李白",
    "prompt": "过年，春节，正月，除夕",
    "topicType": "normal"
}

'''
  注意这里仅为了简化编码每一次请求都去获取token， 线上环境token有过期时间， 客户端可自行缓存，过期后重新获取。
'''
token_result = getToken(API_KEY, PUBLIC_KEY)

if token_result and token_result["code"] == 200:
    token = token_result["data"]
    resp = executeEngineV2(ability_type, engine_type, token, data)
    no = resp['data']['taskOrderNo']
    while True:
        resp_n = queryTaskResult(token, no)
        if resp_n['data']['outputText'] is not None:
            break
    str1 = str(resp_n['data']['outputText'])
    print(str1.split(',')[0])
else:
    print("获取token失败，请检查 API_KEY 和 PUBLIC_KEY")


# 能力类型
ability_type = "couplet_generation"
# 引擎类型
engine_type = "txl-general-engine-v1"
# 请求参数样例
data = {
    "prompt": str1.split(',')[0],
    "requestTaskNo": "46"
}

'''
  注意这里仅为了简化编码每一次请求都去获取token， 线上环境token有过期时间， 客户端可自行缓存，过期后重新获取。
'''
token_result = getToken(API_KEY, PUBLIC_KEY)

if token_result and token_result["code"] == 200:
    token = token_result["data"]
    resp = executeEngineV2(ability_type, engine_type, token, data)
    # print(resp)
    no = resp['data']['taskOrderNo']
    while True:
        resp_n = queryTaskResult(token, no)
        if resp_n['data']['outputText'] is not None:
            break
    print(resp_n['data']['outputText'])
else:
    print("获取token失败，请检查 API_KEY 和 PUBLIC_KEY")
