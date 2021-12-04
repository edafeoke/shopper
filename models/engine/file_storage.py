#!/usr/bin/python3
'''
FileStorage module
==================
'''

from models.base_model import BaseModel
import json
from os.path import exists
import models


class FileStorage:
    '''
    FileStorage
    ===========
    A class that serializes instances to a JSON file
    and deserializes JSON file to instances.

    Private class attributes:
    -------------------------
         __file_path:
            string - path to the JSON file (ex: file.json)

         __objects:
            dictionary - empty but will store all objects
     '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        returns the dictionary __objects
        '''
        return self.__objects

    def new(self, obj):
        '''
        sets in __objects the obj with key <obj class name>.id
        '''
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''
        serializes __objects to the JSON file
        '''
        json_object = {}
        for key, value in self.__objects.items():
            json_object[key] = value.to_dict()
        json_str = json.dumps(json_object)

        with open(self.__file_path, 'w') as f:
            f.write(json_str)

    def reload(self):
        '''
        deserializes the JSON file to __objects
        '''
        if exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                data = f.read()
                json_object = json.loads(data)
                for k, v in json_object.items():
                    classname, _ = k.split(".")
                    Class = globals()[classname]
                    print(v,"\n-------------\n")
                    obj = Class(v)
                    print(obj)
