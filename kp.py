from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import configparser
import os, os.path
import docx

# slikeDir = os.getcwd() 


	
def getDescription(file):
	doc = docx.Document(file)
	fullText = []
	for para in doc.paragraphs:
		fullText.append(para.text)
	return '\n'.join(fullText)

description = getDescription(os.getcwd()+'\\description.docx')

config = configparser.ConfigParser()
try:
	config.read("config.ini")
	config.read('xpath.ini')
except UnicodeDecodeError:
	print("Koristili ste č,ć,đ,š ili ž. Promenite pa pokušajte ponovo")
	quit()

brojOglasa = config['user']['brojOglasa']
email = config['user']['email']
passwd = config['user']['password']
ime = config['user']['name']
brTelefona = config['user']['phoneNumber']

naslov = config['data']['title']
kategorija = config['data']['kategorija']
kategorijaXPATH = config['kategorija'][kategorija]
grupa = config['data']['grupa']
stanje = config['data']['stanje']
stanjeId = config['stanje'][stanje]
deskripcija = config['data']['description']
cena = config['data']['cena']
fiksno = config['data']['fiksno']
valuta = config['data']['valuta']
valutaID = config['valuta'][valuta]

print(brojOglasa)
PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.kupujemprodajem.com/")


link = driver.find_element(By.XPATH,'//*[@id="bodyTag"]/div[9]/div/div[1]/div[2]/div/div/div/div[4]/div/span')
link.click()

time.sleep(3)

imejl = driver.find_element(By.ID,"email")
imejl.send_keys(email)

sifra = driver.find_element(By.ID,"password")
sifra.send_keys(passwd)

button = driver.find_element(By.ID,"submitButton")
button.click()

time.sleep(3) #ulogovan
# try: // nece trenutno
# 	postaviteOglas = driver.find_element(By.XPATH,'//*[@id="leftNav"]/div[2]/a')
# 	postaviteOglas.click()
# except NoSuchElementException:
# 	quit()

for i in range(1,int(brojOglasa)+1):
	config.read(f"artikal{i}.ini")

	naslov = config['data']['title']
	kategorija = config['data']['kategorija']
	kategorijaXPATH = config['kategorija'][kategorija]
	grupa = config['data']['grupa']
	stanje = config['data']['stanje']
	stanjeId = config['stanje'][stanje]
	deskripcija = config['data']['description']
	cena = config['data']['cena']
	fiksno = config['data']['fiksno']
	valuta = config['data']['valuta']
	valutaID = config['valuta'][valuta]

	brSlika = len(os.listdir(os.getcwd()+f'\\artikal{i}_slike'))

	driver.get("https://www.kupujemprodajem.com/oglasi.php?action=new")
	time.sleep(3)
	try:
		naslovOglasa = driver.find_element(By.ID,'data[group_suggest_text]')
		naslovOglasa.send_keys(naslov)
	except NoSuchElementException:
		quit()

	# time.sleep(3)

	try:
		btnKategorija = driver.find_element(By.XPATH,'//*[@id="categorySelection"]/div/div[1]/div/span[3]')
		btnKategorija.click()
	except NoSuchElementException:
		quit()

	# time.sleep(3)

	try:
		kategorijaMeni = driver.find_element(By.XPATH,kategorijaXPATH)
		kategorijaMeni.click()
	except:
		quit()

	time.sleep(3)

	# grupa = driver.find_element_by_xpath('//*[@id="groupSelection"]/div/div[1]/div/span[3]')
	# grupa.click()

	# time.sleep(5)

	# find element by clicking
	# grupaMeni = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/form/div[5]/div/div/div[1]/div[3]/div/div[4]/div[2]/div[1]/span/div/div/div[2]/div/div[3]/div[3]/div[1]')
	# grupaMeni.click()

	#find element by text input
	# grupa = driver.find_element(By.XPATH,'//*[@id="groupSelection"]/div/div[2]/div/div[2]/input')
	# grupa.send_keys('Horor')
	# time.sleep(2)
	# pyautogui.press('enter')

	try:
		btnGrupa = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="groupSelection"]/div/div[2]/div/div[2]/input')))
		btnGrupa.send_keys(grupa)
		time.sleep(4)
		pyautogui.press('enter')
	except NoSuchElementException:
		quit()

	time.sleep(3)
	try:
		stanje = driver.find_element(By.ID,stanjeId)
		stanje.click()
	except:
		pass

	# naslovOglasa = driver.find_element_by_id('data[name]')
	# naslovOglasa.clear()
	# naslovOglasa.send_keys("Promena")

	try:
		txtCena = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,'data[price]')))
		txtCena.send_keys(cena)
	except NoSuchElementException:
		quit()

	if fiksno == 'da':
		try:
			chkFiksno = driver.find_element(By.ID,"data[price_fixed]")
			chkFiksno.click()
		except NoSuchElementException:
			quit()

	try:
		rbtnValuta = driver.find_element(By.ID,valutaID)
		rbtnValuta.click()
	except NoSuchElementException:
		quit()

	try:
		frame = driver.find_element(By.ID,'data[description]_ifr')
		driver.switch_to.frame(frame)
		tekst = driver.find_element(By.ID,'tinymce')
		tekst.send_keys(description)
	except NoSuchElementException:
		quit()

	driver.switch_to.default_content()
	# driver.execute_script("window.scrollTo(0, 100)") 
	try:
		slika = driver.find_element(By.XPATH,'//*[@id="addPhotoButtonInList"]/div')
		for x in range(brSlika):

			slika.click()
			time.sleep(3)
			pyautogui.write(os.getcwd()+'\\artikal{}_slike\\{}.jpg'.format(i,x+1))
			pyautogui.press('enter')
	except NoSuchElementException:
		quit()

	try:
		txtIme = driver.find_element(By.ID,'data[owner]')
		txtIme.clear()
		txtIme.send_keys(ime)
	except NoSuchElementException:
		quit()

	try:
		txtBrTelefona = driver.find_element(By.ID,'phone_number')
		txtBrTelefona.clear()
		txtBrTelefona.send_keys(brTelefona)
	except NoSuchElementException:
		quit()

	time.sleep(40*brSlika)
	try:
		btnSledece = driver.find_element(By.XPATH,'//*[@id="adFormInfo"]/div[2]/div[21]/div/input')
		btnSledece.click()
	except NoSuchElementException:
		quit()

	time.sleep(3)

	try:
		chkVidljivost = driver.find_element(By.XPATH,'//*[@id="service-holder-none"]/div[3]/div/div[1]')
		chkVidljivost.click()
	except NoSuchElementException:
		quit()

	try:
		btnSledece = driver.find_element(By.XPATH,'//*[@id="adFormPromo"]/div[4]/div/input')
		btnSledece.click()
	except NoSuchElementException:
		quit()

	time.sleep(3)

	try:
		chkPravila = driver.find_element(By.ID,'accept_yes')
		chkPravila.click()
	except NoSuchElementException:
		quit()

	try:
		btnPostaviteOglas = driver.find_element(By.XPATH,'//*[@id="adFormDeclaration"]/div[8]/div/input')
		btnPostaviteOglas.click()
	except NoSuchElementException:
		quit()