#!/usr/bin/python3
'''module containing storage engine class
'''
import models

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models.base_model import Base, BaseModel
from models.artist import Artist
from models.track import Track
from models.user import User


classes = {'Artist': Artist, 'Track': Track, 'User': User}

class Storage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://root:neodynamics@localhost/music_recommender')

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.id
                    new_dict[key] = obj
        return (new_dict)

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def new(self, obj):
        '''add object to the current database session'''
        self.__session.add(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()