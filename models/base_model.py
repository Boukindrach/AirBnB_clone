#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime

class BaseModel:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def  save(self):
       self.update_at = datetime.now()
       models.storage.save()

    def __str__(self):
        return "[] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
