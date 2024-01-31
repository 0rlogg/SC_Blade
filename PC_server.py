import socket
import pyautogui
import time

# Configura la dirección IP y el puerto
HOST = '0.0.0.0'  # Escucha en todas las interfaces
PORT = 55555  # El mismo puerto que especificaste en el script del PC principal

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Esperando conexiones en {HOST}:{PORT}")

    while True:
        try:
            conn, addr = s.accept()
            print('Conexión desde', addr)

            while True:
                command = conn.recv(1024).decode('utf-8')
                if not command:
                    break
                print(f"Comando recibido: {command}")

                # Ejecuta el comando recibido (simular la pulsación de tecla 'I')
                if command == 'encendido':
                    pyautogui.press('e')
                # Ejecuta el comando recibido (simular la pulsación de tecla 'I')
                if command == 'target':
                    pyautogui.press('t')
                if command == 'MM':
                    pyautogui.press('m')
                    time.sleep(0.4)  # Añade un retraso de 0.2 segundos entre pulsaciones de teclas
                    pyautogui.click(button='right')
                    time.sleep(0.4)  # Añade un retraso de 0.2 segundos entre pulsaciones de teclas
                    pyautogui.click(button='left')
                if command == 'disparar':
                    pyautogui.click(button='left')

        except Exception as e:
            print(f"Error de conexión: {e}")
