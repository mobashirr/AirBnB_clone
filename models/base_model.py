#!/usr/bin/python3

'''
the BASE CLASS
'''


import uuid, datetime
import models


class BaseModel:


    def __init__(self, *args, **kwargs):
        """
        Initiating an instance...

        id: a unique identifier of the instance

        created_at: date of the instance in which it has
        been created.

        updated_at: date of the instance in which it has
        been updated.
        """
        if kwargs:
            ''' Initiating using dic'''
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        self.__dict__[key] = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)    # save the new instance to FileStorage class
    

    def __str__(self):
        return f"[{self.__class__.__name__ }] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.save()   # use the storage variable to save to the file

    def to_dict(self):
        """
        Returns a dictionary of all keys and values
        of __dict__
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
