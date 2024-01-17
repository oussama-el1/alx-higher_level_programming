from sqlalchemy.orm import declarative_base
from sqlalchemy import column, String, Integer

Base = declarative_base()
class State(Base):
    __tablename__ = 'states'
    id = column(Integer, primary_key=True)
    name = column(String(length=100), nullable = False)