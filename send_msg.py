# -*- coding: utf-8 -*-
# @Time    : 2022/4/18 20:38
# @Author  : huni
# @Email   : zcshiyonghao@163.com
# @File    : send_msg.py
# @Software: PyCharm
# import os
# from dotenv import load_dotenv
# load_dotenv()
# from twilio.rest import Client
#
# def send_massage(massag_,phonenumber):
#     account_sid = os.getenv('TWILIO_ACCOUNT_SID')
#     auth_token = os.getenv('TWILIO_AUTH_TOKEN')
#     client = Client(account_sid, auth_token)
#
#     message = client.messages.create(
#                                   body=massag_,
#                                   from_=f"{os.environ.get('TRIAL_NUMBER')}",
#                                   to=f"+86{phonenumber}"
#                               )
#     print(message.sid)


import requests
import json
from tools import Log
log = Log()


def send_notice(msg):
    url = f"https://hook.jijyun.cn/v1/accept/data/webhook_accept_first?apikey=zflcJ0hZCsrmFq9j5VIebHpNwMGgYWR1"
    data = {
        'msg': msg
    }
    response = requests.request("POST", url, data=json.dumps(data)).json()
    if response['Code'] == 200:
        log.success('发送成功')
    else:
        log.error('发送失败')
send_notice('测试')

