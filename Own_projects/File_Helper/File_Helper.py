import os,shutil
from pathlib import Path

def Find_last_downloads():
    path = r'C:\Users\alfon\Downloads'
    # first_files = os.listdir(path)
    first_files = list(reversed(sorted(Path(path).iterdir(), key=os.path.getmtime)))
    return first_files
    
def Check_folder(my_last_downloads):
    print("is this your folder? y/n")
    last_download = my_last_downloads[0]
    print(last_download)
    response_input = input()
    
    if(response_input == "y"):
        return last_download
    
    elif(response_input == "n"):
        print("no")

    else:
        print("invalid response try it again:")
        Check_folder(last_download)

def Find_folder__(my_folder, last_downloads):
    for elements in last_downloads:
        if(my_folder == elements):
            return elements
        
        print("folder not found")



last_downloads = Find_last_downloads()

#Descargas
#BEYONDTECH EUROPE/CONTABILIDAD/Facturas EMITIDAS- Clientes -PAN EUROPEO/Pan Europa/Por Paises/España