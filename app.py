from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

URL = 'https://nipagpu.managed.co.kr/NIPA/AIArchvs/public'


try:
    browser.get(URL)
    time.sleep(10)
    vsp = input("인증 코드를 입력하세요 : ")
    browser.find_element(By.ID, 'captchaAnwser').send_keys(int(vsp))    

except:
    pass

finally:
    # browser.quit()
    while True:
        break