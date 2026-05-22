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
        self.__age_preserved = age_preserved
        self.__is_crystallised = is_crystallised

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

    
    def crack_resin(self) -> str:
        """Crack the amber shell to release stored energy.When cracked, the slime is no longer crystallised, its size grows slightly from the energy release, and power is recalculated."""
        self.__is_crystallised = False

        # Energy release pushes the slime to grow, capped at the max size.
        new_size = min(self.__size + 10.0, 200.0)
        self.__size = new_size

        self.calculate_power()
        return (
            f"{self.__name} cracks its amber shell! "
            f"Ancient energy erupts. New size: {self.__size:.1f} cm, "
            f"Power: {self.__power:.2f}."
        )

    def fossilise(self) -> str:
        """Harden the amber shell back to a crystallised state.

        Crystallisation reduces size slightly as the slime compresses,
        then power is recalculated.

        Returns:
            A description of the fossilisation event.
        """
        self.__is_crystallised = True

        new_size = max(self._Slime__size - 5.0, 5.0)
        self._Slime__size = new_size

        self.calculate_power()
        return (
            f"{self._Slime__name} hardens back into crystallised amber. "
            f"Size: {self._Slime__size:.1f} cm, Power: {self._Slime__power:.2f}."
        )
