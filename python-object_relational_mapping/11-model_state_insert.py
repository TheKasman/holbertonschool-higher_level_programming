#!/usr/bin/python3
"""State class definition for use in SQLAlchemy"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    #  MYSQL connection
    USER_NAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    DATABASE = sys.argv[3]

    engine = create_engine(f"mysql+mysqldb://{USER_NAME}:{PASSWORD}"
                           f"@localhost:3306/{DATABASE}")

    Session = sessionmaker(bind=engine)
    session = Session()

    #  This is it. this is the SQL query now.
    state = session.query(State).filter(State.id == 2).first()

    if state is None:
        # If the state doesn’t exist, create it
        state = State(name="New Mexico")
        session.add(state)
    else:
        # If it exists, update the name
        state.name = "New Mexico"

    if state:
        print(state.id)
