"""StormSlime: a lightning-charged slime that absorbs environmental energy."""

from slime import Slime

class StormSlime(Slime):
    """A slime infused with storm energy that interacts with weather events."""

    INITIAL_POWER = 6.0
    _OVERCHARGE_THRESHOLD = 100.0

    def __init__(self, name, size, charge_level, is_overcharged=False,weather=None):
        """Initialise a StormSlime with electrical charge properties."""
        super().__init__(name, size)
        self.__charge_level = charge_level
        self.__is_overcharged = is_overcharged
        self.__weather = weather
        

    def get_charge_level(self) -> float:
        return self.__charge_level

    def set_charge_level(self, value) -> None:
        # Raise TypeError: If value is not a numeric type.
        if not isinstance(value, (int, float)):
            raise TypeError("Charge level must be a numeric value.")
        # Raise ValueError: If value is negative.
        if value < 0:
            raise ValueError("Charge level must be non-negative.")
        self.__charge_level = float(value)