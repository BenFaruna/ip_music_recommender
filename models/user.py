#!/usr/bin/python3
'''module for defining user table'''
from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel


user_liked_tracks = Table(
    'user_liked_tracks', Base.metadata,
    Column('user_id', String(50), ForeignKey(
        'user.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True),
    Column('track_id', String(50), ForeignKey(
        'track.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
)


class User(Base, BaseModel):
    '''Class defining columns for user table'''

    __tablename__ = 'user'

    id = Column(String(50), unique=True, nullable=False, primary_key=True)
    username = Column(String(40), unique=True, nullable=False)
    password = Column(String(40), nullable=False)
    liked_tracks = relationship('User', secondary=user_liked_tracks,
                                backref='users', viewonly=False)
