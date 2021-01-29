from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe" #path for the chromedriver.
driver = webdriver.Chrome(PATH)

time.sleep(5)
input("Press enter to start!")
userName = input("Enter the user's name(Must enter emojis if present): ")
msg = input("Enter the msg you want to send to the user: ")
count = int(input("Enter the number of msgs you want to send(Must be a number!): "))
input("Now press enter key and scan the qr code.")

driver.get("https://web.whatsapp.com/")  #opens site on the browser

time.sleep(15)

span = "span[title = '%s']" %(userName)

#points to the user's chat and clicks on it
userChat = driver.find_element_by_css_selector(span)
userChat.click()

#points to the chat's textfield and clicks on it
textfield = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
textfield.click()

#Sends the msg for the specified number of times.
for i in range(count):
    textfield.send_keys(msg,i)
    textfield.send_keys(Keys.RETURN)

driver.quit()