<<<<<<< HEAD
from sqlalchemy import column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
=======
#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

meta = MetaData()
Base = declarative_base(metadata=meta)

>>>>>>> e42e250bd46dc59dc1e121c8e16a57af56ed7fe6

class State(Base):
    __tablename__ = 'states'
<<<<<<< HEAD
    id = column(Integer, primary_key=True)
    name = column(String(length=100), nullable = False)
=======
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable = False)
>>>>>>> e42e250bd46dc59dc1e121c8e16a57af56ed7fe6
