from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://drivetest.ca/book-a-road-test/booking.html#/validate-driver-email")

url = driver.command_executor._url      
session_id = driver.session_id   

email = driver.find_element_by_name("email")
email.send_keys("priyanshubhatt1377@gmail.com")
email.send_keys(Keys.TAB)

email = driver.find_element_by_name("email")
email.send_keys("priyanshubhatt1377@gmail.com")
email.send_keys(Keys.TAB)

licNum = driver.find_element_by_name("licenceNumber")
licNum.send_keys("-------------")
licNum.send_keys(Keys.TAB)

expDate = driver.find_element_by_id("licenceExpiryDate")
expDate.send_keys("-------------")
expDate.send_keys(Keys.TAB)

button = driver.find_element_by_id("regSubmitBtn")
button.click()

driver.__exit__()
