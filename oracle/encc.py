# encc.py
import os
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://oms1:7799/em/faces/logon/core-uifwk-console-login"
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
edge_driver_path = os.path.join(os.getcwd(), 'msedgedriver.exe')
edge_options = Options()
edge_options.add_argument(f'user-agent={user_agent}')
browser = webdriver.Edge(service=Service(edge_driver_path), options=edge_options)
urldashboard = "https://oms1:7799/em/jetp/dashboards/index.html"
username = "aasupport"
password = "Pa55w.rd123!"


def EnccDoing():
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
            EC.presence_of_element_located((By.ID, "j_username::content"))
        )        
        username_input.send_keys(username)
        print('ใส่ชื่อ') 
        
        password_input = WebDriverWait(browser, 3000).until(
            EC.presence_of_element_located((By.ID, "j_password::content"))
        )        
        password_input.send_keys(password)
        print('ใส่ password') 
        
        login_button = browser.find_element(By.ID, "login")
        login_button.click()
        print('รอเข้าสู่ login') 
        
        # WebDriverWait(browser, 60).until(
        #     EC.url_contains("expected_part_of_url")
        #     # หรือ
        #     # EC.url_to_be("expected_full_url")
        # )
        print('login Success ->> goDashboard') 
        Godashboard()
        
    except:
        print('ล้มเหลว')
        
def Godashboard():
    browser.get(urldashboard)
    browser.save_screenshot("screenshot.png")
        
    
# EnccDoing() #Step Login



 
    
    





