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


    def destroy(self):
        self.driver.quit()
