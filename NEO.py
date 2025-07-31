import subprocess
import threading
from datetime import datetime
import time
import webbrowser

# CONFIGURACION
assistant_name = "NEO"
user_name = ""

def NomUs():
    global user_name
    while True:
        user_name = input("por favor ingrese el nombre de usuario con el cual me voy a dirigir a usted: ").strip()
        if user_name:
            print(f"Perfecto, gusto en conocerte {user_name}")
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

def saludar_segun_hora():
    hora = datetime.now().hour

    if 5 <= hora < 11:
        print(f"\n[{assistant_name}] Buenos días . ¿Listo para un nuevo día?")
    elif 12 <= hora < 18:
        print(f"\n[{assistant_name}] Buenas tardes {user_name}. ¡Espero te este yendo bien!")
        if hora == 13 or hora == 20:
            print(
                f"\n[{assistant_name}] Buena suerte en Riwi {user_name}, ¡espero tus codigos salgan como quieres!")
    elif 18 <= hora < 22:
        print(
            f"\n[{assistant_name}] Buenas noches {user_name}. Espero hayas tenido un excelente dia.")
    else:
        print(
            f"\n[{assistant_name} 🔴] Ya es bastante tarde {user_name}. Recuerda que dormir bien es importante.")
saludar_segun_hora()


def abrir_app(nombre_app):
    if nombre_app in apps:
        try:
            subprocess.Popen(
                [apps[nombre_app]], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"[{assistant_name}] Abriendo {nombre_app}...")
        except FileNotFoundError:
            print(
                f"[{assistant_name}] No encontre la aplicacion ' {nombre_app}'. Asegurate de tenerla instalada")
    else:
        print(f"[{assistant_name}] No tengo registrada esa aplicación.")


def busquedas_web():
    comando = input(" Que quieres que busque? ").lower()
    if comando.startswith("busca"):
        busqueda = comando.replace("busca", "").strip()
        if busqueda:
            url = f"https://www.google.com/search?q={busqueda}"
            webbrowser.open(url)
            print(
                f"[{assistant_name}] Buscando '{busqueda}' en tu navegador predeterminado...")
        else:
            print(f"[{assistant_name}] No has especificado qué buscar.")


def alerta_nocturna():
    ya_avisado = False
    while True:
        hora_actual = datetime.now().hour
        if hora_actual >= 23:
            if not ya_avisado:
                print(f"\n [{assistant_name}] Ya es bastante tarde. Recuerda dormir a buena hora. Para poder cumplir satisfactoriamente con todas tus obligaciones.")
                ya_avisado = True
            else:
                print(
                    f"\n[{assistant_name}] Aun estas activo. Intenta dormir pronto")
            time.sleep(500)
        else:
            ya_avisado = False
            time.sleep(60)


hilo_noche = threading.Thread(target=alerta_nocturna)
hilo_noche.start()


def alerta_descanso():
    tiempo_inicio = time.time()
    intervalo_entre_alertas = 3600

    while True:
        tiempo_actual = time.time()
        tiempo_transcurrido = tiempo_actual - tiempo_inicio
        if tiempo_transcurrido >= intervalo_entre_alertas:
            print(
                f"\n [{assistant_name}] Has pasado en estado activo por mas de 1 hora. Tomate un descanso, estira las piernas e hidratate.")
            tiempo_inicio = time.time()


hilo_descanso = threading.Thread(target=alerta_descanso)
hilo_descanso.start()


def mostrar_menu():
    print("\n--- MENÚ DE COMANDOS DE NEO---")
    print("1. Abrir aplicación")
    print("2. Hacer busqueda en tu navegador")
    print("0. Salir")


# Bucle principal
while True:
    mostrar_menu()
    opcion = input(f"\n[{assistant_name}] ¿Qué deseas hacer?: ")
    if opcion == "1":
        app = input(
            f"[{assistant_name}] ¿Qué aplicación quieres abrir?: ").lower()
        abrir_app(app)
    elif opcion == "2":
        busquedas_web()
    elif opcion == "0":
        print(f"[{assistant_name}] Hasta pronto, cuídate.")
        break

    else:
        print(f"[{assistant_name}] No entendí eso. Intenta otra opción.")
