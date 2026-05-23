"""
Filename: slime.py
Description: 
Author: Anh Khoa Truong
AU Username: a1989330
GitHub Classroom Username: takhoa2007

This is my own work as defined by the Adelaide University's Academic Misconduct Policy.
"""
""" This is an abstract class for whole types of slime """

from exceptions import InvalidSizeError, InvalidVolatilityError
from abc import ABC, abstractmethod
import math
import random


class Slime(ABC):
    """Abstract class representing a volatile slime entity """
    # Initial value
    # Class-level counter used generate unique sequential IDS.
    __id_counter = 0
    INITIAL_POWER = 5.0

    def __init__(self, name, size):
        """ Initialise a new Slime with a unique ID and random volatility"""
        Slime.__id_counter += 1
        self.__id = f"SLM-{Slime.__id_counter:03d}"
        self.__name = name
        self.__size = size
        self.__volatility_level = random.randint(0, 10)
        self.__power = self.INITIAL_POWER

    def get_id(self) -> str:
        return self.__id
    id = property(get_id)

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name) -> None:
        # Raise TypeError: If value is not a string.
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        # Raise ValueError: If value is an empty or whitespace-only string.
        if not name.strip():
            raise ValueError("Name must not be empty.")
        self.__name = name
    name = property(get_name, set_name)

    def get_size(self) -> float:
        return self.__size

    def set_size(self, size) -> None:
        # Raises TypeError: If value is not a numeric type (int or float).
        if not isinstance(size, (int, float)):
            raise TypeError("Must be a numeric value.")
        # Raise InvalidSizeError: If value is outside the range 5.0–200.0.
        if not (5.0 <= size <= 200):
            raise InvalidSizeError(
                f"Size must be between 5.0 and 200.0 cm, got {size}.")
        self.__size = float(size)
    size = property(get_size, set_size)

    def get_volatility_level(self) -> int:
        return self.__volatility_level

    def set_volatility_level(self, volatility_level) -> None:
        # Raise TypeError: If value is not an integer.
        if not isinstance(volatility_level, int):
            raise TypeError("Volatility level must be an integer.")
        # Raise InvalidVolatilityError: If value is outside the range 0–10.
        if not (0 <= volatility_level <= 10):
            raise InvalidVolatilityError(
                f"Volatility must be between 0 and 10, got {volatility_level}.")
        self.__volatility_level = volatility_level
    volatility_level = property(get_volatility_level, set_volatility_level)

    def get_power(self):
        return self.__power
    power = property(get_power)

    def _get_power_attributes(self):
        return {
            "size": self.__size,
            "volatility_level": self.__volatility_level,
            "name": self.__name,
        }

    def calculate_power(self):
        """Calculate and store power using the formula."""
        attributes = self._get_power_attributes()
        power = self.INITIAL_POWER
        strings = []
        bools = []

        for i in attributes.values():
            # Booleans are subclasses of int so check them first.
            if isinstance(i, bool):
                bools.append(i)
            elif isinstance(i, (int, float)):
                power += i
            elif isinstance(i, str):
                # Use string length as a numeric proxy.
                strings.append(float(len(i)))
            elif i is not None:
                # Other types add a fixed 1.0.
                power += 1.0

        if strings:
            # Average string lengths then multiply by pi.
            avg = sum(strings) / len(strings)
            power += avg * math.pi

        for flag in bools:
            # Apply boolean multipliers.
            if flag:
                power = power * 2.0
            else:
                power = power / 2.0
        # Rule 6: round and store.
        self.__power = round(power, 2)
        return self.__power

    @abstractmethod
    def describe_ability(self):
        pass

    def __str__(self):
        return (f"{type(self).__name__}] {self.__id} {self.__name} "
                f"Size: {self.__size:.1f} cm Volatility: {self.__volatility_level} Power: {self.__power:.2f}")
