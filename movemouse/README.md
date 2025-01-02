# Proyecto: Mover Mouse Automáticamente Durante una Hora

Este proyecto contiene un script en Python que mueve ligeramente el mouse de forma automática durante una hora. Es útil para evitar que el sistema entre en modo de reposo o para mantener la actividad en aplicaciones que requieren interacción constante.

## Requisitos

- Python 3.x
- Biblioteca `pyautogui`

Puedes instalar `pyautogui` utilizando pip:

```bash
pip install pyautogui
```

## Uso

1. Clona este repositorio o descarga el archivo `script.py`.
2. Ejecuta el script en una terminal o entorno de desarrollo con el siguiente comando:

```bash
python mover_mouse.py
```

3. El script iniciará el movimiento del mouse durante una hora. Si deseas detenerlo manualmente, presiona `Ctrl + C`.

## Cómo funciona

- El script mueve el mouse ligeramente (1 píxel a la derecha y vuelve al lugar original) cada 30 segundos durante una hora.
- Utiliza las funciones de `pyautogui` para obtener y establecer la posición del mouse.
- El tiempo total de ejecución es de una hora, pero puedes ajustarlo modificando la variable `tiempo_total` en el código.

## Personalización

- **Intervalo de movimiento:** Cambia el valor de `intervalo` (en segundos) para ajustar la frecuencia de los movimientos.
- **Duración total:** Cambia el valor de `tiempo_total` (en segundos) para ajustar la duración total del script.

## Advertencia

Este script debe usarse de manera responsable. No es recomendable usarlo para manipular sistemas de manera indebida o violar términos de uso de aplicaciones.

## Contribuciones

Si deseas mejorar el proyecto o agregar nuevas funcionalidades, no dudes en hacer un fork y enviar un pull request.

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Puedes consultar el archivo `LICENSE` para más detalles.

---

¡Gracias por usar este script! Si tienes preguntas o sugerencias, no dudes en abrir un issue.