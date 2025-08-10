from homeassistant.helpers.entity import Entity

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    async_add_entities([
        HolaMundoSensor(),
        HoraActualSensor()
    ], True)


class HolaMundoSensor(Entity):
    def __init__(self):
        self._state = "¡Hola Mundo!"

    @property
    def name(self):
        return "Hola Mundo"

    @property
    def state(self):
        return self._state

from datetime import datetime

class HoraActualSensor(Entity):
    def __init__(self):
        self._state = None

    @property
    def name(self):
        return "Hora Actual"

    @property
    def state(self):
        return self._state

    async def async_update(self):
        self._state = datetime.now().strftime("%H:%M:%S")
