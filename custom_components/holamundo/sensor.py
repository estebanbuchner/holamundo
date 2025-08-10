from datetime import datetime, timedelta
import logging
import voluptuous as vol
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import CONF_NAME
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import HomeAssistantType, ConfigType
from homeassistant.helpers.event import async_track_time_interval

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass: HomeAssistantType, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info=None):
    data = hass.data[DOMAIN]
    refresh = data.get("refresh", 10)
#    sensors = data.get("sensors", [])
#
#    entities = [HolaMundoSensor(sensor, refresh) for sensor in sensors]
    entities = [HolaMundoSensorFecha( refresh), HolaMundoSensorHora( refresh) ]
    async_add_entities(entities, update_before_add=True)

class HolaMundoSensorFecha(SensorEntity):
    def __init__(self, refresh):
        self._name = "Fecha"
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
        
        fecha = now.strftime("%Y-%m-%d")
        dia = now.strftime("%A")
        self._state = f"{fecha} ({dia})"

    async def async_added_to_hass(self):
        async_track_time_interval(
            self.hass, lambda now: self.async_schedule_update_ha_state(True),
            timedelta(self._refresh)
        )

class HolaMundoSensorHora(SensorEntity):
    def __init__(self, refresh):
        self._name = "Hora"
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
        hora = now.strftime("%H:%M:%S") 
        self._state = f"{hora}"
    
    async def async_added_to_hass(self):
        async_track_time_interval(
            self.hass, lambda now: self.async_schedule_update_ha_state(True),
            timedelta(self._refresh)
        )