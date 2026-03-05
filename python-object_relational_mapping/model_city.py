#!/usr/bin/python3
"""State class definition for use in SQLAlchemy"""

from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_state import State

#  All ORM classes inherit from this.
Base = declarative_base()


class City(Base):
    """State class mapped to the 'cities' table"""
    __tablename__ = 'cities'  # The same one as in MySQL

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    state = relationship("State")

if __name__ == "__main__":
    #  MYSQL connection
    username = 'root'
    password = 'root'
    database = 'hbtn_0e_6_usa'

    engine = create_engine(f"mysql+mysqldb://{username}:{password}"
                           f"@localhost:3306/{database}")
    Base.metadata.create_all(engine)
