#!/usr/bin/python3
"""
import nedded
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    session = Session(bind=engine)
    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        print(str(state.id) + ": " + state.name)
