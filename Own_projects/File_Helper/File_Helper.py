import os,shutil
from pathlib import Path

def Find_last_downloads():
    path = r'C:\Users\alfon\Downloads'
    # first_files = os.listdir(path)
    first_files = list(reversed(sorted(Path(path).iterdir(), key=os.path.getmtime)))
    return first_files
    
def Check_folder(my_last_downloads):
    print("is this your folder? type y/n and press enter")
    last_download = my_last_downloads[0]
    print(last_download)
    response_input = input()
    
    if(response_input == "y"):
        return last_download
    
    elif(response_input == "n"):
        print("type name of the file you want")
        my_folder = input()
        return Find_folder(my_folder, my_last_downloads)

    else:
        print("invalid response try it again:")
        Check_folder(my_last_downloads)

def Find_folder(my_folder, last_downloads):
    for elements in last_downloads:
        if(my_folder == elements):
            return elements
        
        print("folder not found")

def Analize_my_folder(my_folder):
    list_of_files = os.listdir(my_folder)
    for elements in list_of_files:
        if "ES" in elements:
            print("España")

last_downloads = Find_last_downloads()
my_folder = Check_folder(last_downloads)
Analize_my_folder(my_folder)

#Descargas
#BEYONDTECH EUROPE/CONTABILIDAD/Facturas EMITIDAS- Clientes -PAN EUROPEO/Pan Europa/Por Paises/España