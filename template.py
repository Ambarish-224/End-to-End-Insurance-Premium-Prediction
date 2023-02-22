import os
from pathlib import Path
import logging

logging.basicConfig(
    level = logging.INFO,
    format = "[%(asctime)s: %(levelname)s]: %(message)s"
)

while True:
    project_name = input("Enter your project name: ")
    if project_name !='':
        break

logging.info(f"Creating project by name: {project_name}")

lists_of_files = [
    ".github/workflows/.gitkeep",
    ".github/workflows/main.yaml",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/config.py",
    f"{project_name}/exception.py",
    f"{project_name}/predictor.py",
    f"{project_name}/utils.py",
    f"configs/config.yaml",
    "requirements.txt",
    "setup.py",
    "main.py"
]

for filepath in lists_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Creating a new directory at : {filedir} for file :{filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
      with open(filepath, "w") as f:
        pass
        logging.info(f"Creating a new file: {filename} for path: {filepath}")
    else:
        logging.info(f"file is already present at: {filepath}")