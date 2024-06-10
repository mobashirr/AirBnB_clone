#!/usr/bin/python3

'''
the BASE CLASS
'''


import uuid, datetime
# from models import storage
# from . import storage


class BaseModel:
    """
        Initiating an instance...

        id: a uniqe identifier of the instance

        created_at: date of the instance in which it has
        been created.

        updated_at: date of the instance in which it has
        been updated.
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__ }] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()

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
