"""
Filename: slime.py
Description: 
Author: Anh Khoa Truong
AU Username: a1989330
GitHub Classroom Username: takhoa2007

This is my own work as defined by the Adelaide University's Academic Misconduct Policy.
"""
""" This is an abstract class for whole types of slime """

from abc import ABC, abstractmethod
import math
import random

class Slime(ABC):
    #Initial value (Could not be changed)
    __id_counter = 0
    INITIAL_POWER = 5.0
    def __init__(self,ID,name,size) -> None:
        Slime.__id_counter += 1
        self.__id = f"SLM-{Slime._id_counter}"
        self.__name = name
        self.__size = size
        self.set_name(name)
        self.set_size(size)
        self.__volatility_level = random.randint(0,10)
        self.__power = self.INITIAL_POWER

    def get_id(self) -> str:
        return self.__id
    
    def get_name(self) -> str:
        return self.__name
    
    def set_name(self,name) -> None:
        if not isinstance(name,str):
            raise TypeError("Name must be a string.")
        if not name.strip():
            raise ValueError("Name must not be empty.")
        self.__name = name

    def get_size(self) -> float:
        return self.__size
    
    def set_size(self,size) -> None:
        if not isinstance(size, (int,float)):
            raise TypeError("Must be a numeric value.")
        # Raises TypeError: If value is not a numeric type (int or float).
        self.__size = float(size)