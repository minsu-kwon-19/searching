from pickle import FALSE
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests
import json
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

import subprocess
import pyautogui
import socks
from stem import Signal
from stem.control import Controller
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import tbselenium.common as cm
from tbselenium.tbdriver import TorBrowserDriver
from tbselenium.utils import launch_tbb_tor_with_stem
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

import random




#    Get Response.
#
def getRes(url, headers):
    res = requests.get(url, headers = headers)
    time.sleep(3)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
        
    return res

def keyDownEnd():
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

def keyDownPageDown():
    time.sleep(1)
    pyautogui.press('pagedown')
    time.sleep(1)
    pyautogui.press('pagedown')
    time.sleep(1)
    pyautogui.press('pagedown')
    time.sleep(1)
    pyautogui.press('pagedown')
    time.sleep(1)
    pyautogui.press('pagedown')
    time.sleep(1)

def keyDownPageUp():
    time.sleep(1)
    pyautogui.press('pageup')
    time.sleep(1)
    pyautogui.press('pageup')
    time.sleep(1)
    pyautogui.press('pageup')
    time.sleep(1)
    pyautogui.press('pageup')
    time.sleep(1)
    pyautogui.press('pageup')
    time.sleep(1)    


def SearchKeyword(keyword, LinkText):

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

    userAgent = user_agent_rotator.get_random_user_agent()

    options.add_argument(f'user-agent={userAgent}')
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

    driver.switch_to.window(driver.window_handles[1])


    for cnt in range(1, 10):
        # 화면 내리기 end 키로.
        keyDownEnd()

        try:
            naseong = driver.find_element(By.LINK_TEXT, LinkText)
            naseong.click()
        except selenium.common.exceptions.NoSuchElementException as ex:
            if cnt == 9:
                print(f"제목이 없음 : {LinkText}")
                break
            
            # next page
            naseong = driver.find_element(By.XPATH, f'//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/div[3]/div/a[{cnt}]')
            naseong.click()
            time.sleep(1)
            continue

        keyDownPageDown()

        time.sleep(30)

        pyautogui.press('home')

        time.sleep(3)

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

    cnt = 0
    for val in range(0, 10):
        cnt += 1
        filePath = './searchInfo.json'  # json 파일.
        Array = getJsonInfo(filePath)
        print(f"count : {cnt}")
        time.sleep(2)

        for keywordInfo in Array:
            #print(f"{keywordInfo['키워드']}, {keywordInfo['제목']}")
            SearchKeyword(keywordInfo['키워드'], keywordInfo['제목'])
        time.sleep(random.randrange(50, 70))