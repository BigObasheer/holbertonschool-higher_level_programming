#!/usr/bin/python3
""" Script that lists all State objects from the database hbtn_0e_6_usa """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user, passwd, database = argv[1], argv[2], argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).filter(State.name == argv[4]).all()
    if results != []:
        for states in results:
            print(states.id)
    else:
        print('Not Found')
