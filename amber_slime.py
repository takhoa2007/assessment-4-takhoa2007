"""AmberSlime: a resin-encased slime entity that preserves ancient power."""
from slime import Slime


class Amber(Slime):
    """A slime encased in hardened amber resin with preserved fossil energy.

     AmberSlime stores ancient energy inside its amber shell. The older
    the preserved specimen (age_preserved), the more power it has. When
    its resin cracks, it releases ancient energy."""
    INITIAL_POWER = 8.0

    def __init__(self, name, size, age_preserved, is_crystallised):
        super().__init__(name, size)
        # Using setter to validate the input values
        self.set_age_preserved(age_preserved)
        self.set_is_crystallised(is_crystallised)

    def get_age_preserved(self) -> int:
        # Return how many year this slime has been preserved.
        return self.__age_preserved

    def set_age_preserved(self, age_preserved) -> None:
        if not isinstance(age_preserved, int):
            # Raise TypeError: If value is not an integer.
            raise TypeError("Age preserved must be an integer")
        if age_preserved < 0:
            # Raise ValueError: If value is negative.
            raise ValueError("Age preserved must be a non-negative integer")
        self.__age_preserved = age_preserved
    age_preserved = property(get_age_preserved, set_age_preserved)

    def get_is_crystallised(self) -> bool:
        # Return whether the amber shell is fully crystallised.
        return self.__is_crystallised

    def set_is_crystallised(self, is_crystallised) -> None:
        if not isinstance(is_crystallised, bool):
            # Raise TypeError: If value is not a boolean.
            raise TypeError("is_crystallised must be a boolean.")
        self.__is_crystallised = is_crystallised

    is_crystallised = property(get_is_crystallised, set_is_crystallised)

    def crack_resin(self) -> str:
        """Crack the amber shell to release stored energy.When cracked, the slime is no longer crystallised, its size grows slightly from the energy release, and power is recalculated."""
        self.__is_crystallised = False

        # Energy release pushes the slime to grow, capped at the max size.
        new_size = min(self.get_size() + 10.0, 200.0)
        self._size = new_size

        self.calculate_power()
        return (
            f"{self.get_name()} cracks its amber shell! "
            f"Ancient energy erupts. New size: {self.get_size():.1f} cm, "
            f"Power: {self.get_power():.2f}."
        )

    def fossilise(self) -> str:
        # Harden the amber shell back to a crystallised state. Crystallisation reduces size slightly as the slime compresses, then power is recalculated.
        self.__is_crystallised = True

        new_size = max(self.get_size() - 5.0, 5.0)
        self._size = new_size

        self.calculate_power()
        return (
            f"{self.get_name()} hardens back into crystallised amber. "
            f"Size: {self.get_size():.1f} cm, "
            f"Power: {self.get_power():.2f}."
        )

    def describe_ability(self) -> str:
        # Returns of the slime's aura based on its current shell state.
        if self.__is_crystallised:
            state = "crystallised"
        else:
            state = "soft"
        return (
            f"{self.get_name()} radiates {self.get_age_preserved()}-year-old preserved "
            f"energy through its {state} amber casing."
        )

    def _get_power_attributes(self) -> dict:
        # Adds age_preserved and is_crystallised to the power formula.
        base = super()._get_power_attributes()
        base["age_preserved"] = self.__age_preserved
        base["is_crystallised"] = self.__is_crystallised
        return base

    def __str__(self) -> str:
        # Return a detailed string summary for AmberSlime.
        if self.__is_crystallised:
            state = "crystallised"
        else:
            state = "soft"
        return (
            f"{super().__str__()}\n"
            f"Age Preserved: {self.__age_preserved} yrs\n"
            f"Shell: {state}"
        )
