#!/usr/bin/python3
"""Defines a class to manage db storage for hbnb clone v2"""

from os import getenv, remove

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.engine.url import URL
from sqlalchemy.orm.session import Session

from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class DBStorage():
    """This class manages storage in a database"""

    __engine = None
    __session = None

    classes = [Amenity, City, Place, Review, State, User]

    def __init__(self):
        """Initiates the DBStorage class"""

        mySQL_u = getenv("HBNB_MYSQL_USER")
        mySQL_p = getenv("HBNB_MYSQL_PWD")
        db_host = getenv("HBNB_MYSQL_HOST")
        db_name = getenv("HBNB_MYSQL_DB")


        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                .format(mySQL_u, mySQL_p, db_host, db_name),
                pool_pre_ping=True)

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """Returns a dictionary of models currently in database"""

        objs = []
        dct = {}
        if not cls:
            for item in self.classes:
                objs.extend(self.__session.query(item).all())
        else:
            if type(cls) is str:
                cls = eval(cls)
            objs = self.__session.query(cls).all()

        for obj in objs:
            dict[obj.__class__.__name__ + '.' + obj.id] = obj
        return dict
   
    def new(self, obj):
        """Adds the object to the database"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables of the database"""
        Base.metadata.create_all(self.__engine)

        s_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(s_factory)
        self.__session = Session()

    def close(self):
        """Handles close of DBStorage"""
        self._session.close()

