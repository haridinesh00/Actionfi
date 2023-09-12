import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime, timedelta
from retrying import retry
from selenium.common.exceptions import NoSuchElementException


class SeleniumAutomation:
    def __init__(self):
        self.driver = self.chrome_settings()

    @staticmethod
    def chrome_settings():
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')
            prefs = {"download.default_directory": "C:\\Users\\harid\\PycharmProjects\\SeleniumBegin\\SeleniumSessions"}
            options.add_experimental_option("prefs", prefs)
            driver = webdriver.Chrome(options=options)
            return driver
        except Exception as e:
            raise e

    def switch_frame(self, frm):
        try:
            self.driver.switch_to.frame(self.driver.find_element(By.ID, frm))
        except Exception as e:
            raise e

    def date_select_switch(self, no_day):
        try:
            self.driver.switch_to.frame(self.driver.find_element(By.ID, "ifrmDateTimePicker"))
            # Calculate yesterday's date
            yesterday = datetime.now() - timedelta(days=no_day)
            desired_date = str(int(yesterday.strftime("%d")))
            self.driver.implicitly_wait(5)
            self.driver.find_element(By.XPATH,
                                     f"(//div[@class='dhtmlxcalendar_label'][normalize-space()="
                                     f"'{desired_date}'])[1]").click()
        except Exception as e:
            raise e

    def go_to_page(self):
        try:
            self.driver.maximize_window()
            self.driver.get("https://ops07.lower.trintech.com")
            self.driver.implicitly_wait(5)
        except Exception as e:
            raise e

    @retry(delay=5, tries=6)
    def login(self):
        try:
            username = self.driver.find_element(By.XPATH, "//input[@id='UseriName']")
            username.clear()
            username.send_keys("sa")
            password = self.driver.find_element(By.XPATH, "//input[@id='Password']")
            password.clear()
            password.send_keys("Trintech1!")
            submit = self.driver.find_element(By.XPATH, "//input[@value='Sign In']")
            submit.click()
            time.sleep(5)
            self.driver.implicitly_wait(10)
            return True
        except Exception as e:
            raise e

    def certify_sidebar_reporting(self):
        try:
            certification = self.driver.find_element(By.XPATH, "//a[@id='tb_cert_tab']")
            certification.click()
            time.sleep(5)
            self.driver.implicitly_wait(5)
            side_bar_toggle = self.driver.find_element(By.XPATH,
                                                       "//button[@class='btn btn-sidebar-toggle mt-4 ng-tns-c55-0']")
            side_bar_toggle.click()
            time.sleep(5)
            self.driver.implicitly_wait(10)
            analysis = self.driver.find_element(By.XPATH, "//span[normalize-space()='Analysis']")
            analysis.click()
            reporting = self.driver.find_element(By.XPATH, "//a[normalize-space()='Reporting']")
            reporting.click()
            self.driver.implicitly_wait(10)
        except Exception as e:
            raise e

    def dropdown_action(self, visible_text, element_id):
        try:
            dropdown_element = self.driver.find_element(By.ID, element_id)
            dropdown = Select(dropdown_element)
            dropdown.select_by_visible_text(visible_text)
            time.sleep(2)
        except Exception as e:
            raise e

    def filter_report(self, field, condition):
        try:
            filter_tool = self.driver.find_element(By.ID, "FilterToolBarImgTd")
            filter_tool.click()
            first_filter_field = self.driver.find_element(By.ID, "lstFilterFieldName0")
            first_filter_field.click()
            self.driver.implicitly_wait(5)
            self.driver.find_element(By.XPATH, f"(//span[contains(text(), '{field}')])[6]").click()
            self.driver.implicitly_wait(10)
            if condition:
                self.dropdown_action("Is", "lstFilterCriteria0")
                date_input = self.driver.find_element(By.ID, "CalendarPicker10")
                date_input.click()
                self.date_select_switch(0)
            else:
                self.dropdown_action("Between", "lstFilterCriteria0")
                date_input = self.driver.find_element(By.ID, "CalendarPicker10")
                date_input.click()
                self.date_select_switch(1)
                self.driver.switch_to.default_content()
                self.switch_frame("ReportListFrm")
                date_input = self.driver.find_element(By.ID, "CalendarPicker20")
                date_input.click()
                self.date_select_switch(0)
                time.sleep(3)
        except Exception as e:
            raise e

    def remove_add_filters(self, fil_col):
        try:
            self.driver.find_element(By.ID, fil_col).click()
            time.sleep(0.5)
        except Exception as e:
            raise e

    def journal_entry_nav(self):
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
            journal = self.driver.find_element(By.XPATH, "//span[normalize-space()='Journal Entry Reports']")
            journal.click()
            self.driver.implicitly_wait(10)
            # Switch to the iframe
            self.switch_frame("ReportListFrm")
        except Exception as e:
            raise e

    def jed_enhanced(self):
        try:
            self.driver.find_element(By.XPATH, "//input[@value='499C9C1A-2F10-F15A-8164-7E1F9A052871']").click()
            self.driver.implicitly_wait(5)
            self.driver.find_element(By.ID, "FishEyeToolbarOuterDiv_Run_Img").click()
            time.sleep(3)
        except Exception as e:
            raise e

    def download_btn(self):
        try:
            self.driver.find_element(By.ID, "btnPreview").click()
            time.sleep(10)
        except Exception as e:
            raise e


def run():
    automation = SeleniumAutomation()
    automation.go_to_page()
    automation.login()
    automation.certify_sidebar_reporting()
    automation.journal_entry_nav()
    automation.jed_enhanced()
    # Available formats: HTML, ACROBAT PDF, MS EXCEL, COMMA SEPARATED, TEXT.
    FORMAT = 'TEXT'
    automation.dropdown_action(FORMAT, "lstFormat")
    automation.filter_report("Datecreated", False)
    automation.driver.switch_to.default_content()
    automation.switch_frame("ReportListFrm")
    automation.remove_add_filters("colRemoveFilter1")
    automation.remove_add_filters("colRemoveFilter2")
    automation.download_btn()
    automation.driver.quit()


if __name__ == "__main__":
    run()
