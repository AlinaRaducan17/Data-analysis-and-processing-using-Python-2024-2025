"""## Set comenzi pentru automatizare de Django
1. Adaugare aplicatie/aplicatii
2. Adaugare in settings
3. Creare folder templates
4. Creare fisier urls.py pt fiecare aplicatie
5. Creare perechi view+template"""

import os
import subprocess
import time
import shutil

#verifica sistemul de operare este windows
if os.name == "nt":
    python_command = "python"
#in caz contrar mac/linux
else:
    python_command = "python3"
    
# PROJECT_NAME = "myproject"
# CREARE_PROJECT = f"{python_command} -m django startproject {PROJECT_NAME}"
# print(CREARE_PROJECT)

def create_project(project_name="test_project"):
    CREATE_PROJECT_CMD = f"{python_command} -m django startproject {project_name}"
    #CREATE_PROJECT_CMD = f"{python_command} -m django startproject {project_name} ." - cu punct ca sa nu obtinem eroare si sa creeze automat folderul de app in folderul de project
    subprocess.call(CREATE_PROJECT_CMD, shell=True)
    
def delete_project(project_name="test_project"):
    shutil.rmtree(project_name)
    
def create_application(app_name="test_app", project_name="test_project"):
    #current working directory
    cwd = os.getcwd() #cwd = current working directory
    print("Inainte de a schimba path-ul", cwd)
    os.chdir(os.path.join(cwd, project_name))
    print("Dupa schimbarea path-ului", os.getcwd())
    
    CREATE_APP_CMD = f"{python_command} manage.py startapp {app_name}"
    subprocess.call(CREATE_APP_CMD, shell=True)



if __name__ == "__main__":
    #print(os.getcwd())
    
    create_project()
    time.sleep(3)
    create_application()
    
    #delete_project()