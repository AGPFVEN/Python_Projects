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
        print("type name of the folder you want")
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

def Month_calculator(number_of_month, name_of_month):
    return str(number_of_month + ".- " + name_of_month)

def Month_printer(number_of_month):
    if(number_of_month == "1"):
        return Month_calculator("1", "Enero")

    if(number_of_month == "2"):
        return Month_calculator("2", "Febrero")

    if(number_of_month == "3"):
        return Month_calculator("3", "Marzo")

    if(number_of_month == "4"):
        return Month_calculator("4", "Abril")

    if(number_of_month == "5"):
        return Month_calculator("5", "Mayo")

    if(number_of_month == "6"):
        return Month_calculator("6", "Junio")

    if(number_of_month == "7"):
        return Month_calculator("7", "Julio")

    if(number_of_month == "8"):
        return Month_calculator("8", "Agosto")

    if(number_of_month == "9"):
        return Month_calculator("9", "Septiembre")

    if(number_of_month == "10"):
        return Month_calculator("10", "Octubre")
    
    if(number_of_month == "11"):
        return Month_calculator("11", "Noviembre")

    if(number_of_month == "12"):
        return Month_calculator("12", "Diciembre")

def Analize_my_folder(my_files):
    print("Input month (numerically)")
    month = str(input())
    print("Input year")
    year = str(input())
    path_old = "/Volumes/GoogleDrive/Unidades compartidas/BEYONDTECH EUROPE/CONTABILIDAD/Facturas EMITIDAS- Clientes -PAN EUROPEO/Pan Europeo/Por Paises/"
    for element in my_files:
        print(element)
        if "DE" in str(element):
            path = path_old + "Alemania/" + year + "/" + Month_printer(month)

        if "ES" in str(element):
            path = path_old + "España/" + year + "/" + Month_printer(month)

        if "FR" in str(element):
            path = path_old + "Francia/" + year + "/" + Month_printer(month)

        if "IT" in str(element):
            path = path_old + "Italia/" + year + "/" + Month_printer(month)

        if "PL" in str(element):
            path = path_old + "Polonia/" + year + "/" + Month_printer(month)

        if "GB" in str(element):
            path = path_old + "Reino Unido/" + year + "/" + Month_printer(month)

        if "CZ" in str(element):
            path = path_old + "Republica Checa/" + year + "/" + Month_printer(month)

        shutil.move(element, path)

my_downloads = Retrive_files(r'/Users/gianinafernandez/Downloads')
my_folder = Check_folder(my_downloads)
my_files= Retrive_files(my_folder)
Analize_my_folder(my_files)

#Descargas
#taxInvoice_d80fc5f11fe37fb52935487f22881a21112ff42e
#/Volumes/GoogleDrive/Unidades compartidas/BEYONDTECH EUROPE/CONTABILIDAD/Facturas EMITIDAS- Clientes -PAN EUROPEO/Pan Europeo/Por Paises