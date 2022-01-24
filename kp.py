from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.kupujemprodajem.com/")

link = driver.find_element_by_xpath('//*[@id="bodyTag"]/div[9]/div/div[1]/div[2]/div/div/div/div[4]/div/span')
link.click()

time.sleep(3)

email = driver.find_element_by_id("email")
email.send_keys("magiicall8@gmail.com")

passwd = driver.find_element_by_id("password")
passwd.send_keys("b14.....b43,,,")

button = driver.find_element_by_id("submitButton")
button.click()

time.sleep(3)

# postaviteOglas = driver.find_element_by_xpath('//*[@id="leftNav"]/div[2]/a')
# postaviteOglas.click()

# naslovOglasa = driver.find_element_by_id('data[group_suggest_text]')