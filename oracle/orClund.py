# orClund.py
import os
import time
from datetime import date
from PIL import ImageGrab
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
edge_driver_path = os.path.join(os.getcwd(), 'msedgedriver.exe')
edge_options = Options()
# edge_options.add_argument("--headless")

edge_options.add_argument(f'user-agent={user_agent}')

browser = webdriver.Edge(service=Service(edge_driver_path), options=edge_options)
browser.set_window_position(0, 0)
browser.set_window_size(1440, 900)

#Capture Desktop ,Browser
screenshot = ImageGrab.grab()

# หน้าหลักในการเข้าถึง
url = "https://www.oracle.com/cloud/sign-in.html?redirect_uri=https%3A%2F%2Fcloud.oracle.com%2F"

# OrlCloud
urldashboard = "https://oms1:7799/em/jetp/dashboards/index.html"

# 
urlOrClund = "https://cloud.oracle.com/compute/instances?region=ap-singapore-1"

surename = "mtisoci"
username = "vongvaris@mfec.co.th"
password = "0994541525Att!"

def OrlCloudDoing():
    try:
        browser.get(url)
        user_input = WebDriverWait(browser, 3000).until(
            EC.presence_of_element_located((By.ID, "cloudAccountName"))
        )        
        user_input.send_keys(surename)
        print('ใส่ชื่อ') 
        # next
        nextbtn = WebDriverWait(browser, 3000).until(
            EC.presence_of_element_located((By.ID, "cloudAccountButton"))
        )        
        nextbtn.click()
        print('go to login') 
        # 
        time.sleep(15) 
        # 
        print('login')         
        username_input = WebDriverWait(browser, 3000).until(
            EC.presence_of_element_located((By.ID, "idcs-signin-basic-signin-form-username"))
        )        
        username_input.send_keys(username)
        print('ใส่ user')
        password_input = WebDriverWait(browser, 3000).until(
            EC.presence_of_element_located((By.ID, "idcs-signin-basic-signin-form-password|input"))
        )        
        password_input.send_keys(password)
        print('ใส่ password')
        login_button = browser.find_element(By.ID, "idcs-signin-basic-signin-form-submit")
        login_button.click()
        print('login')
        # 
        time.sleep(20) #Authen
        browser.get(urlOrClund)
        print('เข้ามาแล้ว')
        time.sleep(5)
        # 
        print('กำลังหาช่อง')
        # Dropdown = WebDriverWait(browser, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[@class='node-label' and text()='Finastra_DC']"))
        # )
        # Dropdown.click()
        # print('เลือกDropDown')        
        # element = WebDriverWait(browser, 60).until(
        #     EC.presence_of_element_located((By.XPATH, "//input[@class='search' and @placeholder='Choose a compartment']"))
        # )
        # element.click()
        # ทำให้โปรแกรมค้างที่นี่
        while True:
            pass
        
    except:
        print('ล้มเหลว')
        
OrlCloudDoing()      

