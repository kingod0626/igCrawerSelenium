from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import wget

accountLogin = input('輸入你的ig帳號:')
passwordLogin = input('輸入你的ig密碼:')



PATH="D:/code/workplace/igCrawerSele/chromedriver.exe"
driver = webdriver.Chrome(PATH)
cookies = driver.get_cookies()
print(f"main: cookies = {cookies}")
driver.delete_all_cookies()

driver.get("https://www.instagram.com/")


username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
)
password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
)

login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')

time.sleep(5)

username.clear()
password.clear()
username.send_keys(accountLogin)
password.send_keys(passwordLogin)
login.click()
datasave = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/section/div/button'))
)
datasave.click()
announcecancel = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]'))
)
announcecancel.click()
search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
keyword= "#濱邊美波"
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(5)

imgs = driver.find_elements_by_class_name("FFVAD")

path = os.path.join(keyword)
os.mkdir(path)

count = 0 
for img in imgs:
        save_as = os.path.join(path,keyword + str(count)+'.jpg')
        print(img.get_attribute("src"))
        wget.download(img.get_attribute("src"), save_as)
        count += 1
