import json
from models.base_model import BaseModel

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        return {k: v for k, v in FileStorage.__objects.items() if isinstance(v, cls)}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        serialized_objs = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(serialized_objs, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                serialized_objs = json.load(f)
                for key, obj_dict in serialized_objs.items():
                    cls_name = obj_dict['__class__']
                    cls = eval(cls_name)
                    self.__objects[key] = cls(**obj_dict)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from storage if it exists"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects.pop(key, None)
            self.save()
