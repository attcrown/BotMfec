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
screenshot = ImageGrab.grab()

url = "http://maxar-debtapp.ana.local:8080/login?redirect=%2Fhome"

def maxza2Doing():
    try:
        browser.get(url)
        WebDriverWait(browser, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img[data-v-26084dc2]')))
        current_date = date.today()
        browser.save_screenshot(f"Pagemaxza_maxar-debtapp_{current_date}.png")
        print('Capture Maxza2 Success')
        browser.quit()
    except:
        print('An exception occurred')
        
# maxza2Doing()