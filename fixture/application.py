from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.maximize_window()
        self.wd.implicity_wait(60)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://192.168.64.2/addressbook/index.php")

    def destroy(self):
        self.wd.quit()
