import socket
import subprocess
import sys
import time
import pyautogui

# Verifica si pyautogui está instalado e intenta instalarlo si no lo está.
try:
    import subprocess
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'subprocess'])
    import subprocess
try:
    import sys
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'sys'])
    import sys
try:
    import pyautogui
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyautogui'])
    import pyautogui
try:
    import time
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'time'])
    import time
try:
    import socket
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'socket'])
    import socket   
    

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

        except Exception as error:
            print(f"Error de conexión: {error}")
