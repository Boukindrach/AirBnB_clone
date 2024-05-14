#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime

class BaseModel:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

   def  save(self):
       self.update_at = datetime.now()




    def __str__(self):
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)
