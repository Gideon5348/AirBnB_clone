#!/usr/bin/python3
"""
BaseModel: Defines the BaseModel class that serves as the foundation for other classes
"""

import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel class with common attributes and methods for other classes
    """

    def __init__(self):
        """
        Initialize a new BaseModel instance with unique ID and timestamps
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance
        """
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data