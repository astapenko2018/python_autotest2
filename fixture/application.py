from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.driver.implicitly_wait(60)

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")
        self.driver.set_window_size(1048, 1040)

    # def open_groups_page(self):
    #     self.driver.find_element(By.LINK_TEXT, "groups").click()
    #     self.driver.find_element(By.NAME, "new").click()
    #
    # def create_group(self, group):
    #     self.open_groups_page()
    #     self.driver.find_element(By.NAME, "group_name").click()
    #     self.driver.find_element(By.NAME, "group_name").send_keys(group.name)
    #     self.driver.find_element(By.NAME, "group_header").click()
    #     self.driver.find_element(By.NAME, "group_header").send_keys(group.header)
    #     self.driver.find_element(By.NAME, "group_footer").click()
    #     self.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
    #     self.driver.find_element(By.NAME, "submit").click()
    #     self.return_groups()
    #
    # def return_groups(self):
    #     self.driver.find_element(By.LINK_TEXT, "groups").click()

    def destroy(self):
        self.driver.quit()
