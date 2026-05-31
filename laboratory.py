"""
Filename: laboratory.py
Description: Laboratory: the central hub for managing slime experiments.
Author: Anh Khoa Truong
AU Username: a1989330
GitHub Classroom Username: takhoa2007

This is my own work as defined by the Adelaide University's Academic Misconduct Policy.
"""

import random
import copy
from slime import Slime
from amber_slime import AmberSlime
from storm_slime import StormSlime
from weather_condition import WeatherCondition


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

    def create_amber_slime(self, name, size,
                           age_preserved, is_crystallised=False,) -> AmberSlime:
        # Create an AmberSlime, register it, and return it.
        try:
            slime = AmberSlime(name, size, age_preserved, is_crystallised)
            self.__register_slime(slime)
            return slime
        except Exception as error:
            print(f"Construction error: {error}")

    def create_weather_condition(self, storm_intensity,
                                 electrical_charge, is_active=True) -> WeatherCondition:
        """Create and return a WeatherCondition for linking to a StormSlime."""
        try:
            return WeatherCondition(storm_intensity, electrical_charge, is_active)
        except Exception as error:
            print(f"Construction error: {error}")

    def create_storm_slime(self, name, size, charge_level,
                           is_overcharged=False, weather=None,) -> StormSlime:
        """Create a StormSlime, register it, and return it."""
        try:
            slime = StormSlime(name, size, charge_level,
                               is_overcharged, weather)
            self.__register_slime(slime)
            return slime
        except Exception as error:
            print(f"Construction error: {error}")

    def __register_slime(self, slime: Slime) -> None:
        # Add a fully constructed slime to the experiments dictionary.
        if slime.get_id() in self.__experiments:
            # Raises ValueError: If a slime with the same ID already exists.
            raise ValueError(f"Slime ID {slime.get_id()!r} already exists.")
        self.__experiments[slime.get_id()] = slime

    def add_slime(self, slime: Slime) -> Slime:
        """Register a pre-existing Slime instance in the laboratory."""
        if not isinstance(slime, Slime):
            raise TypeError("Only Slime instances can be registered.")
        self.__register_slime(slime)
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
        if slime_id_1 == slime_id_2:
            raise ValueError("A slime cannot interact with itself.")

        if len(self.__experiments) < 2:
            raise ValueError(
                "At least 2 slimes are required for an interaction.")
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

    def _replicate(self, slime_1, slime_2) -> str:
        # Deep copy a randomly chosen parent to create an independent offspring.
        parent = random.choice([slime_1, slime_2])
        offspring = copy.deepcopy(parent)
        offspring._assign_new_id()

        self.__experiments[offspring.get_id()] = offspring
        return (
            f"REPLICATION! {parent.get_name()} ({parent.get_id()}) produced "
            f"offspring {offspring.get_name()} ({offspring.get_id()})."
        )

    def __str__(self) -> str:
        # Return early if no slimes have been registered yet.
        if not self.__experiments:
            return f"=== {self.__name} ===\n  (No slimes registered.)"

        result = f"=== {self.__name} ===\n"
        result += f"  Total slimes: {len(self.__experiments)}\n"
        for slime_id, slime in self.__experiments.items():
            indented = str(slime).replace("\n", "\n    ")
            result += f"    {indented}\n"
        return result.strip()
