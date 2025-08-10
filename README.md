# Hola Mundo Sensor para Home Assistant

Este componente personalizado para Home Assistant crea sensores que muestran un saludo, la fecha, la hora y el día de la semana. Además, permite validar sensores configurados y parametrizar el token, el endpoint y el intervalo de actualización.

---

## 🚀 Instalación

1. Cloná o descargá este repositorio en tu carpeta `custom_components`:
    /config/custom_components/holamundo/

2. Reiniciá Home Assistant.

3. Agregá la configuración en `configuration.yaml`.

---

## ⚙️ Configuración.yaml
holamundo:
api_token: !secret holamundo_token
base_url: http://hatest.local:8123/
refresh: 15
sensors:
 - saludo
 - reloj


Parámetros
Parámetro	Tipo	Descripción	Default
api_token	string	Token de autenticación para validar sensores	obligatorio
base_url	string	URL base del endpoint de validación	http://hatest.local:8123/
refresh	integer	Intervalo de actualización en segundos	10
sensors	lista	Lista de nombres de sensores a crear	[]


🧪 Validación de sensores
El componente valida:

Formato del token

Acceso al endpoint /validate

Nombres de sensores definidos

Los errores se loguean en el registro de Home Assistant.

🔄 Scripts útiles
validate_sensors.py
Valida que los sensores estén activos y configurados correctamente.

revert_hora_dia.sh
Desactiva el sensor de hora y día comentando la línea en configuration.yaml.