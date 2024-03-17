#!/usr/bin/python3
"""
a script that prints the first State
object from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    instance = Session.query(State).order_by(State.id).first()

    print('{0}: {1}'.format(instance.id, instance.name))
