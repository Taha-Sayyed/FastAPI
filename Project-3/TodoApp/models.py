#models.py is a way for SQL alchemy to be able to underatnd what kind of database tables we are going to create in future

from database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Todos(Base):
    __tablename__='todos'
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    description=Column(String)
    priority=Column(Integer)
    complete=Column(Boolean,default=False)