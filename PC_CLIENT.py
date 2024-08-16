import socket
from pynput import keyboard as pynput_keyboard

# Configura la dirección IP y el puerto del PC secundario
SERVER_IP = '192.168.1.242'  # Reemplaza con la dirección IP del PC secundario
SERVER_PORT = 61000  # Elige un puerto disponible

# Variable de estado para controlar el envío de comandos
command_sending_enabled = False
shift_pressed = False

def send_command(command):
    if command_sending_enabled:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_INFO:
            socket_INFO.connect((SERVER_IP, SERVER_PORT))
            socket_INFO.sendall(command.encode('utf-8'))
            print(f"Comando enviado: {command}")

def on_press(key):
    global command_sending_enabled, shift_pressed

    try:
        if key == pynput_keyboard.Key.shift:
            shift_pressed = True
        elif key.char == 'e' and shift_pressed:
            send_command('encendido')
        elif key.char == '.':
            command_sending_enabled = not command_sending_enabled
            state = "activado" if command_sending_enabled else "desactivado"
            print(f"El envío de comandos ha sido {state}.")
    except AttributeError:
        pass

def on_release(key):
    global shift_pressed
    if key == pynput_keyboard.Key.shift:
        shift_pressed = False

# Listener para el teclado
keyboard_listener = pynput_keyboard.Listener(on_press=on_press, on_release=on_release)
keyboard_listener.start()

keyboard_listener.join()
