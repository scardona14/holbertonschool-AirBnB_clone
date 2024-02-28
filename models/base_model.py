#!/usr/bin/python3
"""This module contains the BaseModel class for the AirBnB clone"""
from uuid import uuid4
from datetime import datetime
import models
format_ = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:

    """Base class for AirBnB clone
    id: string - assign with an uuid when an instance is created
    created_at: original datetime
    updated_at: datetime of the last update
    save(self): updates updated_at with the current datetime
    to_dict(self): returns a dictionary containing all keys/values of __dict__
    __str__: should print: [{lass name}] ({self.id}) {self.__dict__}
    """

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__ = datetime.strptime(value, format_)
                elif key == '__class__':
                    value = self.__class__
                else:
                    setattr(self, key, value)
            else:
                models.storage.new(self)

        def __str__(self):
            """String representation of the BaseModel class"""
            return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

        def save(self):
            """Updates the updated_at attribute with the current datetime"""
            self.updated_at = datetime.now()
            models.storage.save()

        def to_dict(self):
            """Returns a dictionary containing all keys/values of __dict__"""
            nt = self.__dict__.copy()
            nt["created_at"] = self.created_at.isoformat()
            nt["updated_at"] = self.updated_at.isoformat()
            nt["__class__"] = self.__class__.__name__

            return nt
