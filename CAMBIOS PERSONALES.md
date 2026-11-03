# Cambios personales de PX100

Esta copia deriva de [misdoro/Electronic_load_px100](https://github.com/misdoro/Electronic_load_px100), distribuido bajo GPL-3.0. Se conserva el historial del proyecto y su licencia. Base instalada: revisión a8df111 (3 de agosto de 2026); comprobar REVISION.txt y Git para el identificador completo.

## Cambios de esta copia

- La detección termina al encontrar la primera carga compatible; se muestran errores de lectura y se descartan lecturas incompletas.
- Acceso de Windows con consola de diagnóstico; se oculta tras las primeras lecturas válidas del dispositivo y se puede mostrar desde el icono de la barra de la gráfica.
- Etiqueta de hasta 20 caracteres, con validación para nombres de Windows.
- Pasos independientes y persistentes de 0,01, 0,10 y 1,00 para corriente y voltaje.
- Eje de voltaje a la izquierda y corriente a la derecha; la gráfica conserva zoom y desplazamiento durante las lecturas. La casita vuelve a la vista automática.
- Botón Guardar prueba: exporta CSV y gráfica PNG (y resistencia interna si existe), con fecha/hora y nombres únicos, en logs/<etiqueta>. No reinicia datos ni envía correo.
- Autoguardado original: se actualiza el archivo <etiqueta>_raw_autosave.csv en logs; puede ser sobrescrito por una prueba posterior con la misma etiqueta. Guardar prueba crea una copia independiente.
- Consola registra lecturas; se recupera el ajuste de temporizador del dispositivo.

## Uso y observaciones

Abrir PX100.cmd usa el entorno .venv local. No subir .venv, backups, archivos personales ni datos de pruebas al repositorio. Revisar antes de publicar para evitar compartir credenciales, ajustes o datos privados. Software CC-CV puede modificar la corriente y debe desactivarse para control manual. El uso del temporizador con la DL24 real sigue pendiente de comprobar. Cambios probados parcialmente con lecturas simuladas; verificar cada función con el equipo antes de depender de ella.

El fork de Jay2k1 es otro proyecto preparado aparte para comparación, no se han incorporado sus funciones automáticamente.
