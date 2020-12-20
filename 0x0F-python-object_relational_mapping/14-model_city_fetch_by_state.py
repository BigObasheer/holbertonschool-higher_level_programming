#!/usr/bin/python3
""" Prints all City objects from the database hbtn_0e_14_usa """
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import City


if __name__ == "__main__":

    user, passwd, database = argv[1], argv[2], argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, database), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City, State).join(State,
                                             City.state_id == State.id).all()
    for cities, states in result:
        print('{}: ({}) {}'.format(states.name, cities.id, cities.name))
