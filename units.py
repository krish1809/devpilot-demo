"""Unit conversions used across the weather tools."""


def to_celsius(fahrenheit):
    """Convert degrees Fahrenheit to degrees Celsius."""
    return (fahrenheit - 32) * 5 / 9


def to_kmh(mph):
    """Convert miles per hour to kilometres per hour."""
    return mph * 1.609344
