from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import keyboard
import time

class get_Pic:
    def __init__(self, driver, element) -> None:
        self.driver = driver
        self.element = element

        #open file in write and binary mode
        with open('profile_pic.png', 'wb') as file:
        #identify image to be captured
            time.sleep(30)
            self.driver.save_screenshot('shot.png')
            l = self.driver.find_element(By.LINK_TEXT, self.element)
            #poo = self.driver.find_element(By.LINK_TEXT, self.element)
            '''
            2 next lines will be useful w/ HTTP
            x = l.get_attribute('src')
            print('X: ', str(x))
            '''
            #write file
            file.write(l.screenshot_as_png)
            time.sleep(5)

if __name__ == "__main__":
    get_Pic()