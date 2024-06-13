#!/usr/bin/python3
'''
    File: file_storage.py
    Defines the FileStorage class.
'''

import json
import models


class FileStorage:
    '''
    Serializes instances to JSON file and deserializes to JSON file.
    '''

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        '''
        Returns the dictionary of all objects or filtered by class name.

        Args:
            cls (str): Class name to filter by (optional).

        Returns:
            dict: Dictionary of objects filtered by class name if provided,
                  otherwise all objects.
        '''
        if cls is None:
            return self.__objects

        filtered_dict = {}
        for key, obj in self.__objects.items():
            if key.split('.')[0] == cls.__name__:
                filtered_dict[key] = obj
        return filtered_dict

    def new(self, obj):
        '''
        Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj (BaseModel): Object instance to be stored.
        '''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        '''
        Serializes __objects to JSON file.
        '''
        serialized_objs = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objs[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w', encoding="UTF8") as file:
            json.dump(serialized_objs, file)

    def reload(self):
        '''
        Deserializes the JSON file to __objects.
        '''
        try:
            with open(FileStorage.__file_path, 'r', encoding="UTF8") as file:
                FileStorage.__objects = json.load(file)
                for key, obj_dict in FileStorage.__objects.items():
                    class_name = obj_dict['__class__']
                    cls = models.classes[class_name]
                    FileStorage.__objects[key] = cls(**obj_dict)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        '''
        Deletes obj from __objects if it exists.

        Args:
            obj (BaseModel): Object instance to be deleted.
        '''
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects.pop(key, None)
            self.save()

    def close(self):
        '''
        Calls reload() method to deserialize JSON file to objects.
        '''
        self.reload()

    def get(self, cls, id):
        '''
        Retrieves an object based on class name and ID.

        Args:
            cls (str): Class name of the object.
            id (str): ID of the object.

        Returns:
            obj: Object instance if found, None if not found.
        '''
        obj_dict = self.all(cls)
        for key, obj in obj_dict.items():
            if obj.id == id:
                return obj
        return None

    def count(self, cls=None):
        '''
        Counts number of objects in a class (if given).

        Args:
            cls (str): Class name (optional).

        Returns:
            int: Number of objects in the class or total objects if cls is None.
        '''
        return len(self.all(cls))
