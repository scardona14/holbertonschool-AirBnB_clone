#!/usr/bin/python3
"""
File Storage
"""
import json
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models.base_model import BaseModel


class FileStorage:
    """
    File storage WIP
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        k = "{}.{}".format(obj.__class__.__name__, obj.id)
        # k = f"{self.obj.__class__.__name__}.{obj.id}"
        self.__objects[k] = obj

    def save(self):
        """
        Function that writes an object to text file,
        using a JSON representation.
        """
        dic = {}
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            for k, v in self.__objects.items():
                dic[k] = v.to_dict()
            json.dump(dic, f)

    def reload(self):
        """Reloading"""
        try:
            with open(self.__file_path, 'r') as f:
                d = json.load(f)
                for v in d.values():
                    val = v['__class__']
                    del v['__class__']
                    self.new(eval(val)(**v))
        except FileNotFoundError:
            pass

    def class_dict(self):
        dict_ = {
            "State": State(),
            "City": City(),
            "Amenity": Amenity(),
            "Place": Place(),
            "Review": Review(),
            "User": User(),
            "BaseModel": BaseModel()}
        return dict_
