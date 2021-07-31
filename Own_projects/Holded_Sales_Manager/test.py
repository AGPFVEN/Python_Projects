from os import replace
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
            print(doc_name_)
            print(element)
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


def Generator_to_array(generator):
    array = []

    for i in generator:
        array.append(i)

    return array

# INV-DE-910864895-2021-40.pdf CN-DE-910864895-2021-3.pdf CN-FR-910864895-2021-3.pdf INV-FR-910864895-2021-65.pdf

#Extract_info_of_pdf('INV-ES-910864895-2021-184.pdf')


# doc_name = "INV-DE-910864895-2021-40.pdf"
# doc_name = "CN-DE-910864895-2021-3.pdf"
# doc_name = "CN-FR-910864895-2021-3.pdf"
doc_name = "INV-FR-910864895-2021-65.pdf"

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
doc_info = Extract_info_of_pdf(array_text, doc_name.replace('.pdf', ""))
print(array_text)
print(doc_info)
# print(array_text.index(doc_info))

# for i in doc_text:
#     print(i)
# kk =Generator_to_array(Extract_Doc_text('INV-DE-910864895-2021-40.pdf'))
# print(kk[1])
# print(high_level.extract_text('INV-DE-910864895-2021-40.pdf'))
