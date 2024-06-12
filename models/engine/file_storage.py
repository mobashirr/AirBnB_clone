'''
sereliztion and deserelization process
'''


import datetime
import json
import os,sys
from models.base_model import BaseModel


class FileStorage:
    ''''''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj
        self.save()

    def save(self):
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):

        if os.path.exists(self.__file_path) and os.path.getsize(self.__file_path) != 0:
            try:
                with open(self.__file_path, 'r') as f:
                    deserialized_objs = json.load(f)
                    
                    for key, data in deserialized_objs.items():
                        if '__class__' in data and data['__class__'] == 'BaseModel':
                            self.__objects[key] = BaseModel(**data)
            except json.decoder.JSONDecodeError as e:
                print("Error decoding JSON:", e)
            except Exception as e:
                print("An error occurred:", e)
