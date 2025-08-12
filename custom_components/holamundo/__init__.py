import logging
from .const import DOMAIN, DEFAULT_BASE_URL, DEFAULT_REFRESH, SENSOR_FECHA, SENSOR_HORA , SENSOR_DIA
from .validator import SensorValidator

_LOGGER = logging.getLogger(__name__)

def setup(hass, config):
    conf = config.get(DOMAIN)
    token = conf.get("api_token")
    base_url = conf.get("base_url", DEFAULT_BASE_URL)
    refresh = conf.get("refresh", DEFAULT_REFRESH)
    switch_file =  conf.get("switch_file", "/config/holamundo_switch_state.txt")
    
    sensors = [SENSOR_FECHA,SENSOR_HORA,SENSOR_DIA]

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
        "switch_file": switch_file,
    }

    return True


