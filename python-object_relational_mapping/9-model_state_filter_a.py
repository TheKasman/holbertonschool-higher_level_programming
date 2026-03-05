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
    states = session.query(State)\
        .filter(State.name.like("%a%"))\
        .order_by(State.id).first()

    for state in states:
        print(f"{state.id}: {state.name}")
