import os

class Config:
    VERSION = "0.1.0"
    GITHUB_REPO_URL = "https://github.com/Narckano/Notebook2.git"
    MODULES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "modules")
