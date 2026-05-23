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

    def get_electrical_charge(self) -> float:
        return self.__electrical_charge

    def set_electrical_charge(self, value: float) -> None:
        # Raise TypeError: If value is not a numeric type.
        if not isinstance(value, (int, float)):
            raise TypeError("Electrical charge must be a numeric value.")
        # Raise ValueError: If value is negative.
        if value < 0:
            raise ValueError("Electrical charge must be non-negative.")
        self.__electrical_charge = float(value)
    electrical_charge = property(get_electrical_charge, set_electrical_charge)

    def get_is_active(self) -> bool:
        return self.__is_active

    def set_is_active(self, value: bool) -> None:
        # Raise TypeError: If value is not a boolean.
        if not isinstance(value, bool):
            raise TypeError("is_active must be a boolean.")
        self.__is_active = value
    is_active = property(get_is_active, set_is_active)

    def calculate_energy_output(self) -> float:
        """Calculate total energy output from storm intensity and electrical charge.

        Returns 0.0 if the storm is not currently active.
        """
        if not self.__is_active:
            return 0.0
        return round(self.__storm_intensity * self.__electrical_charge, 2)

    def dissipate(self) -> str:
        # Deactivate this weather condition as the storm passes.
        self.__is_active = False
        return "The storm dissipates. Electrical charge fades to zero."

    def __str__(self) -> str:
        active_str = "active" if self.__is_active else "dissipated"
        return (
            f"[WeatherCondition] Intensity: {self.__storm_intensity}/10 | "
            f"Charge: {self.__electrical_charge:.1f} kV | "
            f"Status: {active_str}"
        )