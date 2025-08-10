import logging
import re
import requests

_LOGGER = logging.getLogger(__name__)

class SensorValidator:
    def __init__(self, base_url, token):
        self.base_url = base_url.rstrip("/")
        self.token = token

    def validate_token(self):
        if not self.token or not isinstance(self.token, str):
            _LOGGER.error("Token ausente o inválido.")
            return False

        if len(self.token) < 20 or not re.match(r"^[A-Za-z0-9\-_\.]+$", self.token):
            _LOGGER.error("Formato de token inválido.")
            return False

        try:
            response = requests.get(
                f"{self.base_url}/config",
                headers={"Authorization": f"Bearer {self.token}"},
                timeout=5
            )
            _LOGGER.debug(f"validate_token {response.status_code } ")
            return response.status_code == 200
        except requests.RequestException as e:
            _LOGGER.error(f"Error al validar token: {e}")
            return False

    def validate_sensors(self, sensors):
    
        _LOGGER.debug("validate_sensors")

        if not self.validate_token():
            return False
        
        _LOGGER.debug("validate_token okl")

        # Simulación de validación de sensores
        for sensor in sensors:
            if not isinstance(sensor, str) or not sensor:
                _LOGGER.warning(f"Sensor inválido: {sensor}")
                return False

        return True
