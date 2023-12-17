#Solarwind
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

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
edge_driver_path = os.path.join(os.getcwd(), 'msedgedriver.exe')
edge_options = Options()
edge_options.add_argument(f'user-agent={user_agent}')
browser = webdriver.Edge(service=Service(edge_driver_path), options=edge_options)
browser.set_window_position(0, 0)
browser.set_window_size(1440, 900)

url = "https://202.80.231.19/Orion/Login.aspx"
username = "aasupport"
password = "Pa55w.rd123!"

def SolarwindDoing():
    try:
        browser.get(url)
        print('login') 
        Scel = WebDriverWait(browser, 3000).until(
            EC.presence_of_element_located((By.ID, "details-button"))
        )        
        Scel.click()
        print('detail')
        
        LinkUrl = WebDriverWait(browser, 3000).until(
            EC.presence_of_element_located((By.ID, "proceed-link"))
        )        
        LinkUrl.click()
        print('go to link detail')
        
        username_input = WebDriverWait(browser, 3000).until(
            EC.presence_of_element_located((By.ID, "ctl00_BodyContent_Username"))
        )        
        username_input.send_keys(username)
        print('ใส่ชื่อ') 
        password_input = WebDriverWait(browser, 3000).until(
            EC.presence_of_element_located((By.ID, "ctl00_BodyContent_Password"))
        )        
        password_input.send_keys(password)
        print('ใส่ password') 
        login_button = browser.find_element(By.ID, "ctl00_BodyContent_LoginButton")
        login_button.click()
        print('รอเข้าสู่ login') 
        
        print('login Success ->> goDashboard')
        time.sleep(10)
        current_date = date.today()
        browser.save_screenshot(f"DashSolar{current_date}.png")
        print('Capture Solarwind Success')
        
        # CheckCWTower
        CheckTW()
    
    except:
        print('ล้มเหลว')
        
def CheckTW():
    main_dashboard_element = WebDriverWait(browser, 60).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='/Orion/NetPerfMon/NodeDetails.aspx?NetObject=N:18']"))
    )
    main_dashboard_element.click()
    # รอ Element ปรากฏ
    element = WebDriverWait(browser, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, "NetObjectLink"))
    )
    # ตรวจสอบข้อความใน Element
    if "Node is Critical." in element.text:
        element.click()
    else :
        element.click()
        time.sleep(10)
        current_date = date.today()
        browser.save_screenshot(f"Alert_CWTower02{current_date}.png")
        
        element = WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.XPATH, "//td[@class='PropertyHeader' and text()='Description']"))
        )
        browser.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(4)
        browser.save_screenshot(f"Alert_CWTower02{current_date}_2.png")

        
# SolarwindDoing()