"""StormSlime: a lightning-charged slime that absorbs environmental energy."""

from slime import Slime
from weather_condition import WeatherCondition

class StormSlime(Slime):
    """A slime infused with storm energy that interacts with weather events."""

    INITIAL_POWER = 6.0
    _OVERCHARGE_THRESHOLD = 100.0

    def __init__(self, name, size, charge_level, is_overcharged=False, weather=None):
        """Initialise a StormSlime with electrical charge properties."""
        super().__init__(name, size)
        self.__charge_level = charge_level
        self.__is_overcharged = is_overcharged
        self.__weather = weather

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
        volatility_boost = min(int(energy // 20), 10 - self.__volatility_level)
        self.__volatility_level = min(self.__volatility_level + volatility_boost, 10)

        # Mark overcharged if charge exceeds the safety threshold.
        self.__is_overcharged = self.__charge_level >= self._OVERCHARGE_THRESHOLD

        self.calculate_power()
        return (
            f"{self.get_name()} absorbs {energy:.1f} kV from the storm! \n"
            f"Charge: {self.__charge_level:.1f} kV \n"
            f"Volatility: {self.__volatility_level}\n"
            f"Power: {self.__power:.2f}."
        )