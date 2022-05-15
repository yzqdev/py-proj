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
html='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<p>Hi this test mail, thanks for using Fastapi-mail</p>

<pre>
    <code>
       @app.post("/email")
async def simple_send(
        email: EmailSchema
) -> JSONResponse:
    message = MessageSchema(
        subject="this is subject",
        recipients=email.dict().get("email"),  # List of recipients, as many as you can pass
        body=html,
        subtype="html"
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})

    </code>
</pre>
</body>
</html>'''