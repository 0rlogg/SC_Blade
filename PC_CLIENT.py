import socket
from pynput import keyboard as pynput_keyboard

# Configura la dirección IP y el puerto del PC secundario
SERVER_IP = '192.168.1.242'  # Reemplaza con la dirección IP del PC secundario
SERVER_PORT = 61000  # Elige un puerto disponible

ALLOWED_KEYS = {'e', '0', 't', '1', '5'}  # Lista de teclas permitidas

def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_INFO:
        socket_INFO.connect((SERVER_IP, SERVER_PORT))
        socket_INFO.sendall(command.encode('utf-8'))

def simulate_key_press_release(key):
    try:
        with pynput_keyboard.Controller() as controller:
            controller.press(key)
            controller.release(key)
    except Exception as error:
        print(f"Error al simular la pulsación de tecla: {error}")

# Define las teclas que activarán los comandos
encender_puesto = 'shift' + 'e' 
disparar = '0'  
target = 't'  
MM = '1' 
center_turret = '5'

def on_press(key):
    try:
        key_char = key.char
    except AttributeError:
        key_char = str(key)

    if key_char in ALLOWED_KEYS:
        if key_char == encender_puesto:
            send_command('encendido')
        elif key_char == disparar:
            send_command('disparar')
        elif key_char == target:
            send_command('target')
        elif key_char == MM:
            send_command('MM')
        elif key_char == center_turret:
            send_command('center_turret')

        simulate_key_press_release(key_char)

# Listener para el teclado
keyboard_listener = pynput_keyboard.Listener(on_press=on_press)
keyboard_listener.start()

keyboard_listener.join()
