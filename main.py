from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By




chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://elgoog.im/t-rex/")


# Wait until the page is loaded 
time.sleep(3)

random_element=driver.find_element(by=By.NAME,'div')




