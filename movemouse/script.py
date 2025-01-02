import pyautogui
import time

def mover_mouse_durante_una_hora():
    print("Iniciando el movimiento del mouse por una hora...")
    tiempo_total = 60 * 60  # 60 minutos en segundos
    intervalo = 30  # Intervalo en segundos
    tiempo_transcurrido = 0

    try:
        while tiempo_transcurrido < tiempo_total:
            # Obtén la posición actual del mouse
            x, y = pyautogui.position()
            # Mueve el mouse un píxel hacia la derecha y vuelve al lugar original
            pyautogui.moveTo(x + 1, y, duration=0.1)
            pyautogui.moveTo(x, y, duration=0.1)
            print(f"Mouse movido ligeramente. Esperando {intervalo} segundos...")
            # Espera 30 segundos
            time.sleep(intervalo)
            tiempo_transcurrido += intervalo
        print("Se completó una hora de movimiento del mouse.")
    except KeyboardInterrupt:
        print("\nMovimiento del mouse detenido manualmente.")

if __name__ == "__main__":
    mover_mouse_durante_una_hora()
