import os,shutil
from pathlib import Path
from typing import Type

def Retrive_files(path): #retrives archives from a folder (returns Posix not strings)
    first_files = list(reversed(sorted(Path(path).iterdir(), key=os.path.getmtime)))
    return first_files
    
def Check_folder(my_last_downloads): #check if the file is the correct one
    print("is this your folder? type y/n and press enter")
    last_download = my_last_downloads[1]    
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

def Find_folder(my_folder, last_downloads): #Search a folder or file
    for element in last_downloads:
        if "/Users/gianinafernandez/Downloads/" + my_folder == str(element):
            return element

    print(my_folder + " Not found")

def Analize_my_folder(my_files):
    for element in my_files:
        if "ES" in element:
            print("ESSSS")

my_downloads = Retrive_files(r'/Users/gianinafernandez/Downloads')
my_folder = Retrive_files(Check_folder(Retrive_files(r'/Users/gianinafernandez/Downloads')))
Analize_my_folder(my_folder)

#Descargas
#taxInvoice_a59a69add60f2eed6c934e0e49ad6684cf54edb4
#BEYONDTECH EUROPE/CONTABILIDAD/Facturas EMITIDAS- Clientes -PAN EUROPEO/Pan Europa/Por Paises/España