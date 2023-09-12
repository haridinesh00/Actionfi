import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def ad():
    skip = driver.find_element(By.XPATH, "//button[@class='ytp-ad-skip-button ytp-button']")
    return skip


driver = webdriver.Chrome()

driver.get('https://www.youtube.com/')
a = driver.find_element(By.NAME, "search_query")
a.send_keys("asmr")
a.submit()
driver.implicitly_wait(5)
first_result = driver.find_element(By.CSS_SELECTOR, "a#video-title")
first_result.click()
time.sleep(10)
driver.implicitly_wait(30)
print(ad().is_displayed())
# if ad().is_displayed():
#     ad().click()
# pause = driver.find_element(By.XPATH, "//button[@title='Pause (k)']")
# pause.click()
# time.sleep(2)
# pause.click()
time.sleep(20)
# driver.find_element(By.ID, "video-title").click()
# time.sleep(10)
driver.close()
