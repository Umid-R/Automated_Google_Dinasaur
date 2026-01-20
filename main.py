from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from PIL import ImageGrab
import numpy as np




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





def get_image():
    region = ImageGrab.grab(bbox=(110, 630,313,695))
    return region

def detect_mode():
    

    # Grab a tiny background area (adjust if needed)
    img = ImageGrab.grab(bbox=(110, 700,306,710))  
    gray = np.array(img.convert("L"))  

    avg_brightness = gray.mean()

    if avg_brightness < 100:
        return "dark"
    else:
        return  "light"
    

def detect_obstacle(image, mode):
    gray = image.convert("L")
    pixels = gray.load()
    y = gray.height // 2
    obstacle = False
    if mode=='light':
        for x in range(gray.width):
            if pixels[x, y] < 100:
                obstacle = True
                break
    else:
        for x in range(gray.width):
            if pixels[x, y] > 150:  
                obstacle = True
                break
        
            
    return obstacle
    




while True:
    image=get_image()
    mode=detect_mode()
    if detect_obstacle(image,mode):
        random_element.send_keys(Keys.SPACE)
    
    
    
    
    
