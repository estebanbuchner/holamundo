import os
from datetime import timedelta
from homeassistant.components.switch import SwitchEntity
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.event import async_track_time_interval
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN

async def async_setup_platform(hass: HomeAssistant, config: dict, async_add_entities: AddEntitiesCallback, discovery_info=None):
    data = hass.data[DOMAIN]
    file_path = data.get("switch_file", "/config/holamundo_switch_state.txt")
    refresh = data.get("refresh", 10)

    async_add_entities([HolaMundoSwitch("Interruptor", file_path, refresh)], update_before_add=True)


class HolaMundoSwitch(SwitchEntity):
    def __init__(self, name: str, file_path: str, refresh: int):
        self._name = name
        self._file_path = file_path
        self._refresh = refresh
        self._is_on = False

    @property
    def name(self):
        return self._name

    @property
    def is_on(self):
        return self._is_on

    async def async_turn_on(self, **kwargs):
        self._is_on = True
        await self._write_state("on")
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs):
        self._is_on = False
        await self._write_state("off")
        self.async_write_ha_state()

    async def async_update(self):
        """Lee el estado desde el archivo."""
        if os.path.exists(self._file_path):
            try:
                with open(self._file_path, "r") as f:
                    content = f.read().strip()
                    self._is_on = content == "on"
            except Exception as e:
                self._is_on = False  # fallback
                _LOGGER.warning(f"No se pudo leer el archivo {self._file_path}: {e}")

    async def async_added_to_hass(self):
        """Registra el refresco periódico."""
        self.async_on_remove(
            async_track_time_interval(
                self.hass,
                self._async_update_callback,
                timedelta(seconds=self._refresh)
            )
        )

    @callback
    def _async_update_callback(self, now):
        self.async_schedule_update_ha_state(True)

    async def _write_state(self, state: str):
        try:
            with open(self._file_path, "w") as f:
                f.write(state)
        except Exception as e:
            _LOGGER.error(f"No se pudo escribir en {self._file_path}: {e}")
