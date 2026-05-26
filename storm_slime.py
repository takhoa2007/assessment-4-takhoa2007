"""StormSlime: A lightning-charged slime that absorbs environmental energy."""
"""
Filename: storm_slime.py
Description: StormSlime: A lightning-charged slime that absorbs environmental energy.
Author: Anh Khoa Truong
AU Username: a1989330
GitHub Classroom Username: takhoa2007

This is my own work as defined by the Adelaide University's Academic Misconduct Policy.
"""

from slime import Slime
from weather_condition import WeatherCondition


class StormSlime(Slime):
    """A slime infused with storm energy that interacts with weather events."""

    INITIAL_POWER = 6.0
    _OVERCHARGE_THRESHOLD = 100.0

    def __init__(self, name, size, charge_level, is_overcharged=False, weather=None):
        """Initialise a StormSlime with electrical charge properties."""
        super().__init__(name, size)
        self.set_charge_level(charge_level)
        self.set_is_overcharged(is_overcharged)
        self.set_weather(weather)
        self.calculate_power()

    def get_charge_level(self) -> float:
        return self.__charge_level

    def set_charge_level(self, charge_level) -> None:
        # Raise TypeError: If value is not a numeric type.
        if not isinstance(charge_level, (int, float)):
            raise TypeError("Charge level must be a numeric value.")
        # Raise ValueError: If value is negative.
        if charge_level < 0:
            raise ValueError("Charge level must be non-negative.")
        self.__charge_level = float(charge_level)
    charge_level = property(get_charge_level, set_charge_level)

    def get_is_overcharged(self) -> bool:
        return self.__is_overcharged

    def set_is_overcharged(self, is_overcharged) -> None:
        # Raise TypeError: If value is not a boolean.
        if not isinstance(is_overcharged, bool):
            raise TypeError("is_overcharged must be a boolean.")
        self.__is_overcharged = is_overcharged
    is_overcharged = property(get_is_overcharged, set_is_overcharged)

    def get_weather(self):
        return self.__weather

    def set_weather(self, weather) -> None:
        # Raise TypeError: If value is not a WeatherCondition or None.
        if weather is not None and not isinstance(weather, WeatherCondition):
            raise TypeError("weather must be a WeatherCondition or None.")
        self.__weather = weather
    weather = property(get_weather, set_weather)

    def absorb_weather(self, weather) -> str:
        """Absorb energy from a WeatherCondition to boost charge and power."""
        if not isinstance(weather, WeatherCondition):
            raise TypeError("Must provide a WeatherCondition to absorb.")
        if not weather.get_is_active():
            raise ValueError("Cannot absorb from an inactive weather event.")

        self.__weather = weather
        energy = weather.calculate_energy_output()
        self.__charge_level += energy

        # Higher charge pushes volatility up, capped at 10.
        volatility_boost = min(int(energy // 20), 10 -
                               self.get_volatility_level())
        new_volatility = min(
            self.get_volatility_level() + volatility_boost, 10)
        self.set_volatility_level(new_volatility)

        # Mark overcharged if charge exceeds the safety threshold.
        self.__is_overcharged = self.__charge_level >= self._OVERCHARGE_THRESHOLD

        self.calculate_power()
        return (
            f"{self.get_name()} absorbs {energy:.1f} kV from the storm! \n"
            f"Charge: {self.__charge_level:.1f} kV \n"
            f"Volatility: {self.get_volatility_level()}\n"
            f"Power: {self.get_power():.2f}."
        )

    def discharge(self) -> str:
        # Release half the stored charge to stabilise the slime.
        released = round(self.__charge_level / 2.0, 2)
        self.__charge_level = round(self.__charge_level - released, 2)
        new_volatility = max(self.get_volatility_level() - 3, 0)
        self.set_volatility_level(new_volatility)
        self.__is_overcharged = False

        self.calculate_power()
        return (
            f"{self.get_name()} discharges {released:.1f} kV!\n"
            f"Remaining charge: {self.__charge_level:.1f} kV\n"
            f"Volatility: {self.get_volatility_level()} \n"
            f"Power: {self.get_power():.2f}."
        )

    def describe_ability(self) -> str:
        # Describe StormSlime's charge state including overcharge warning.
        if self.__is_overcharged:
            overcharge_str = " OVERCHARGED!"
        else:
            overcharge_str = ""
        return (
            f"{self.get_name()} crackles with {self.__charge_level:.1f} kV of "
            f"stored lightning energy.{overcharge_str}"
        )

    def _get_power_attributes(self) -> dict:
        # Adds charge_level, is_overcharged, and optional weather energy to the formula.
        base = super()._get_power_attributes()
        base["charge_level"] = self.__charge_level
        base["is_overcharged"] = self.__is_overcharged
        if self.__weather is not None:
            base["weather_energy"] = self.__weather.calculate_energy_output()
        return base

    def __str__(self) -> str:
        # Extends the base slime summary with StormSlime-specific fields.
        overcharge_str = "YES" if self.__is_overcharged else "NO"
        if self.__weather:
            weather_str = f"Storm: {self.__weather.get_storm_intensity()}/10"
        else:
            weather_str = "No linked storm"
        return (
            f"{super().__str__()}\n"
            f"Charge: {self.__charge_level:.1f} kV \n"
            f"Overcharged: {overcharge_str} \n"
            f"{weather_str}"
        )
