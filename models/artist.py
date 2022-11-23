#!/usr/bin/python3
'''module for defining artist ORM'''
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel


class Artist(Base, BaseModel):
    '''class showing ORM for artist table'''
    __tablename__ = 'artist'

    id = Column(String(50), primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    tracks = relationship('Track', cascade='all, delete, delete-orphan')
