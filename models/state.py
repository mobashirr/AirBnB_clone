#!/usr/bin/env python3


from models.base_model import BaseModel

class State(BaseModel):
    """
    State class that inherits from BaseModel
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)