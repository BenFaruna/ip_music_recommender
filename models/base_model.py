#!/usr/bin/python3
'''module for defining general structure for all models'''
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    '''class housing gemeral methods for all database models'''

    def __init__(self, **kwargs):
        '''initialisation of model'''
        if kwargs:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def __str__(self):
        '''string representation of object'''
        return '[{}] {}'.format(self.__class__.__name__, self.to_dict())

    def to_dict(self):
        '''converts class into a dictionary'''
        return self.__dict__.copy()
