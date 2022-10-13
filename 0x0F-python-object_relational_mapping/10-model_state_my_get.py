#!/usr/bin/python3
""" prints the state objects with name passed as argument
    to table in database
    """

import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State.id).filter(State.name == (sys.argv[4],))
    if (instance.first() is None):
        print("Not found")
    else:
        print(instance.first()[0])
