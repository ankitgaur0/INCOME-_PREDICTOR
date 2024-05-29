import os
import sys
from pathlib import Path
#this should be the name of project
package_name="INCOME_PREDICTOR"
#create a list of all the folders and files
list_of_files=[
    ".github/workflows/main.yaml",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/components/data_injection.py",
    f"src/{package_name}/components/data_tranformation.py",
    f"src/{package_name}/components/model_training.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/pipeline/training_pipline.py",
    f"src/{package_name}/pipeline/prediction_pipline.py",
    f"src/{package_name}/utils/utils.py",
    f"src/{package_name}/logging.py",
    f"src/{package_name}/exception_handle.py",
    f"src/{package_name}/logger.py",

    "notebook/__init__.py",
    "notebook/data",
    "notebook/EDA.ipynb",

    "notebook/model_trainer.ipynb",
    "setup.py",
    "__init__.py",
    "app.py",
    "dockerfile"
]


for filepath in list_of_files:
    filepath=Path(filepath)
    #now i have to split the file directory and file name
    file_dir,file_name=os.path.split(filepath)
    #os.path.join(filepath)

    if(file_dir !=""):
        os.makedirs(file_dir,exist_ok=True)

    if(not os.path.exists(filepath) or os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass

    else:
        print("path is already existing state")