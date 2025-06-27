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

#def create_project(project_name="test_project", app_name="test_app"): pt o aplicatie
def create_project(project_name="test_project", *applications): #pt mai multe aplicatii
    CREATE_PROJECT_CMD = f"{python_command} -m django startproject {project_name}"
    #CREATE_PROJECT_CMD = f"{python_command} -m django startproject {project_name} ." - cu punct ca sa nu obtinem eroare si sa creeze automat folderul de app in folderul de project
    subprocess.call(CREATE_PROJECT_CMD, shell=True)
    for app_name in applications: #pt a crea mai multe aplicatii
        create_application(app_name, project_name)
        
        
def delete_project(project_name="test_project"):
    shutil.rmtree(project_name)
    
def project_path(project_name="test_project"):
    return os.path.join(os.getcwd(), project_name)
    
def inner_project_path(project_name="test_project"):
    return os.path.join(os.getcwd(), project_name, project_name)

def app_path(app_name="test_app", project_name="test_project"):
    return os.path.join(os.getcwd(), project_name, app_name)

def change_cwd(path):
    def change_back_cwd(function):    
        def inner_function(*args, **kwargs):
            cwd = os.getcwd()
            print(kwargs)
            if kwargs:
                result = function(*args, **kwargs)
            elif args:
                result = function(app_name=args[0], project_name=args[1])
            os.chdir(cwd)
            return(result)
        return inner_function
    
@change_cwd(project_path(project_name="test_project"))
def create_application(app_name="test_app", project_name="test_project"):
    os.chdir(project_path(project_name))
    #current working directory
    # cwd = os.getcwd() #cwd = current working directory
    # print("Inainte de a schimba path-ul", cwd)
    # os.chdir(os.path.join(cwd, project_name))
    # print("Dupa schimbarea path-ului", os.getcwd())
    
    CREATE_APP_CMD = f"{python_command} {project_name}/manage.py startapp {app_name}"
    #CREATE_APP_CMD = f"{python_command} manage.py startapp {app_name}"
    subprocess.call(CREATE_APP_CMD, shell=True)
    time.sleep(0.5)
    setup_application(app_name, project_name)

def setup_application(app_name="test_app", project_name="test_project"):
    _add_app_to_installed_apps(app_name, project_name)
    _create_templates_folder(app_name, project_name)
    _create_app_url_file(app_name, project_name)
    _link_app_in_project_url_file(app_name, project_name)

def _add_app_to_installed_apps(app_name="test_app", project_name="test_project"):
    # cwd = os.getcwd() #cwd = current working directory
    # print("Inainte de a schimba path-ul", cwd)
    # os.chdir(os.path.join(cwd, project_name))
    # print("Dupa schimbarea path-ului", os.getcwd())
    
    # cwd = os.getcwd()
    # os.chdir(os.path.join(cwd, project_name))
    # print("Dupa schimbarea path-ului", os.getcwd())
    
    #with open("settings.py", "r") as freader:
    with open(f"{inner_project_path(project_name)}/settings.py", "r") as freader:
        settings_content = freader.readlines()
        #print(settings_content)
    
    has_encounter_installed_apps = False
    for index, line in enumerate(settings_content):
        if "INSTALLED_APPS = [" in line:
            has_encounter_installed_apps = True
            print("has encounter")
        elif has_encounter_installed_apps and ("]" in line):
            settings_content.insert(index, f"\t'{app_name}',\n")
            break
    
    print("\n".join(settings_content))   
         
    #with open("settings.py", "w") as fwriter:
    with open(f"{inner_project_path(project_name)}/settings.py", "w") as fwriter:
        fwriter.writelines(settings_content)

def _create_templates_folder(app_name="test_app", project_name="test_project"):
    # cwd = os.getcwd()
    # os.chdir(os.path.join(cwd, project_name, app_name))
    #TEMPLATES = "templates"
    TEMPLATES = f"{app_path(app_name, project_name)}/templates"
    os.makedirs(TEMPLATES, exist_ok=True)
    
def _create_app_url_file(app_name="test_app", project_name="test_project"):
    # cwd = os.getcwd()
    # os.chdir(os.path.join(cwd, project_name, app_name))
    #URLS_FILE_NAME = "urls.py"
    URLS_FILE_NAME =  f"{app_path(app_name, project_name)}/urls.py"
    URLS_CONTENT ="""from django.urls import path \n\nurlpatterns = [\n\n]\n"""
    with open(URLS_FILE_NAME, "w") as fwriter:
        fwriter.write(URLS_CONTENT)
        
def _link_app_in_project_url_file(app_name="test_app", project_name="test_project"):
    # cwd = os.getcwd()
    # os.chdir(os.path.join(cwd, project_name, project_name))
    with open(f"{inner_project_path(project_name)}/urls.py", "r") as freader:
        urls_lines = freader.readlines()
    
    print(urls_lines)
    has_encounter_urlpatterns = False
    new_line = f"\tpath('{app_name}/', include('{app_name}.urls')),\n"
    if new_line in urls_lines:
        return
    
    for index, line in enumerate(urls_lines):
        if 'from django.urls import path' in line and 'include' not in line:
            urls_lines[index] = line.replace("path", "path, include")
        if "urlpatterns = [" in line:
            has_encounter_urlpatterns = True
        elif has_encounter_urlpatterns and "]" in line:
            urls_lines.insert(index, new_line)
            break
        
    with open(f"{inner_project_path(project_name)}/urls.py", "w") as fwriter:
        fwriter.writelines(urls_lines)
    
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
    #demo_enumerate()
    # create_project()
    create_project("proiectul_meu", "app1", "app2")
    #create_application("app3", "proiectulmeu")
    # time.sleep(3)
    # create_application()
    #_create_templates_folder()
    #_create_app_url_file()
    #_add_app_to_installed_apps()
    
    # _link_app_in_project_url_file()
    #delete_project()