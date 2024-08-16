import socket
import time
import pyautogui  

# Configura la dirección IP y el puerto
HOSTNAME = socket.gethostname()
HOST = input('Type the IP of the PC-server: ')  # Asegúrate de ingresar la IP correcta aquí
PORT = 61000

print(HOSTNAME)
print(HOST)
print(PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_info:
    socket_info.bind((HOST, PORT))
    socket_info.listen()
    print(f"Waiting for connections at {HOST}:{PORT}")

    while True:
        try:
            conn, addr = socket_info.accept()
            print('Connected by', addr)

            while True:
                command = conn.recv(1024).decode('utf-8')
                if not command:
                    break
                print(f"Command received: {command}")

                # Ejecuta el comando recibido
                if command == 'encendido':
                    pyautogui.press('e')
                elif command == 'target':
                    pyautogui.press('t')

        except Exception as error:
            print(f"Connection error: {error}")
