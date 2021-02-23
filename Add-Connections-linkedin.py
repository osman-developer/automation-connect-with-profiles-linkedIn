from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
import time
browser = webdriver.Chrome()

#navigation
browser.maximize_window()
browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

firstname = browser.find_element_by_id("username")
firstname.send_keys('example@example.com')

firstname = browser.find_element_by_id("password")
firstname.send_keys('yourPassword')

wait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//main/div[2]/form/div[3]/button"))).click()

browser.get('https://www.linkedin.com/mynetwork/')
time.sleep(15)
for i in range(100):
	wait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Connect']"))).click()
	time.sleep(1)