import sys
sys.path.append("D:\\python_agpfven\\lib\\site-packages")

from selenium import webdriver

path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.wikipedia.org/")

# contact_search = driver.find_exelement_by_class_name( "_3FRCZ copyable-text selectable-text")

# print(contact_search)