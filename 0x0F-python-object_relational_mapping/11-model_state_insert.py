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
    state1 = State(name="Louisiana")
    session.add(state1)
    session.commit()
    state = session.query(State).where(State.name == 'Louisiana').first()
    print(state.id)
    session.close()
