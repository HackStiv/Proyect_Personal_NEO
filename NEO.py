import subprocess
import threading
from datetime import datetime
import time
import webbrowser

# CONFIGURACION
assistant_name = "NEO"
user_name = ""

def NomUs():
    global nombre_usuario
    while True:
        nombre_usuario = input("por favor ingrese el nombre de usuario con el cual me voy a dirigir a usted: ").strip()
        if nombre_usuario:
            print(f"Perfecto, gusto en conocerte {nombre_usuario}")
            break
        else:
            print("Por favor, ingrese un nombre válido (no puede estar vacío).")

NomUs()

# Lista de apps que puede abrir (ajústalas a tus rutas)
apps = {
    # Aqui lo que hice fue dejar algo preestablecido pero necesitas cambiar el nombre del usario al de tu sistema en si.
    "chrome": "google-chrome",
    "libreoffice": "libreoffice",
    "brave": "brave",
    "visualstudio": "code",
    "visual": "code",
    "visualstudiocode": "code",
    "discord": "discord"
}