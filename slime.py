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
    __id_counter = 0
    INITIAL_POWER = 5.0
    def __init__(self,ID,name,size):
        Slime.__id_counter += 1
        self.__id = f"SLM-{Slime._id_counter}"
        self.__name = name
        self.__size = size
        self.set_name(name)
        self.set_size(size)
        self.__volatility_level = random.randint(0,10)
        self.__power = self.INITIAL_POWER


