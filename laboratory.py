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

    def get_experiments(self) -> dict:
        # Returns a copy to prevent external mutation of the internal dict.
        return dict(self.__experiments)
    experiments = property(get_experiments)

    def add_slime(self, slime) -> None:
        """Add an existing Slime to the laboratory."""
        # Raise TypeError: If slime is not a Slime instance.
        if not isinstance(slime, Slime):
            raise TypeError("Only Slime instances can be added.")
        # Raise ValueError: If a slime with the same ID already exists.
        if slime.get_id() in self.__experiments:
            raise ValueError(
                f"A slime with ID {slime.get_id()!r} already exists in this lab."
            )
        self.__experiments[slime.get_id()] = slime

