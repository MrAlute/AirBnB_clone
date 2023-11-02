#!/usr/bin/python3
"""
The module for Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """The custom amenity class

    Attributes:
        name(str): amenity name

    """
    name = ""
