https://github.com/Narckano/Notebook2.git from config import Config
from modules import updater

def main():
    print(f"Productivity Program v{Config.VERSION}")
    updater.check_for_updates()

if __name__ == "__main__":
    main()
