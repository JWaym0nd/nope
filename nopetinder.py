#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import keyboard
import time
import image_loader
import get_Pic
import os

url = "https://tinder.onelink.me/9K8a/3d4abb81"

#img_xpath = '//*[@id="q798806120"]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div[1]/div[1]/span[1]/div'
# img_xpath = '//*[@id="q798806120"]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div[1]/div[1]/span[1]'
#img_xpath = '/html/body/div[1]/div/div[1]/div/div/main/div/div/div[1]/div/div[2]/div[1]/div[1]/span[1]/div'
img_linktext = 'Nope'

nope_xpath = '//*[@id="q798806120"]/div/div[1]/div/main/div[1]/div/div/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button'
like_xpath = '//*[@id="q798806120"]/div/div[1]/div/main/div[1]/div/div/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button'
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
dir_path = os.getcwd()
chrome_options.add_argument(f'user-data-dir={dir_path}/selenium')
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=chrome_options)
driver.get(url)
cookies = driver.get_cookies()
driver.add_cookie(cookies)
#time.sleep(10)

def like_or_pass():
    print('likeorpass')
    # integrate keyboard to detect button press
    keyboard.on_press_key("left arrow", lambda _: print('mkay'))
    keyboard.on_press_key("right arrow", lambda _: image_loader.upload_file())
    while True:
        continue
get_Pic.get_Pic(driver, img_linktext)
like_or_pass()

while(True):
    pass