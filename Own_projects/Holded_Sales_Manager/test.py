import requests
from pdfminer import high_level
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
    return text_separated_by_new_line

def Extract_DocNum_of_pdf(doc_text):
    for elements in doc_text:
        new_elements = elements.split("-")
        if 3 == len(new_elements): 
            if (str.isdecimal(new_elements[0])and str.isdecimal(new_elements[1]) and str.isdecimal(new_elements[2])):
                return elements
    
# INV-ES-910864895-2021-184.pdf INV-DE-910864895-2021-40.pdf

doc_text = Extract_Doc_text("INV-DE-910864895-2021-40.pdf")
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
print(doc_text)
