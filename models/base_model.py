#!/usr/bin/python3

import models
import uuid
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel class for other models to inherit from."""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Save the instance to storage."""
        self.update_at = datetime.now()
        Storage.save()

    def to_dict(self):
        """Convert instance to dictionary."""
        dictionary = self.__dict__.copy()
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary['__class__'] = self.__class__.__name__
        return dictionary

    def __str__(self):
        """Return string representation of the instance."""
        return "[] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__)
