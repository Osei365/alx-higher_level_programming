#!/usr/bin/python3
"""
Satate table creation using sqlalchemy
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """represents the State class for sql table state."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    mb = 'City'
    cities = relationship(mb, backref='state', cascade="all, delete-orphan")
