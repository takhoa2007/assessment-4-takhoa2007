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
