import Secret_Holder
import requests

# https://api.holded.com/api/invoicing/v1/documents/docType/documentId/pdf Get_List_Of_DocId_With_DocNum

def Get_List_Of_Docs():
    url = "https://api.holded.com/api/invoicing/v1/documents/salesreceipt"

    headers = {
        "Accept": "application/json",
        "key": Secret_Holder.Holded_API
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


# print(Get_List_Of_Docs())
mylist = Group_DocId_By_DocNum()
for i in mylist:
    print(i)