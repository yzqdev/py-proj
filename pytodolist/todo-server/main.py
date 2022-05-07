#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List

from fastapi import (
    FastAPI
)
from fastapi_mail import FastMail, MessageSchema
from pydantic import EmailStr, BaseModel
from starlette.responses import JSONResponse

from email_config import conf, html


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


SECRET_KEY = 'This is my key'


class EmailSchema(BaseModel):
    email: List[EmailStr]


app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items")
async def items():
    stu = Student('zhangsan', 90)
    return {"items": stu}


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
