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

## [v1.3.8] - 2025-08-12

### Changed
- Reemplazo de `HomeAssistantType` por `HomeAssistant` para compatibilidad con HA Core 2025.5
- Eliminado `ConfigType` obsoleto, reemplazado por `dict` en `async_setup_platform`

## [v1.4] - 2025-08-12
### Added
- Switch que persiste su estado en archivo local y lo lee en `async_update`
