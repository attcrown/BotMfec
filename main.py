import os
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# กำหนด URL ของเว็บไซต์
url = "https://know-are-learning.web.app/login"

# กำหนด User Agent
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'

# กำหนดตำแหน่งของ msedgedriver.exe
edge_driver_path = os.path.join(os.getcwd(), 'msedgedriver.exe')

# กำหนด options
edge_options = Options()
edge_options.add_argument(f'user-agent={user_agent}')

# เรียกใช้ webdriver
browser = webdriver.Edge(service=Service(edge_driver_path), options=edge_options)

# เปิดเว็บไซต์
browser.get(url)

# ใส่ชื่อผู้ใช้และรหัสผ่าน
username = "Admin123"
password = "admin123"

# รอให้ Element ปรากฏขึ้น
username_input = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "input-12"))
)

# ใส่ข้อมูลลงในช่อง input ที่ใช้ใส่ชื่อผู้ใช้
username_input.send_keys(username)

# รอให้ Element ปรากฏขึ้น
password_input = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "input-15"))
)

# ใส่ข้อมูลลงในช่อง input ที่ใช้ใส่รหัสผ่าน
password_input.send_keys(password)

# หากคุณทราบ id ของปุ่ม login ให้ค้นหาด้วย By.XPATH หรือ By.CSS_SELECTOR แทน By.TYPE
login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

menu = WebDriverWait(browser, 20).until(
    EC.presence_of_element_located((By.XPATH, "//button[@type='button']"))
)
# เปิดเมนูด้านข้าง
menu.click()

# เปิดเมนู Salary เงินเดือน
menu_salary = WebDriverWait(browser, 20).until(
    EC.presence_of_element_located((By.XPATH, "//a[@href='/admin/salary']"))
)
menu_salary.click()

search_tea = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "input-149"))
)
search_tea.send_keys('FS1234')

selectName = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "list-item-181-0"))
)
selectName.click()

time.sleep(2)

browser.quit()




