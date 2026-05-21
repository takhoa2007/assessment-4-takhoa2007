"""Custom exceptions for the Slimepocalypse Initiative project."""

class InvalidSizeError(ValueError):
    """Raised when a slime size is outside the valid range (5.0–200.0 cm)."""

    pass

class InvalidVolatilityError(ValueError):
    """Raised when a volatility level is outside the valid range (0–10)."""

    pass
