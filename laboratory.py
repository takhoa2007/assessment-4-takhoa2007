"""Laboratory: the central hub for managing slime experiments."""

import random
from slime import Slime

class Laboratory:
    """Manages a collection of slime experiments inside the dungeon lab."""

    def __init__(self, name):
        """Initialise an empty Laboratory with the given name."""
        self.set_name(name)
        self.__experiments = {}

    def get_name(self) -> str:
        return self.__name
    def set_name(self, value) -> None:
        # Raise TypeError: If value is not a string.
        if not isinstance(value, str):
            raise TypeError("Laboratory name must be a string.")
        # Raise ValueError: If value is empty or whitespace only.
        if not value.strip():
            raise ValueError("Laboratory name must not be empty.")
        self.__name = value
    name = property(get_name, set_name)
