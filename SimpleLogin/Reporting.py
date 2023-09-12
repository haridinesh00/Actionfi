import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime, timedelta


def chrome_settings():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    prefs = {"download.default_directory": "C:\\Users\\harid\\PycharmProjects\\SeleniumBegin\\SeleniumSessions"}
    options.add_experimental_option("prefs", prefs)
    drive = webdriver.Chrome(options=options)
    return drive


def switch_frame(frm):
    driver.switch_to.frame(driver.find_element(By.ID, frm))


def date_select_switch():
    driver.switch_to.frame(driver.find_element(By.ID, "ifrmDateTimePicker"))
    # Calculate yesterday's date
    yes = datetime.now()
    desired_dat = str(int(yes.strftime("%d")))
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,
                        f"(//div[@class='dhtmlxcalendar_label'][normalize-space()='{desired_dat}'])[1]").click()


def go_to_page():
    driver.maximize_window()
    driver.get("https://ops07.lower.trintech.com")
    driver.implicitly_wait(5)  # Waits 5 seconds to find the sign in button,


def login():
    username = driver.find_element(By.NAME, "UserName")
    username.clear()
    username.send_keys("sa")
    password = driver.find_element(By.NAME, "Password")
    password.clear()
    password.send_keys("Trintech1!")
    submit = driver.find_element(By.CLASS_NAME, "loginButton")
    submit.click()
    time.sleep(5)
    driver.implicitly_wait(10)


def certify_sidebar_reporting():
    certification = driver.find_element(By.LINK_TEXT, "Certification")
    certification.click()
    time.sleep(5)
    driver.implicitly_wait(5)
    side_bar_toggle = driver.find_element(By.CLASS_NAME, "btn-sidebar-toggle")
    side_bar_toggle.click()
    time.sleep(5)
    driver.implicitly_wait(10)
    analysis = driver.find_element(By.LINK_TEXT, "Analysis")
    analysis.click()
    reporting = driver.find_element(By.LINK_TEXT, "Reporting")
    reporting.click()
    driver.implicitly_wait(10)


def dropdown_action(visible_text, element_id):
    dropdown_element = driver.find_element(By.ID, element_id)
    dropdown = Select(dropdown_element)
    dropdown.select_by_visible_text(visible_text)
    time.sleep(2)


def filter_report(field, condition):
    filter_tool = driver.find_element(By.ID, "FilterToolBarImgTd")
    filter_tool.click()
    first_filter_field = driver.find_element(By.ID, "lstFilterFieldName0")
    first_filter_field.click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, f"(//span[contains(text(), '{field}')])[6]").click()
    driver.implicitly_wait(10)
    if condition:
        dropdown_action("Is", "lstFilterCriteria0")
        date_input = driver.find_element(By.ID, "CalendarPicker10")
        date_input.click()
        date_select_switch()

    else:
        dropdown_action("Between", "lstFilterCriteria0")
        date_input = driver.find_element(By.ID, "CalendarPicker10")
        date_input.click()
        driver.switch_to.frame(driver.find_element(By.ID, "ifrmDateTimePicker"))
        # Calculate yesterday's date
        yesterday = datetime.now() - timedelta(days=1)
        desired_date = str(int(yesterday.strftime("%d")))
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH,
                            f"(//div[@class='dhtmlxcalendar_label'][normalize-space()='{desired_date}'])[1]").click()
        driver.switch_to.default_content()
        switch_frame("ReportListFrm")
        date_input = driver.find_element(By.ID, "CalendarPicker20")
        date_input.click()
        date_select_switch()
        time.sleep(3)


def remove_add_filters(fil_col):
    driver.find_element(By.ID, fil_col).click()
    time.sleep(0.5)


def journal_entry_nav():
    driver.switch_to.window(driver.window_handles[1])
    journal = driver.find_element(By.LINK_TEXT, "Journal Entry Reports")
    journal.click()
    driver.implicitly_wait(10)
    # Switch to the iframe
    switch_frame("ReportListFrm")


def jed_enhanced():
    driver.find_element(By.XPATH, "//input[@value='499C9C1A-2F10-F15A-8164-7E1F9A052871']").click()
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "FishEyeToolbarOuterDiv_Run_Img").click()
    time.sleep(3)


def download_btn():
    driver.find_element(By.ID, "btnPreview").click()
    time.sleep(10)


driver = chrome_settings()
go_to_page()
login()
certify_sidebar_reporting()
journal_entry_nav()
jed_enhanced()
# Available formats: HTML, ACROBAT PDF, MS EXCEL, COMMA SEPARATED, TEXT.
FORMAT = 'TEXT'
dropdown_action(FORMAT, "lstFormat")
filter_report("Datecreated", "False")
driver.switch_to.default_content()
switch_frame("ReportListFrm")
remove_add_filters("colRemoveFilter1")
remove_add_filters("colRemoveFilter2")
download_btn()
driver.quit()
