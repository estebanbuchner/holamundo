"""Platform for the 'Hola Mundo' sensor."""
from homeassistant.components.sensor import SensorEntity

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the sensor platform."""
    async_add_entities([HelloWorldSensor()])

class HelloWorldSensor(SensorEntity):
    """Representation of a 'Hello World' sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = "¡Hola, mundo!"

    @property
    def name(self):
        """Return the name of the sensor."""
        return "Hola Mundo Sensor"

    @property
    def unique_id(self):
        """Return a unique ID for this sensor."""
        return "hola_mundo_sensor"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state