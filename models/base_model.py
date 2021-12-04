#!/usr/bin/python3
'''
Shopper BaseModel Module
========================
'''

import uuid
from datetime import datetime
import models


class BaseModel:
    '''
    BaseModel class that all other models inherits from
    '''
    id = ""
    created_at = None
    updated_at = None
    
    def __init__(self, *args, **kwargs):
        '''
        init method
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''
        Returns string representation of the curent object
        '''
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        '''
        Returns the dictionary representation of the current object
        '''
        obj = {}
        for k, v in self.__dict__.items():
            obj[k] = v
        obj['id'] = self.id
        obj['__class__'] = type(self).__name__
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return obj

    def save(self):
        '''
        updates the public instance attribute of current object
        '''
        self.updated_at = datetime.now()
        models.storage.save()

