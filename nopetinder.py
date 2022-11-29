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

url = "https://tinder.com"

img_xpath = '//*[@id="q798806120"]/div/div[1]/div/main/div[1]/div/div/div/div/div[1]/div[1]/div/div[3]/div[1]/div[1]/span[1]'
img_element = '<div aria-label="Lauren" role="img" class="Bdrs(8px) Bgz(cv) Bgp(c) StretchedBox" style="background-image: url(&quot;https://images-ssl.gotinder.com/u/cdQEoW3pKrEU4q668Jbf39/gRsHK9Jhf5isJ6eET5nrkm.webp?Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6IiovdS9jZFFFb1czcEtyRVU0cTY2OEpiZjM5LyoiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE2NzAwMDUwMDZ9fX1dfQ__&amp;Signature=ylU7Nl4VdFpeh1tkVMUsijyh5r2rOTNBMuHoM3yNknK3-vIwscXll699rFGElrmfaIfrrjH~NHL8trXCyIuGZKED2EebDxWQkzgDVUsDn084Eitvr2DNZHV3K~YyLi-eYdO8cv0VIB62VBeqZstOMR9wtzKBwWIuhqncI1Xy00YUT11MOZ2j25gdSsChuJNDuM3tcrhD9Wg~H6mzHZXbQntggspQTy0vo8xU3giKtidsvguQjx~R3ZNm4ud7FxYcJpDzCsFLM9gubhyXsKD4CzNDyRnQHlSoY5DKjbKrxberRwr~f70cJRorCoSZFJLAyrBjw6CfyfQAr6GrGlAk~g__&amp;Key-Pair-Id=K368TLDEUPA6OI&quot;); background-position: 50% 0%; background-size: 120.755%;"></div>'

nope_xpath = '//*[@id="q798806120"]/div/div[1]/div/main/div[1]/div/div/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button'
like_xpath = '//*[@id="q798806120"]/div/div[1]/div/main/div[1]/div/div/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button'
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=chrome_options)
driver.get(url)
time.sleep(10)

def getRekognitionScore():
    pass

def getPic():
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

def like_or_pass():
    time.sleep(10)
    # integrate keyboard to detect button press
    keyboard.on_press_key("left arrow", lambda _: print('mkay'))
    keyboard.on_press_key("right arrow", lambda _: getPic())
    while True:
        continue



while(True):
    pass