import socket
import time
import pyautogui


# Configure the IP address and port
HOSTNAME = socket.gethostname()
HOST =  socket.gethostbyname(HOSTNAME)
PORT = 61000

print (HOSTNAME)
print (HOST)
print (PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_info:
    socket_info.bind((HOST, PORT))
    socket_info.listen()
    print(f"Waiting conexions in {HOST}:{PORT}")

    while True:
        try:
            conn, addr = socket_info.accept()
            print('Conexion from', addr)

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
