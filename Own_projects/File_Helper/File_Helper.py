import os,shutil
from pathlib import Path

def Find_folder():
    path = r'C:\Users\alfon\Downloads'
    # first_files = os.listdir(path)
    first_files = sorted(Path(path).iterdir(), key=os.path.getmtime)
    print(first_files)
    print("is this your folder? y/n")
    fist_file = first_files[0]
    response_input = input()
    
    if(response_input == "y"):
        return fist_file
    
    elif(response_input == "n"):
        print("no")

    else:
        print("invalid response try it again:")
        Find_folder()

def Find_folder__(my_folder):
    path = r'C:\Users\alfon\Downloads'
    first_files = os.listdir(path)
    
    for elements in first_files:
        if(my_folder == "elements"):
            return elements
        
        print("not found")


print(Find_folder())



#Descargas
#BEYONDTECH EUROPE/CONTABILIDAD/Facturas EMITIDAS- Clientes -PAN EUROPEO/Pan Europa/Por Paises/España