import os
from pathlib import Path
from posix import listdir
from pdfminer import high_level
from pdf2image import convert_from_path
import requests
import Secret_Holder

# https://api.holded.com/api/invoicing/v1/documents/docType/documentId/pdf Get_List_Of_DocId_With_DocNum

def Get_List_Of_Docs():
    url = "https://api.holded.com/api/invoicing/v1/documents/salesreceipt"

    headers = {
        "Accept": "application/json",
        "key": Secret_Holder.Holded_API
    }

    response = requests.request("GET", url, headers=headers)

    return response

def Get_Doc_by_DocId(docId):
    url = "https://api.holded.com/api/invoicing/v1/documents/salesreceipt/" + docId

    headers = {
        "Accept": "application/json",
        "key": "0476c2dcf451e748daf1c33c08c746cf"
    }

    response = requests.request("GET", url, headers=headers)

    return response

def Group_DocId_By_DocNum():
    list_of_docs = Get_List_Of_Docs()
    list_of_items_in_docs = list_of_docs.text.split(",")
    
    for element in list_of_items_in_docs:
        if "\"desc\":" in element:
            if ("\"desc\":\"\"" != element):
                yield element

        if ("\"id\":\"" in element):
            if not (("\"paymentsDetail\":[{\"id\"" in element) or ("\"from\":{\"id\":\"" in element)):
                yield element

def Extract_Doc_text(filename): #This function can fail be carefull
    text = high_level.extract_text(filename)
    text_separated_by_new_line = text.split("\n")
    for element in text_separated_by_new_line:
        if(element != ""):
            yield element

def Extract_DocNum_of_pdf(doc_text):
    for elements in doc_text:
        new_elements = elements.split("-")
        if 3 == len(new_elements): 
            if (str.isdecimal(new_elements[0])and str.isdecimal(new_elements[1]) and str.isdecimal(new_elements[2])):
                return elements

def Extract_info_of_pdf(pdf_text, doc_name_):
    i = 0

    for element in pdf_text:

        if doc_name_ == element:
            k = pdf_text.index(element)
            fecha = pdf_text[k - 2]

        if "€" in element:
            i = pdf_text.index(element)

        if "www.amazon." in element:
            nombre = pdf_text[i + 1]
            
            if ((pdf_text[i + 18].replace(" ", "") in pdf_text[i + 19]) and (pdf_text[i + 18].replace(" ", "") != pdf_text[i + 19].replace(" ", ""))):
                cif = pdf_text[i + 19]
                return nombre, cif, fecha

            return nombre, fecha

def Extract_eur(doc_text):
    array = []

    for element in doc_text:
        if "€" in element:
            array.append(element)
    
    if (len(array)>3):
        final_array = [array[0], array[-4], array[-1]]

        return final_array

    return array


def Generator_to_array(generator):
    array = []

    for i in generator:
        array.append(i)

    return array

def Get_files(path_):
    folder = os.path.realpath(path_)
    files = listdir(folder)
    return files

# doc_name = "INV-DE-910864895-2021-40.pdf"
# doc_name = "CN-DE-910864895-2021-3.pdf"
# doc_name = "CN-FR-910864895-2021-3.pdf"
doc_name = "INV-FR-910864895-2021-65.pdf"

def Get_all_info(doc_name):
    doc_text = Extract_Doc_text(doc_name)
    docNum = Extract_DocNum_of_pdf(doc_text)
    list_Of_Docs = Group_DocId_By_DocNum()

    for i in list_Of_Docs:
        if ("id" in i):
            new_docId = i

        if ("desc" in i):
            new_docNum = i 

            if(docNum in new_docNum):
                break

    docIds = new_docId.split("\"")
    docId = docIds[3]
    Doc = Get_Doc_by_DocId(docId)


    doc_text_ = Extract_Doc_text(doc_name)
    array_text = Generator_to_array(doc_text_)
    
    doc_name_ = str(doc_name).split(r'/')
    _doc_name_ = doc_name_[-1].replace('.pdf', "")

    doc_info = Extract_info_of_pdf(array_text, _doc_name_)
    doc_info_eur = Extract_eur(array_text)
    
    return Doc, doc_info, doc_info_eur 

def Retrive_files(path): #retrives archives from a folder (returns Posix not strings)
    first_files = list(reversed(sorted(Path(path).iterdir(), key=os.path.getmtime)))
    return first_files


path_ = r'/Volumes/GoogleDrive/Unidades compartidas/BEYONDTECH EUROPE/CONTABILIDAD/Facturas EMITIDAS- Clientes -PAN EUROPEO/Pan Europeo/Por Paises/Alemania/2021/3.- Marzo'
files = Retrive_files(path_)

for file in files:
    all_info = Get_all_info(file)
    print(all_info)
