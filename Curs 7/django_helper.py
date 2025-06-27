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

def _add_app_to_installed_apps(app_name="test_app", project_name="test_project"):
    cwd = os.getcwd() #cwd = current working directory
    print("Inainte de a schimba path-ul", cwd)
    os.chdir(os.path.join(cwd, project_name))
    print("Dupa schimbarea path-ului", os.getcwd())
    
    cwd = os.getcwd()
    os.chdir(os.path.join(cwd, project_name))
    print("Dupa schimbarea path-ului", os.getcwd())
    
    with open("settings.py", "r") as freader:
        settings_content = freader.readlines()
        print(settings_content)
    
    has_encounter_installed_apps = False
    for index, line in enumerate(settings_content):
        if "INSTALLED_APPS = [" in line:
            has_encounter_installed_apps = True
            print("has encounter")
        elif has_encounter_installed_apps and ("]" in line):
            settings_content.insert(index, f"\t'{app_name}',\n")
            break
    
    print("\n".join(settings_content))   
         
    with open("settings.py", "w") as fwriter:
        fwriter.writelines(settings_content)
        
def demo_enumerate():
    lista_mea = ["Maria", "Ion", "Gheorge", "Vasile"]
    for index, element in enumerate(lista_mea):
        print(index, element)
        if element == "Gheorge":
            lista_mea.insert(index, "Florina")
            break
    print(lista_mea)
        
if __name__ == "__main__":
    
    #print(os.getcwd())
    demo_enumerate()
    # create_project()
    # time.sleep(3)
    # create_application()
    
    #_add_app_to_installed_apps()
    
    #delete_project()