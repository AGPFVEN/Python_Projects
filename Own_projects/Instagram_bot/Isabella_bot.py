from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path_webdriver = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(path_webdriver)

driver.get("https://www.google.es/search?source=hp&ei=w8nrX4LDMo6UlwSmhJvADQ&q=kahoot&gs_ssp=eJzj4tVP1zc0TKosyS3MMjE0YPRiy07MyM8vAQBUZAdC&oq=kah&gs_lcp=CgZwc3ktYWIQAxgAMggILhCxAxCTAjIFCAAQsQMyBQgAELEDMgUIABCxAzIFCAAQsQMyAggAMgUIABCxAzICCAAyAggAMgUILhCxAzoLCAAQsQMQxwEQowI6DggAELEDEIMBEMcBEKMCOggIABCxAxCDAToFCC4QkwI6AgguOggILhCxAxCDAToLCAAQsQMQxwEQrwE6DggAELEDEIMBEMcBEK8BOggIABDHARCvAToHCAAQsQMQCjoHCC4QsQMQCjoECAAQClDL8wFYqawCYNq3AmgHcAB4AIABUogBwQOSAQE2mAEAoAEBqgEHZ3dzLXdperABAA&sclient=psy-ab")
# driver.get("https://www.instagram.com/")

#Accept cookies
cookies_class_name = "aOOlW   HoLwm "

# driver.find_element_by_class_name("aOOlW   HoLwm ")

# try:
# cookie_button = WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "aOOlW   HoLwm ")))
# cookie_button.click()
# except:
#     driver.quit()
#     print("cookies failed")

# try:
cookie_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "RveJvd snByac")))
cookie_button.click()
# except:
#     # driver.quit()
#     print("cookies failed")