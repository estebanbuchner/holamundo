# Changelog

## [v1.2.0] - 2025-08-10

### Agregado
- `sensor.hora_actual`: muestra la hora actual en formato `YYYY-MM-DD HH:MM:SS`
- `sensor.hora_y_dia`: muestra atributos `hora`, `día` y `intervalo_actualización`
- Traducción de días al español
- Actualización automática cada 10 segundos usando `async_track_time_interval`

### Mejorado
- Corrección de formato en `strftime`
- Modularización de sensores múltiples en `sensor.py`

### Configurable
- Activación condicional de `HoraDiaSensor` desde `configuration.yaml` con `mostrar_hora_dia: true`
