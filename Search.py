from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests
import json
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains

import pyautogui

#
#    Get Response.
#
def getRes(url, headers):
    res = requests.get(url, headers = headers)
    time.sleep(1)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
        
    return res


def SearchKeyword(keyword, LinkText):

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.w3c = True
    driver = webdriver.Chrome(options=options)

    # search url
    url = 'https://naver.com'

    driver.get(url) # Open Url.
    driver.maximize_window() # maximize window.
    action= ActionChains(driver)

    driver.get(f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={keyword}")
    time.sleep(1)

    element = driver.find_element(By.CLASS_NAME, "api_more._link")
    tmp = element.click()
    time.sleep(1)

    print(f"handles : {driver.window_handles}")
    driver.switch_to.window(driver.window_handles[1])


    for cnt in range(1, 10):
        # 화면 내리기 end 키로.
        time.sleep(1)
        pyautogui.press('end')
        time.sleep(1)
        pyautogui.press('end')
        time.sleep(1)
        pyautogui.press('end')
        time.sleep(1)
        pyautogui.press('end')
        time.sleep(1)
        pyautogui.press('end')
        time.sleep(1)

        # 나성유통 타포린백
        try:
            naseong = driver.find_element(By.LINK_TEXT, LinkText)
            naseong.click()
        except selenium.common.exceptions.NoSuchElementException as ex:
            # next page
            naseong = driver.find_element(By.XPATH, f'//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/div[3]/div/a[{cnt}]')
            naseong.click()
            time.sleep(1)
            continue

        time.sleep(20)

        # Close chrome.
        driver.quit()
        time.sleep(1)
        break

def getJsonInfo(filePath):
    with open(filePath, 'r', encoding="UTF-8") as file:
        data = json.load(file)
        array = data['검색명']
        return array

if __name__ == "__main__":
    
    for val in range(0, 70):
        filePath = './searchInfo.json'  # json 파일.
        Array = getJsonInfo(filePath)
        time.sleep(1)

        for keywordInfo in Array:
            SearchKeyword(keywordInfo['키워드'], keywordInfo['제목'])
        time.sleep(60)

