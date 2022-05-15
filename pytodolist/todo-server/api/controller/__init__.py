#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: __init__.py.py
@time: 2022/3/20 14:19
"""

from fastapi import APIRouter

from api.controller.todo_controller import todo_route
from api.controller.user import user_route

router = APIRouter( )

router.include_router(user_route)
router.include_router(todo_route)