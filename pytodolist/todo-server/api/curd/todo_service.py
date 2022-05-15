#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: todo_service.py
@time: 2022/5/15 23:34
"""
from sqlalchemy.orm import Session
from api.model.todolist_model import TodoList

def get_all_todos(db:Session, ):
    return  db.query(TodoList).all()