from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
import requests
from selenium.webdriver.support.wait import WebDriverWait

Path = "D:\Python\chromedriver.exe"
driver = webdriver.Chrome(Path)

def OpenDemo():

    driver.get("https://demoqa.com/text-box")
    driver.implicitly_wait(2)
    driver.maximize_window()
    username=driver.find_element_by_id("userName")
    driver.implicitly_wait(2)

    username.send_keys("Hasmik")
    email=driver.find_element_by_id("userEmail")
    email.send_keys("testingemail@gmail.com")
    driver.implicitly_wait(2)

    currentAddress= driver.find_element_by_id("currentAddress")
    currentAddress.send_keys("Brown street 12, apartment 5")
    driver.implicitly_wait(2)

    permanentAddress=driver.find_element_by_id("permanentAddress")
    permanentAddress.send_keys("Oxford street 45")
    driver.implicitly_wait(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element_by_id("submit").click()

OpenDemo()