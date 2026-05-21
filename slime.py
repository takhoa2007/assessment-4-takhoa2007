"""
Filename: slime.py
Description: 
Author: Anh Khoa Truong
AU Username: a1989330
GitHub Classroom Username: takhoa2007

This is my own work as defined by the Adelaide University's Academic Misconduct Policy.
"""
""" This is an abstract class for whole types of slime """

import random
from abc import ABC, abstractmethod
import math
from exceptions import InvalidSizeError,InvalidVolatilityError

class Slime(ABC):
    """Abstract class representing a volatile slime entity """
    # Initial value 
    __id_counter = 0 #Class-level counter used generate unique sequential IDS.
    INITIAL_POWER = 5.0

    def __init__(self, ID, name, size) -> None:
        """ Initialise a new Slime with a unique ID and random volatility"""
        Slime.__id_counter += 1
        self.__id = f"SLM-{Slime._id_counter:03d}" 
        self.__name = name
        self.__size = size
        self.set_name(name)
        self.set_size(size)
        self.__volatility_level = random.randint(0, 10)
        self.__power = self.INITIAL_POWER

    def get_id(self) -> str:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name) -> None:
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
            #Raise TypeError: If value is not a string.
        if not name.strip():
            raise ValueError("Name must not be empty.")
            #Raise ValueError: If value is an empty or whitespace-only string.
        self.__name = name

    def get_size(self) -> float:
        return self.__size

    def set_size(self, size) -> None:
        if not isinstance(size, (int, float)):
            raise TypeError("Must be a numeric value.")
            # Raises TypeError: If value is not a numeric type (int or float).
        if not (5.0 <= size <= 200):
            raise InvalidSizeError(f"Size must be between 5.0 and 200.0 cm, got {size}.")
            #Raise InvalidSizeError: If value is outside the range 5.0–200.0.
        self.__size = float(size)
    
    def get_volatility_level(self):
        return self.__volatility_level
    
    def set_volatility_level(self,volatility_level):
        if not isinstance(volatility_level, int):
            raise TypeError("Volatility level must be an integer.")
            #Raise TypeError: If value is not an integer.
        if not (0 <= volatility_level <= 10):
            raise InvalidVolatilityError(f"Volatility must be between 0 and 10, got {volatility_level}.")
            #Raise InvalidVolatilityError: If value is outside the range 0–10.
        self.__volatility_level = volatility_level
