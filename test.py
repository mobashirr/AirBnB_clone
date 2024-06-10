#!/usr/bin/python3


class MyClass:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an instance
obj = MyClass("Alice", 30)

from models.base_model import BaseModel

bm = BaseModel()
print(type(bm.id))

# Attempting to access __dict__ will raise an AttributeError
# print(obj.__dict__)  # This will raise an AttributeError




'''
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                # Check if the key is not '__class__'
                if key != '__class__':
                    # If the key is 'created_at' or 'updated_at', convert the value to a datetime object
                    if key in ['created_at', 'updated_at']:
                        # Check if the value is already a datetime object
                        if isinstance(value, datetime):
                            setattr(self, key, value)
                        else:
                            setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            ob = datetime.now()
            self.created_at = self.updated_at = ob.isoformat()
            storage.new(self)   # Add the new object to the storage

    def __str__(self):
        return f"[{self.__class__.__name__ }] ({self.id}) {self.__dict__}"

    def save(self):
        try:
            pass
        except AttributeError:
            for key,value in storage.__objects.items():
                if not isinstance(value,BaseModel):
                    storage.__objects[key] = BaseModel(**value)
        finally:
            storage.save()  # Save the current state of the storage
            ob = datetime.now()
            self.updated_at = ob.isoformat()

    def to_dict(self):
        dict = self.__dict__
        # dict['__class__'] = self.__class__.__name__
        return dict
'''