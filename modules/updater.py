import requests
import subprocess
from config import Config

def check_for_updates():
    try:
        # Obtener el último commit del repositorio de GitHub
        response = requests.get(f"{Config.GITHUB_REPO_URL}/commits/berta")
        response.raise_for_status()  # Lanza una excepción para códigos de error HTTP
        latest_version = response.json()["sha"][:7]  # Obtener los primeros 7 caracteres del SHA

        # Comparar la versión actual con la última versión
        if latest_version > Config.VERSION:
            print("Hay una nueva versión disponible.")
            return latest_version
        else:
            print("No hay actualizaciones disponibles.")
            return None
    except requests.exceptions.RequestException as e:
        print("No se puede verificar la actualización.")
        return None

def update_program(latest_version):
    try:
        # Descargar la nueva versión
        print("Descargando la nueva versión...")
        subprocess.run(["git", "pull"], check=True, cwd=os.path.dirname(os.path.abspath(__file__)))

        # Actualizar la versión en el archivo de configuración
        print("Actualizando la versión...")
        with open("config.py", "w") as f:
            f.write(f'VERSION = "{latest_version}"')

        print("Programa actualizado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al actualizar el programa: {e}")
