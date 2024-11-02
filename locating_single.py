from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
qury="leptop"
driver.get(f"https://www.amazon.in/s?k={qury}&crid=2U44J85V9C94J&sprefix=lep%2Caps%2C757&ref=nb_sb_ss_ts-doa-p_2_3")
elem=driver.find_element(By.CLASS_NAME,"puis-card-container")
print(elem.text)
time.sleep(4)
driver.close()