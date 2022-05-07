#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: email_config.py
@time: 2022/2/10 23:38
"""
from fastapi_mail import ConnectionConfig

conf = ConnectionConfig(MAIL_USERNAME="",
                        MAIL_PASSWORD="",
                        MAIL_FROM="",
                        MAIL_PORT=587,
                        MAIL_SERVER="",
                        MAIL_FROM_NAME="",
                        MAIL_TLS=True,
                        MAIL_SSL=False,
                        USE_CREDENTIALS=True,
                        VALIDATE_CERTS=True)
