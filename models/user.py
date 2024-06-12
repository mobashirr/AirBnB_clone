
'''
Class user mod
'''

from models.base_model import BaseModel


class User(BaseModel):
    '''
    Class user
    '''

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        '''
        Initialize the User instance with base attributes and additional user-specific attributes.
        '''
        # First, call the base class's __init__ method
        super().__init__(*args, **kwargs)
