from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.python.org/")
driver.find_element(by=By.XPATH, value='//*[@id="about"]/a')
driver.maximize_window()
driver.find_element(by=By.XPATH, value='//*[@id="documentation"]/a').click()

# driver.close()