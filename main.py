#!/usr/bin/python
# -*-coding:utf-8-*-


from uvicorn import run
# 下面这个不要删除，否则无法运行
from api import app

if __name__ == '__main__':
    print('下面是文档地址:')
    print("http://127.0.0.1:8000/docs")
    run('main:app', reload=True)
