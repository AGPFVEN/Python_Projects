import sys
sys.path.append("D:\\python_agpfven\\lib\\site-packages")

from selenium import webdriver

path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.wikipedia.org/") 