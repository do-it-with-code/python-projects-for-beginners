from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from creds import *
import time

driver = webdriver.Chrome()
driver.get("https://instagram.com/accounts/login")
time.sleep( 3 )

username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
username.send_keys( username )
password.send_keys( password )

button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')
button.click()

wait = input("Press y to continue.. ")
if wait != 'y':
    exit("Exiting..")
    driver.quit()

driver.get('https://www.instagram.com/hacking.tech/')
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
time.sleep( 10 )

count = 0
last_button = driver.find_elements_by_xpath("//button[contains(text(),'Follow')]")[-1]
while count < 20:
    followers = driver.find_elements_by_xpath("//button[text()='Follow']")
    for i in followers:
        i.click()
        time.sleep( 10 )
        print( count )
        count += 1
    last_button.send_keys(Keys.PAGE_DOWN)

driver.quit()
