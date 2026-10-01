"""Format short weather reports for the dashboard."""

from units import to_celsius, to_kmh


def report(temp_f, wind_mph):
    """A one-line report in metric units, rounded to one decimal place."""
    return f"{round(to_celsius(temp_f), 1)}°C, wind {round(to_kmh(wind_mph), 1)} km/h"
