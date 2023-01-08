# -*- coding:utf-8 -*-
import json
import time
from base_request import sendPost, sendGet
from rsa_util import rsa_encode

BASE_URL = "https://maas.aminer.cn/api/paas"

ENGINES_PATH = "/model/v1/open/engines/"

ENGINES_PATH_V2 = "/model/v2/open/engines/"

ENGINES_PATH_V3 = "/model/v1/open/engines/generate"

TOKEN_PATH = "/passApiToken/createApiToken"

QUERY_ORDER_RESULT = "/request-task/query-request-task-result"


def getToken(api_key, public_key):
    content = str(int(round(time.time() * 1000)))
    crypto = rsa_encode(content.encode("utf-8"), public_key)
    params = {"apiKey": api_key,
              "encrypted": crypto
              }
    data = sendPost(BASE_URL + TOKEN_PATH, params)
    data = json.loads(data)
    return data


def executeEngine(ability_type, engine_type, auth_token, params, timeout=3000):
    req_engine_api_url = BASE_URL + ENGINES_PATH + ability_type + "/" + engine_type
    data = sendPost(req_engine_api_url, params, auth_token, timeout)
    data = json.loads(data)
    return data


def executeEngineV2(ability_type, engine_type, auth_token, params, timeout=3000):
    req_engine_api_url = BASE_URL + ENGINES_PATH_V2 + ability_type + "/" + engine_type
    data = sendPost(req_engine_api_url, params, auth_token, timeout)
    data = json.loads(data)
    return data


def queryTaskResult(auth_token, taskOrderNo):
    api_url = BASE_URL + QUERY_ORDER_RESULT + "/" + taskOrderNo
    task_data = sendGet(api_url, auth_token)
    data = json.loads(task_data)
    return data
