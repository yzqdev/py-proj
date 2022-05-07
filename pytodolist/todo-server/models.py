#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import time

from ext import db


class TodoList(db.Model):
    __tablename__ = 'todolist'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(1024), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, title, status):
        self.user_id = user_id
        self.title = title
        self.status = status
        self.create_time = time.time()

    def __getitem__(self, item):
        return getattr(self, item)
    def to_json(self):
        dict_todo = self.__dict__
        return  json.dumps(dict_todo, ensure_ascii=False)


class User( db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), nullable=False)
    password = db.Column(db.String(24), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
