from random import randint

from flask import Flask,request,render_template,url_for,redirect
from wudao.api_request import executeEngineV2, getToken, queryTaskResult
from django.shortcuts import render

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit_result', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        prompt = request.form['promtp']
    elif request.method == 'GET':
        prompt = request.args.get('prompt')

    ##########################################################################################################
    API_KEY = "c8ca83fc49a6469db090c1a9c5ab4f4c"
    PUBLIC_KEY = "MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAJcQeIuNq2yYlkDxoU1qJi9P5sCJkpDhnwb2RpnKQ2aSIZi/FruXOWFSypIR9HwUcXw7ae2S9SNG0JzYPRey/fMCAwEAAQ=="
    ability_type = "tangPoetry"
    engine_type = "text-general-engine-v1"
    num = randint(1,99999)
    data = {
        "topP": 1,
        "topK": 5,
        "temperature": 1,
        "requestTaskNo": str(num),
        "prompt": prompt,
        "endTokens": ["<n>"]
    }
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
        hstr1 = str1.split(',')[0]
    else:
        print("获取token失败，请检查 API_KEY 和 PUBLIC_KEY")

    ability_type = "couplet_generation"
    engine_type = "txl-general-engine-v1"
    data = {
        "prompt": str1.split(',')[0],
        "requestTaskNo": str(num+1)
    }
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
        hstr2 = resp_n['data']['outputText']
    else:
        print("获取token失败，请检查 API_KEY 和 PUBLIC_KEY")
    ##########################################################################################################
    return render_template( 'indexshow.html', hstr1=hstr1, hstr2=hstr2)# str1.split(',')[0] + ‘  ’ + str2

if __name__ == '__main__':
    app.run(debug=True, port=8080)
