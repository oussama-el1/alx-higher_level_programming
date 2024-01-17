#!/usr/bin/python3
"""
imported module
"""
import sys
from model_state import State, Base
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    citys = session.query(State.name, City.id, City.name).\
        filter(State.id == City.state_id)
    for city in citys:
        print(city[0] + ": " + "(" + str(city[1]) + ") "
              + city[2])
