"""WeatherCondition: a natural atmospheric phenomenon that fuels StormSlime."""


class WeatherCondition:
    """Represents an atmospheric weather event that StormSlime draws power from."""

    def __init__(self, storm_intensity, electrical_charge,is_active = True) -> None:
        """Initialise a WeatherCondition with storm and electrical properties."""
        self.__storm_intensity = storm_intensity
        self.__electrical_charge = electrical_charge
        self.__is_active = is_active

    def get_storm_intensity(self) -> int:
        return self.__storm_intensity

    def set_storm_intensity(self, value: int) -> None:
        # Raise TypeError: If value is not an integer.
        if not isinstance(value, int):
            raise TypeError("Storm intensity must be an integer.")
        # Raise ValueError: If value is outside the range 1–10.
        if not (1 <= value <= 10):
            raise ValueError(f"Storm intensity must be between 1 and 10, got {value}.")
        self.__storm_intensity = value
    storm_intensity = property(get_storm_intensity, set_storm_intensity)
