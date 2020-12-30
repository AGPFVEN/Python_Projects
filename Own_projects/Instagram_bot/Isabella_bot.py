from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path_webdriver = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(path_webdriver)

driver.get("https://www.instagram.com/")
# driver.get("https://www.instagram.com/")

#Accept cookies
cookies_class_name = "aOOlW   HoLwm "

# driver.find_element_by_class_name("aOOlW   HoLwm ")
username = driver.find_element_by_name("username")
username.send_keys("kk")

# try:
# cookie_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "aOOlW   HoLwm ")))
# cookie_button.click()
# except:
#     print("cookies failed")

# except:
#     # driver.quit()
#     print("cookies failed")