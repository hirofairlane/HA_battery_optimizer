echo 'from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType

DOMAIN = "battery_optimizer"

def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    hass.data[DOMAIN] = {}
    return True' > __init__.py
