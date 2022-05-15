#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: use.py
@time: 2022/3/20 14:21
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.curd import user_service

from api.model import user_model
from api.schema.user import UserBase,UserCreate
from database import SessionLocal, Base, engine

user_route = APIRouter(tags=["用户相关"])

Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@user_route.get("/users", summary="当前用户",)
async def user_info( db: Session = Depends(get_db)):
    """
    - username: str 必传
    - password: str 必传
    """
    return user_service.get_all_users(db)


@user_route.post("/users/", response_model=UserBase, summary="当前用户")
def create_user(ucreate: UserCreate, db: Session = Depends(get_db)):
    db_user = user_service.get_user_by_email(db, email=ucreate.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_service.create_user(db=db, user_create=ucreate)


@user_route.get("/getUser/{user_id}", summary="当前用户")
async def get_user_route(user_id: int, db: Session = Depends(get_db)):
    """
    - username: str 必传
    - password: str 必传
    """
    db_user = user_service.get_user(db, user_id)
    return db_user
