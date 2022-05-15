import json
import time

from sqlalchemy import Column
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base
class TodoList(Base):
    __tablename__ = 'todolist'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    title = Column(String(1024), nullable=False)
    status = Column(Integer, nullable=False)
    create_time = Column(Integer, nullable=False)

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
