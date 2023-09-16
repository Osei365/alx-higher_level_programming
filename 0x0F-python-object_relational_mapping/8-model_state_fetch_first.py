#!/usr/bin/python3
"""The module connects to a database and
prints the states present."""

import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    first_state = session.get(State, 1)
    if first_state is not None:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print('Nothing')
    session.close()
