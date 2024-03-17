#!/usr/bin/python3
"""
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{} \
        '.format(argv[1], argv[2], argv[2]))
    Session = sessionmaker(bind=engine)
    for instance in Session.query(State).order_by(state.id):
        print('{0}: {1}'.format(instance.id, instance.name))
