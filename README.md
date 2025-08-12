# Hola Mundo Sensor para Home Assistant

Este componente personalizado para Home Assistant crea sensores que muestran un saludo, la fecha, la hora y el día de la semana. Además, permite parametrizar el token, el endpoint y el intervalo de actualización.

---

## 🚀 Instalación

1. Cloná o descargá este repositorio en tu carpeta `custom_components`:
    /config/custom_components/holamundo/

2. Reiniciá Home Assistant.

3. Agregá la configuración en `configuration.yaml`.

---

## ⚙️ Configuración.yaml

```yaml
sensor:
  - platform: holamundo
holamundo:
  api_token: !secret holamundo_token
  base_url: http://hatest.local:8123/
  refresh: 15




| Configuración | Descripción                            |
|---------------|----------------------------------------|
| `refresh`     | Intervalo de actualización en segundos |
| `base_url`    | URL base de Home Assistant             |
| `api_token`   | Token de autenticación                 |




🧪 Validación de sensores
El componente valida:

Formato del token

Acceso al endpoint /validate

Nombres de sensores definidos

Los errores se loguean en el registro de Home Assistant.

