#!/usr/bin/python3
""" Prints all City objects from a database """
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for ins_state, ins_city in (session.query(State, City)
                                .filter(State.id == City.state_id)
                                .order_by(City.id)):
        print("{}: ({}) {}".format(ins_state.name, ins_city.id, ins_city.name))
