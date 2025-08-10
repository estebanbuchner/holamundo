import logging
from .const import DOMAIN, DEFAULT_BASE_URL, DEFAULT_REFRESH
from .validator import SensorValidator

_LOGGER = logging.getLogger(__name__)

def setup(hass, config):
    conf = config.get(DOMAIN)
    token = conf.get("api_token")
    base_url = conf.get("base_url", DEFAULT_BASE_URL)
    refresh = conf.get("refresh", DEFAULT_REFRESH)
    sensors = ["Fecha","Hora"]

    if not token:
        _LOGGER.error("api_token no definido en configuration.yaml")
        return False

    validator = SensorValidator(base_url, token)
    if not validator.validate_sensors(sensors):
        _LOGGER.error("Validación de sensores fallida.")
        return False

    hass.data[DOMAIN] = {
        "api_token": token,
        "base_url": base_url,
        "refresh": refresh,
        "sensors": sensors,
    }

    return True


