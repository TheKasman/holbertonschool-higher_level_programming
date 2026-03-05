#!/usr/bin/python3
"""State class definition for use in SQLAlchemy"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    #  MYSQL connection
    USER_NAME = 'root'
    PASSWORD = 'root'
    DATABASE = 'hbtn_0e_6_usa'

    engine = create_engine(f"mysql+mysqldb://{USER_NAME}:{PASSWORD}"
                           f"@localhost:3306/{DATABASE}")

    Session = sessionmaker(bind=engine)
    session = Session()

    #  This is it. this is the SQL query now.
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
