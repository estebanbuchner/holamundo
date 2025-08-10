"""Config flow for the 'Hola Mundo' integration."""
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult
import voluptuous as vol

DOMAIN = "holamundo"

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for 'Hola Mundo'."""

    VERSION = 1

    async def async_step_user(self, user_input=None) -> FlowResult:
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="Hola Mundo", data={})

        return self.async_show_form(step_id="user", data_schema=vol.Schema({}))
    