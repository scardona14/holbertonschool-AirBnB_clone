#!/usr/bin/python3
"""Module user"""
from datetime import datetime
from models import base_model
import models


class User(base_model.BaseModel):
    """User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(*args, **kwargs)
        models.storage.new(self)

    def __str__(self):
        """String method"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """Save method"""
        self.updated_at = datetime.now()
        models.storage.save()
    
    def to_dict(self):
        """To dictionary method"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
