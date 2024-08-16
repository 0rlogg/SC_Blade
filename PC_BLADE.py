import socket
import time
import pyautogui  
    

# Configure the IP address and port
HOSTNAME = socket.gethostname()
HOST =  input('type the ip of the pc-server')
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


        except Exception as error:
            print(f"Error de conexión: {error}")
