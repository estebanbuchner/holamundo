"""The 'Hola Mundo' custom integration."""
import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from homeassistant.helpers.discovery import async_load_platform

_LOGGER = logging.getLogger(__name__)

DOMAIN = "holamundo"

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Hola Mundo integration."""
    _LOGGER.info("Starting up 'Hola Mundo'...")
    await async_load_platform(hass, 'sensor', DOMAIN, {}, config)
    return True