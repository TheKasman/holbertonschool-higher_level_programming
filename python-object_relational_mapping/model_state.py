#!/usr/bin/python3
"""State class definition for use in SQLAlchemy"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

#  All ORM classes inherit from this.
Base = declarative_base()


class State(Base):
    """State class mapped to the 'states' table"""
    __tablename__ = 'states'  # The same one as in MySQL

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


#  MYSQL connection
username = 'root'
password = 'root'
database = 'hbtn_0e_6_usa'

engine = create_engine(f"mysql+mysqldb://{username}:{password}"
                       f"@localhost:3306/{database}")
Base.metadata.create_all(engine)
