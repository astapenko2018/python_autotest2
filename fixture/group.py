from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        self.app.driver.find_element(By.LINK_TEXT, "groups").click()


    def create(self, group):
        self.open_groups_page()
        # init group creation
        self.app.driver.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        # submit
        self.app.driver.find_element(By.NAME, "submit").click()
        self.return_groups()

    def fill_group_form(self, group):
        if group.name is not None:
            self.app.driver.find_element(By.NAME, "group_name").click()
            #self.app.driver.find_element(By.NAME, "group_name").clear()
            self.app.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.app.driver.find_element(By.NAME, "group_header").click()
        self.app.driver.find_element(By.NAME, "group_header").send_keys(group.header)
        self.app.driver.find_element(By.NAME, "group_footer").click()
        self.app.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)

    def delete_first_group(self):
        self.open_groups_page()
        self.select_first_group()
        # submit deletion
        self.app.driver.find_element_by_name("delete").click()
        self.return_groups()

    def select_first_group(self):
        self.app.driver.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_data):
        self.open_groups_page()
        self.select_first_group()
        # open modification form
        self.app.driver.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        self.app.driver.find_element_by_name("update").click()
        self.return_groups()


    def return_groups(self):
        self.app.driver.find_element(By.LINK_TEXT, "groups").click()