#!/usr/bin/python3
"""This module Defines the
   BaseModel class.
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """ For Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                tform = "%Y-%m-%dT%H:%M:%S.%f"
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, tform)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """changes updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """This methos Returns the dictionary
        of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return the print/str representation of the
        BaseModel instance.
        """
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
