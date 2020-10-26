"""Constants for Chargeamps."""
# Base component constants
DOMAIN = "chargeamps"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "1.1.0"
PLATFORMS = ["sensor", "switch", "light"]
ISSUE_URL = "https://github.com/kirei/hass-chargeamps/issues"

# Icons
DEFAULT_ICON = "mdi:car-electric"
ICON_MAP = {
    "Charger": "mdi:ev-station",
    "Schuko": "mdi:power-socket-de",
}

# Configuration
CONF_CHARGEPOINTS = "chargepoints"
CONF_READONLY = "readonly"

# Defaults
DEFAULT_NAME = DOMAIN

# Possible dimmer values
DIMMER_VALUES = ["off", "low", "medium", "high"]