# -*- coding:utf-8 -*-
import json
import logging

import requests
from requests import exceptions


def sendPost(api_url, params, authorization=None, timeout=240):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    }

    if authorization:
        headers["Authorization"] = authorization

    try:
        resp = requests.post(api_url, data=json.dumps(params), headers=headers, timeout=timeout)
        if requests.codes.ok == resp.status_code:
            return resp.text
    except exceptions.Timeout as e:
        logging.exception('请求超时', e)
    except exceptions.ConnectionError as e:
        logging.exception('请求连接错误', e)
    except exceptions.HTTPError as e:
        logging.exception('http请求错误', e)


def sendGet(api_url, authorization=None):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    }

    if authorization:
        headers["Authorization"] = authorization

    resp = requests.get(api_url, headers=headers)
    if requests.codes.ok == resp.status_code:
        return resp.text
