#!/usr/bin/python3
'''
    Definition of DBStorage class
'''
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
import models


class DBStorage:
    '''
        DBStorage class for managing SQLAlchemy database
    '''
    __engine = None
    __session = None

    def __init__(self):
        '''
            Initializes DBStorage with connection parameters
        '''
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env_var = getenv("HBNB_ENV", "none")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)
        if env_var == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''
            Returns a dictionary of objects from the current database session
        '''
        objects_dict = {}

        if cls:
            if isinstance(cls, str):
                cls = models.classes[cls]
            objects = self.__session.query(cls).all()
        else:
            for cls in models.classes.values():
                if hasattr(cls, '__tablename__'):
                    objects = self.__session.query(cls).all()

        for obj in objects:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            objects_dict[key] = obj
        return objects_dict

    def new(self, obj):
        '''
            Adds the object to the current database session
        '''
        self.__session.add(obj)

    def save(self):
        '''
            Commits all changes of the current database session
        '''
        self.__session.commit()

    def delete(self, obj=None):
        '''
            Deletes an object from the current database session
        '''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        '''
            Creates all tables in the database and initializes a session
        '''
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

    def close(self):
        '''
            Closes the private session attribute
        '''
        self.__session.close()

    def get(self, cls, id):
        '''
            Retrieves an object by class name and ID
        '''
        key = "{}.{}".format(cls, id)
        return models.storage.all(cls).get(key, None)

    def count(self, cls=None):
        '''
            Counts the number of objects in a class
        '''
        if cls:
            return len(self.all(cls))
        return sum(len(self.all(cls)) for cls in models.classes.values())
