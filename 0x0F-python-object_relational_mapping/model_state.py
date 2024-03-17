#!/usr/bin/python3
"""
python file that contains the class definition
of a State and an instance Base = declarative_base():
"""
from sqlalchemy import column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class state(Base):
    """
    definition of a State properties
    """
    __tablename__ = 'states'

    id = column(Integer, primary_key=True)
    name = column(String(128, nullable=False))

