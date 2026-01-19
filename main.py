from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from PIL import Image
import pyautogui




chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://elgoog.im/t-rex/")


# Wait until the page is loaded 
time.sleep(1)

random_element=driver.find_element(By.TAG_NAME,"body")


# Start the game 
time.sleep(1)
random_element.send_keys(Keys.SPACE)

time.sleep(3)



while True:
    screenshot = pyautogui.screenshot()
    region = screenshot.crop((250, 1200,600, 1400))
    gray = region.convert("L")
    pixels = gray.load()

    obstacle = False
    for x in range(gray.width):
        for y in range(gray.height):
            if pixels[x, y] < 150:
                obstacle = True
                break
        if obstacle:
            break

    if obstacle:
        
        random_element.send_keys(Keys.UP)

    time.sleep(0.01)

