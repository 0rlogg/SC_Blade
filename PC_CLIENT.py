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

# Variables de estado para detectar Shift + e
shift_pressed = False

def on_press(key):
    global shift_pressed

    try:
        if key == pynput_keyboard.Key.shift:
            shift_pressed = True
        elif key.char == 'e' and shift_pressed:
            send_command('encendido')
    except AttributeError:
        pass

def on_release(key):
    global shift_pressed

    if key == pynput_keyboard.Key.shift:
        shift_pressed = False

# Listener para el teclado
keyboard_listener = pynput_keyboard.Listener(on_press=on_press)
keyboard_listener.start()

keyboard_listener.join()
