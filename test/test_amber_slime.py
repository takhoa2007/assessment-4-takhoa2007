"""
Filename: test_amber_slime.py
Description: Unit tests for AmberSlime-specific behaviour and validation.
Author: Anh Khoa Truong
AU Username: a1989330
GitHub Classroom Username: takhoa2007

This is my own work as defined by the Adelaide University's Academic Misconduct Policy.
"""

import math
import pytest
from amber_slime import AmberSlime


def test_amber_slime_initialises_unique_attributes(fixed_volatility):
    """Verify AmberSlime stores age_preserved and is_crystallised on creation.

    These two attributes distinguish AmberSlime from the Slime base class
    and must be reflected accurately in describe_ability.
    """
    fixed_volatility(4)
    amber = AmberSlime("Astra", 20.0, 30, True)

    # Confirm unique attributes are stored and accessible via their getters.
    assert amber.get_age_preserved() == 30
    assert amber.get_is_crystallised() is True
    # describe_ability must reflect both the age and the current shell state.
    assert "30-year-old" in amber.describe_ability()
    assert "crystallised" in amber.describe_ability()


def test_amber_slime_power_includes_age_and_crystallised_state(
        fixed_volatility):
    """Verify that AmberSlime's unique attributes feed into the power formula.

    Rule order: INITIAL_POWER (8.0) + numeric sum (size, volatility,
    age_preserved) + string average * pi, then doubled because
    is_crystallised is True (boolean True multiplies by 2.0).
    """
    fixed_volatility(4)
    amber = AmberSlime("Astra", 20.0, 30, True)

    # Numeric sum: 8.0 (initial) + 20.0 (size) + 4 (volatility) + 30 (age).
    # String contribution: len("Astra") * pi, averaged over one string.
    # Boolean True doubles the running total as the final step.
    expected = round(
        (8.0 + 20.0 + 4 + 30 + len("Astra") * math.pi) * 2.0, 2
    )

    assert amber.get_power() == expected


def test_age_preserved_validation(fixed_volatility):
    """Non-integer and negative age_preserved values raise the correct errors.

    The setter must enforce type before range so that callers receive
    a meaningful exception rather than a silent data corruption.
    """
    fixed_volatility(4)

    # A string argument must raise TypeError before any arithmetic occurs.
    with pytest.raises(TypeError):
        AmberSlime("Astra", 20.0, "old", True)
    # A negative integer violates the non-negative constraint.
    with pytest.raises(ValueError):
        AmberSlime("Astra", 20.0, -1, True)
