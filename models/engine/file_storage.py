#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Retrieve all stored objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the storage"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize objects to a JSON file."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserialize the JSON file to objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for value in obj_dict.values():
                    cls_n = value["__class__"]
                    del value["__class__"]
                    self.new(eval(cls_n)(**value))
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    class_ = self.__objects.get(class_name)
                    if class_:
                        self.__objects[key] = class_(**value)
        except FileNotFoundError:
            return
