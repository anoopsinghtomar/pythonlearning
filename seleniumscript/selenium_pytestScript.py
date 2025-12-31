import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()   
  
def test_python_org_navigation(driver):
    driver.get("https://www.python.org/")

    about_link = driver.find_element(By.XPATH, '//*[@id="about"]/a')
    assert about_link is not None

    doc_link = driver.find_element(By.XPATH, '//*[@id="documentation"]/a')
    doc_link.click()
    
    assert "docs" in driver.current_url.lower()
    