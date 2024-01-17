from sqlalchemy import column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class State(Base):
    __tablename__ = 'states'
    id = column(Integer, primary_key=True)
    name = column(String(length=100), nullable = False)
