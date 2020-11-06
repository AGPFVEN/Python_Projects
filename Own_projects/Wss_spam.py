# import webbrowser 

# webbrowser.open_new("https://web.whatsapp.com/")
from selenium import webdriver

path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
driver = webdriver.Chrome(path)

driver.get("https://web.whatsapp.com")

# contact_search = driver.find_element_by_class_name( "_3FRCZ copyable-text selectable-text")

# print(contact_search)