#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage


class BaseModel:

    def __init__(self, *args, **kwargs):
        if kwargs:  # If kwargs is not empty
            # Iterate over each key-value pair in kwargs
            for key, value in kwargs.items():
                # Check if the key is not '__class__'
                if key != '__class__':
                    # If the key is 'created_at' or 'updated_at', convert the value to a datetime object
                    if key in ['created_at', 'updated_at']:
                        # Check if the value is already a datetime object
                        if isinstance(value, datetime):
                            setattr(self, key, value)
                        else:
                            setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:  # If kwargs is empty
            # Create id and created_at attributes
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__ }] (<{self.id}>) <{self.__dict__}>"

    def save(self):
        storage.save()  # Save the current state of the storage
        self.update_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")

    def to_dict(self):
        dict = self.__dict__
        dict['__class__'] = self.__class__.__name__        
        return dict


# Test the BaseModel class
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)