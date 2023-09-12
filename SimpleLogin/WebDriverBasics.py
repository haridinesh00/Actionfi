import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get("https://www.google.com")
# Navigate to url
driver.get("https://ops07.lower.trintech.com")
#print(driver.title)
# Click on the element
driver.implicitly_wait(5)  # Waits 5 seconds to find the sign in button,
# if not found in 5 seconds, a timeout error occurs.

username = driver.find_element(By.NAME, "UserName")
username.clear()
username.send_keys("sa")
password = driver.find_element(By.NAME, "Password")
password.clear()
password.send_keys("Trintech1!")
submit = driver.find_element(By.CLASS_NAME, "loginButton")

submit.click()

time.sleep(10)
# Wait for a few seconds to see the result (you can adjust this time)
driver.implicitly_wait(10)

certification = driver.find_element(By.LINK_TEXT, "Certification")
certification.click()
time.sleep(5)
driver.implicitly_wait(5)
side_bar_toggle = driver.find_element(By.CLASS_NAME, "btn-sidebar-toggle")
side_bar_toggle.click()
time.sleep(5)
driver.implicitly_wait(5)

recon = driver.find_element(By.LINK_TEXT, "Reconciliations")
recon.click()
recon_due = driver.find_element(By.LINK_TEXT, "Reconciliations Due")
recon_due.click()
time.sleep(5)
filters = driver.find_element(By.ID, "imgFilter")
filters.click()
time.sleep(5)
cc = driver.find_element(By.ID, "ctl00_MainContent_ucAccFilter_accountSegmentsDataList_ctl01_cbAccountSegment_Input")
cc.clear()
cc.send_keys("1000")
bu = driver.find_element(By.ID, "ctl00_MainContent_ucAccFilter_accountSegmentsDataList_ctl02_cbAccountSegment_Input")
bu.clear()
bu.send_keys("0000100009")
apply = driver.find_element(By.LINK_TEXT, "Apply")
apply.click()
time.sleep(10)
# Close the browser window
driver.quit()
