from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

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

postaviteOglas = driver.find_element_by_xpath('//*[@id="leftNav"]/div[2]/a')
postaviteOglas.click()

naslovOglasa = driver.find_element_by_id('data[group_suggest_text]')
naslovOglasa.send_keys("Stephen King IT Knjiga")

# time.sleep(3)

kategorija = driver.find_element_by_xpath('//*[@id="categorySelection"]/div/div[1]/div/span[3]')
kategorija.click()

# time.sleep(3)

kategorijaMeni = driver.find_element_by_xpath('//*[@id="menuGroup0"]/div[22]')
kategorijaMeni.click()

time.sleep(3)

# grupa = driver.find_element_by_xpath('//*[@id="groupSelection"]/div/div[1]/div/span[3]')
# grupa.click()

# time.sleep(5)

grupaMeni = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/form/div[5]/div/div/div[1]/div[3]/div/div[4]/div[2]/div[1]/span/div/div/div[2]/div/div[3]/div[3]/div[1]')
grupaMeni.click()

time.sleep(3)

korisceno = driver.find_element_by_xpath('//*[@id="conditionForm"]/div[2]/div[1]/label[2]')
korisceno.click()

# naslovOglasa = driver.find_element_by_id('data[name]')
# naslovOglasa.clear()
# naslovOglasa.send_keys("Promena")

cena = driver.find_element_by_name('data[price]')
cena.send_keys('1000')

valuta = driver.find_element_by_xpath('//*[@id="data[currency]"]/label[1]')
valuta.click()

frame = driver.find_element_by_id('data[description]_ifr')
driver.switch_to.frame(frame)
tekst = driver.find_element(By.ID,'tinymce')
tekst.send_keys("Stephen King IT - stanje odlicno")

driver.switch_to.default_content()
# driver.execute_script("window.scrollTo(0, 100)") 

slika = driver.find_element(By.XPATH,'//*[@id="addPhotoButtonInList"]/div')
slika.click()
time.sleep(3)
pyautogui.write('C:\\Users\\bole\\OneDrive\\Desktop\\slika.jpg')
pyautogui.press('enter')

ime = driver.find_element(By.ID,'data[owner]')
ime.clear()
ime.send_keys('Neša')

telefon = driver.find_element_by_id('phone_number')
telefon.send_keys('0641234567')

time.sleep(60)

btnSledece = driver.find_element_by_xpath('//*[@id="adFormInfo"]/div[2]/div[21]/div/input')
btnSledece.click()

time.sleep(3)

chkVidljivost = driver.find_element_by_xpath('//*[@id="service-holder-none"]/div[3]/div/div[1]')
chkVidljivost.click()

btnSledece = driver.find_element_by_xpath('//*[@id="adFormPromo"]/div[4]/div/input')
btnSledece.click()

time.sleep(3)
chkPravila = driver.find_element_by_id('accept_yes')
chkPravila.click()

btnPostaviteOglas = driver.find_element_by_xpath('//*[@id="adFormDeclaration"]/div[8]/div/input')
btnPostaviteOglas.click()