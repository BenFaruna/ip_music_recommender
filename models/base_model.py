#!/usr/bin/python3
'''module for defining general structure for all models'''
from sqlalchemy.ext.declarative import declarative_base

import models

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
        new_dict = self.__dict__.copy()
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return '[{}] {}'.format(self.__class__.__name__, new_dict)

    def add(self):
        '''function used to add elements to database'''
        new_obj = models.storage.new(self)
        models.storage.save()

    def delete(self):
        '''function used to remove object from database'''
        models.storage.delete(self)

    def to_dict(self):
        '''converts class into a dictionary'''
        new_dict = self.__dict__.copy()
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

