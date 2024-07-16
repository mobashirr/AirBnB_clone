'''
sereliztion and deserelization process
'''


import datetime
import json
import os,sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.city import City
from models.amenity import Amenity
from models.place import Place


classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "Review": Review,
    "City": City,
    "Amenity": Amenity,
    "Place": Place
}


class FileStorage:
    '''
     __file_path: the path to database file
     __obects: is the variable contain the data in form of key and the value of that key as  object

    '''

    __file_path = "file.json"
    __objects = {}
    classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "Review": Review,
    "City": City,
    "Amenity": Amenity,
    "Place": Place
    }

    def all(self):
        return self.__objects

    def new(self, obj):
        '''add a new instance to the filestorge object'''
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj


    def save(self):
        '''save the data in the database file'''
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        '''reload data from database file'''
        if os.path.exists(self.__file_path) and os.path.getsize(self.__file_path) != 0:
            try:
                with open(self.__file_path, 'r') as f:
                    deserialized_objs = json.load(f)

                    for key, data in deserialized_objs.items():
                        if '__class__' in data and data['__class__'] in classes:
                            self.__objects[key] = classes[data['__class__']](**data)
            except json.decoder.JSONDecodeError as e:
                print("Error decoding JSON:", e)
            except Exception as e:
                print("An error occurred:", e)
