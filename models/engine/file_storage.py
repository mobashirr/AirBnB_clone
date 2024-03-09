import json
import os,sys

class FileStorage:

    def __init__(self) -> None:
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objs = {}
        for key, obj in self.__objects.items():
            try:
                serialized_objs[key] = obj.to_dict()
            except AttributeError as e:
                print(f"Error serializing object {obj}: {e}")

        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objs, f)

    def reload(self):
        if os.path.exists(self.__file_path) and os.path.getsize(self.__file_path) != 0:
            try:
                from models.base_model import BaseModel
                with open(self.__file_path, 'r') as f:
                    deserialized_objs = json.load(f)
                    for key, data in deserialized_objs.items():
                        if not isinstance(data, BaseModel):
                            self.__objects[key] = BaseModel(**data)
                        else:
                            self.__objects[key] = BaseModel(**data)
            except json.decoder.JSONDecodeError as e:
                print("Error decoding JSON:", e)

# Test the FileStorage class
