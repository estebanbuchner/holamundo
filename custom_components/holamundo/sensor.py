from homeassistant.helpers.entity import Entity

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    async_add_entities([HolaMundoSensor()])

class HolaMundoSensor(Entity):
    def __init__(self):
        self._state = "¡Hola Mundo!"

    @property
    def name(self):
        return "Hola Mundo"

    @property
    def state(self):
        return self._state
