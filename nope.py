#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://bumble.com/"

continue_xpath = '//*[@id="notice"]/div[2]/div[2]/div/button'
sign_in_xpath = '//*[@id="page"]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a'
use_pho_num_xpath = '//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[3]/div/span/span/span'
img_xpath = '//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[1]/article/div[1]/div[1]/article/div[1]/div/figure/picture/img'
like_xpath = '//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span'
pass_xpath = '//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div/div[1]/span'
pass_jspath = "document.querySelector(\"#main > div > div.page__layout > main > div.page__content-inner > div > div > span > div.encounters-user__controls > div > div:nth-child(2) > div > div:nth-child(2) > div > div.encounters-action__icon > span\")"

chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path='chromedriver.exe' , chrome_options=chrome_options)
driver.get(url)
try:
    actions = ActionChains(driver)
    for _ in range(5):
        actions = actions.send_keys(Keys.TAB)
    actions = actions.send_keys(Keys.ENTER)
    actions.perform()
except:
    print('No privacy alert found.')
time.sleep(5)
driver.find_element(By.XPATH, sign_in_xpath).click()
driver.implicitly_wait(15)
driver.find_element(By.XPATH, use_pho_num_xpath).click()
actions = ActionChains(driver)
actions = actions.send_keys('4042175250')
actions = actions.send_keys(Keys.ENTER)
actions.perform()

yessir = driver.find_element(By.XPATH, like_xpath).is_selected()
nossir = driver.find_element(By.XPATH, pass_xpath).is_selected()

def getRekognitionScore():
    pass

def like_or_pass(driver):
    time.sleep(10)
    # integrate js to detect button press
    js = "var clicked = false \
         document.getElementById("+ pass_jspath +"}).addEventListener(\"click\", function() { \
         clicked = true \
         });"
    js1 = "var x = document.getElementById("+ pass_jspath +"); \
         x.addEventListener(\"click\", function() { \
         alert(\"You clicked me\"); \
         })"
    x = driver.execute_script(js1)
    print('x: ', x)
    return x
time.sleep(5)
decision = like_or_pass(driver)

def getPic():
    #like_or_pass(driver)
    #open file in write and binary mode
    with open('profile_pic.png', 'wb') as file:
    #identify image to be captured
        time.sleep(10)
        l = driver.find_element(By.XPATH, img_xpath)
        '''
        2 next lines will be useful w/ HTTP
        x = l.get_attribute('src')
        print('X: ', str(x))
        '''
        #write file
        file.write(l.screenshot_as_png)
        time.sleep(5)
        if getRekognitionScore() == 1:
            #append dataset with a 1
            print('like')
        else:
            #append dataset with a 0
            print('pass')
        #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Next'))).click()

getPic()

while(True):
    pass