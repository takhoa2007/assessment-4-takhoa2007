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

    def create_slime(self, slime) -> Slime:
        """Register a new Slime in the laboratory and return it."""
        self.add_slime(slime)
        return slime

    def remove_slime(self, slime_id) -> Slime:
        """Remove and return the slime with the given ID."""
        # Raise TypeError: If slime_id is not a string.
        if not isinstance(slime_id, str):
            raise TypeError("Slime ID must be a string.")
        # Raise KeyError: If no slime with that ID exists.
        if slime_id not in self.__experiments:
            raise KeyError(
                f"No slime with ID {slime_id!r} found in the laboratory.")
        return self.__experiments.pop(slime_id)

    def get_slime(self, slime_id) -> Slime:
        """Retrieve a slime by its ID without removing it."""
        # Raise TypeError: If slime_id is not a string.
        if not isinstance(slime_id, str):
            raise TypeError("Slime ID must be a string.")
        # Raise KeyError: If no slime with that ID exists.
        if slime_id not in self.__experiments:
            raise KeyError(
                f"No slime with ID {slime_id!r} found in the laboratory.")
        return self.__experiments[slime_id]

    def interact(self, slime_id_1, slime_id_2) -> str:
        """Combined volatility determines explosion probability. If no explosion
        occurs, the slimes replicate instead."""
        if len(self.__experiments) < 2:
            raise ValueError("At least 2 slimes are required for an interaction.")
        slime_1 = self.get_slime(slime_id_1)
        slime_2 = self.get_slime(slime_id_2)

        combined_volatility = (
            slime_1.get_volatility_level() + slime_2.get_volatility_level()
        ) / 20.0

        if random.random() < combined_volatility:
            return self._explode(slime_1, slime_2) 
        return self._replicate(slime_1, slime_2)

    def _explode(self, slime_1, slime_2) -> str:
        # Destroy both slimes and remove them from the laboratory.
        self.__experiments.pop(slime_1.get_id())
        self.__experiments.pop(slime_2.get_id())
        return (
            f"EXPLOSION! {slime_1.get_name()} ({slime_1.get_id()}) and "
            f"{slime_2.get_name()} ({slime_2.get_id()}) have been destroyed!"
        )
