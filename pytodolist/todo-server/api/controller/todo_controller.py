#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: todo_controller.py
@time: 2022/5/15 23:36
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from  api.curd import  todo_service
from database import engine, SessionLocal, Base

todo_route = APIRouter(tags=["todo相关"])

Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@todo_route.get("/todos", summary="当前用户",)
async def user_info( db: Session = Depends(get_db)):
    """
    - username: str 必传
    - password: str 必传
    """
    return todo_service.get_all_todos(db)