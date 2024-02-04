from cgitb import text
from logging import root
import socket
import time
import pyautogui
import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Blade_Server")
ventana.geometry("2000x750")  # Formato: anchura x altura + posición_x + posición_y
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)
ventana.columnconfigure(3, weight=1)

# Crear un widget de etiqueta
etiqueta_IP = tk.Label(ventana, text="IP CLIENT:")
entrada_IP = tk.Entry(ventana)

etiqueta_IP.grid(row=0, column=0, padx=10, pady=10)
entrada_IP.grid(row=0, column=1, padx=10, pady=10)

etiqueta_PORT = tk.Label(ventana, text="PORT CLIENT:")
entrada_PORT = tk.Entry(ventana)

etiqueta_PORT.grid(row=0, column=2, padx=10, pady=10)
entrada_PORT.grid(row=0, column=3, padx=10, pady=10)


separator = ttk.Separator(ventana, orient="horizontal")
separator.grid(row=1, column=0, columnspan=10, pady=10, sticky="ew")

def cambiar_tema():

    tema_actual = ventana.tk_getPalette()

    if tema_actual == "default":
         ventana.tk_setPalette(background='#2E2E2E', foreground='white')
    else:
         ventana.tk_setPalette(background='#ffffff', foreground='black')

ventana = tk.Tk()
ventana.title("Cambiar Tema")

# Crear un botón para cambiar el tema
boton_cambiar_tema = tk.Button(ventana, text="Cambiar Tema", command=cambiar_tema)
boton_cambiar_tema.pack(pady=10)
#boton_cambiar_tema = tk.Button(ventana, text="Cambiar Tema")

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()

# Configura la dirección IP y el puerto
HOST = entrada_IP.get() # La misma IP que especificaste en el script del PC principal
PORT = entrada_PORT.get() # El mismo puerto que especificaste en el script del PC principal

print (HOST) #po
print (PORT)

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
