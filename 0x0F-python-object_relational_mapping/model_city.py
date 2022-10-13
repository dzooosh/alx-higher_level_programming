#!/usr/bin/python3
""" contains the class definition of a City """

from sqlalchemy.ext.declarative import declarative_base
from model_state import Base
from sqlalchemy import String, Column, Integer, ForeignKey

class City(Base):
    """ Class that defines each City """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

