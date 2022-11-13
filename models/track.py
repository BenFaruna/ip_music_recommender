#!/usr/bin/python3
'''module defining track model for songs'''
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship

from base_model import Base, BaseModel


class Track(Base, BaseModel):
    '''class for track table in database'''
    __tablename__ = 'track'

    id = Column(String(40), primary_key=True, nullable=False)
    title = Column(String(250), nullable=False)
    image_url = Column(String(250), nullable=False)
    artist_id = Column(String(40), ForeignKey('artist.id'), nullable=False)
    artist = relationship('Artist', uselist=False)
