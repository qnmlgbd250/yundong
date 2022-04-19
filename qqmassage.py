# -*- coding: utf-8 -*-
# @Time    : 2022/4/18 20:38
# @Author  : huni
# @Email   : zcshiyonghao@163.com
# @File    : qqmassage.py
# @Software: PyCharm
import os
from dotenv import load_dotenv
load_dotenv()
from twilio.rest import Client

def send_massage(massag_,phonenumber):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                  body=massag_,
                                  from_=f"{os.environ.get('TRIAL_NUMBER')}",
                                  to=f"+86{phonenumber}"
                              )
    print(message.sid)

