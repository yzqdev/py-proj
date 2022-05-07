#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: user_service.py
@time: 2022/3/20 15:13
"""
from sqlalchemy.orm import Session

from api import model
from api.dto.user_dto import UserCreate
from api.model.user_model import User

# Dependency
from database import SessionLocal

def get_user_by_email(db: Session, email: str):
    return db.query( User).filter( User.email == email).first()

def create_user(db: Session, user_create: UserCreate):
    fake_hashed_password = user_create.password + "notreallyhashed"
    db_user =  User(email=user_create.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query( User).filter( User.id == user_id).first()
