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
