from datetime import datetime, timedelta
import logging
import voluptuous as vol
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import CONF_NAME
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import HomeAssistantType, ConfigType
from homeassistant.helpers.event import async_track_time_interval
from homeassistant.core import callback

from .const import DOMAIN, SENSOR_FECHA, SENSOR_HORA , SENSOR_DIA

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass: HomeAssistantType, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info=None):
    data = hass.data[DOMAIN]
    refresh = data.get("refresh", 10)
    entities = [HolaMundoSensorFecha( refresh), HolaMundoSensorHora( refresh), HolaMundoSensorDia( refresh)  ]
    async_add_entities(entities, update_before_add=True)



class HolaMundoBaseSensor(SensorEntity):
    def __init__(self, name, refresh):
        self._name = name
        self._state = None
        self._refresh = refresh

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    async def async_added_to_hass(self):
        """Register update callback."""
        self.async_on_remove(
            async_track_time_interval(
                self.hass,
                self._async_update_callback,
                timedelta(seconds=self._refresh),
            )
        )

    @callback
    def _async_update_callback(self, now):
        """Callback triggered by time interval."""
        self.async_schedule_update_ha_state(True)



class HolaMundoSensorHora(HolaMundoBaseSensor):
    def __init__(self, refresh):
        super().__init__(SENSOR_HORA, refresh)

    async def async_update(self):
        now = datetime.now()
        self._state = now.strftime("%H:%M:%S")


class HolaMundoSensorFecha(HolaMundoBaseSensor):
    def __init__(self, refresh):
        super().__init__(SENSOR_FECHA, refresh)

    async def async_update(self):
        now = datetime.now()
        fecha = now.strftime("%Y-%m-%d")
        dia = now.strftime("%A")
        self._state = f"{fecha}"


class HolaMundoSensorDia(HolaMundoBaseSensor):
    def __init__(self, refresh):
        super().__init__(SENSOR_DIA, refresh)

    async def async_update(self):
        now = datetime.now()
       
        dia = now.strftime("%A")
        self._state = f"({dia})"
