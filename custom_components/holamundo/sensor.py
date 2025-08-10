from datetime import datetime
import logging
import voluptuous as vol
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import CONF_NAME
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import HomeAssistantType, ConfigType
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass: HomeAssistantType, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info=None):
    data = hass.data[DOMAIN]
    refresh = data.get("refresh", 10)
    sensors = data.get("sensors", [])

    entities = [HolaMundoSensor(sensor, refresh) for sensor in sensors]
    async_add_entities(entities, update_before_add=True)

class HolaMundoSensor(SensorEntity):
    def __init__(self, name, refresh):
        self._name = f"Hola Mundo {name}"
        self._state = None
        self._refresh = refresh

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    async def async_update(self):
        now = datetime.now()
        texto = "Hola Mundo"
        fecha = now.strftime("%Y-%m-%d")
        hora = now.strftime("%H:%M:%S")
        dia = now.strftime("%A")
        self._state = f"{texto} - {fecha} {hora} ({dia})"
