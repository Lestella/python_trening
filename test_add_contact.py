# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from contact import Contact

import unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_new_contact(wd, Contact(firstname="Name", middlename="Middle Name", lastname="Last Name",
                           nickname="Nickname", title="Title", company="Company", address="Address",
                           hometelephone="Hometelephone", mobiletelephone="mobiletelephone",
                           worktelephone="worktelephone", fax="fax", email_1="email1", email_2="email2", email_3="email3",
                           homepage="homepage", birthday="2", birthmonth="August", birthyear="1900", annday="2",
                           annmonth="March", annyear="1900", address_2="address 2", home_2="home 2", notes_2="notes 2"))


        self.logout(wd)

    #def test_add_empty_contact(self):
        #wd = self.wd
        #self.open_home_page(wd)
        #self.login(wd, username="admin", password="secret")
        #self.create_new_contact(wd, Contact(firstname="", middlename="", lastname="",
                                            #nickname="", title="", company="", address="",
                                            #hometelephone="", mobiletelephone="",
                                            #worktelephone="", fax="", email_1="",
                                            #email_2="", email_3="",
                                            #homepage="", birthday="", birthmonth="", birthyear="",
                                            #annday="",
                                            #annmonth="", annyear="", address_2="", home_2="",
                                            #notes_2=""))

        #self.logout(wd)

    def create_new_contact(self, wd, contact):
        # add new contact
        wd.find_element_by_link_text("add new").click()
        # name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # contacts
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.hometelephone)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobiletelephone)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.worktelephone)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email_1)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email_2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email_3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # date
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birthday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birthmonth)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birthyear)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.annday)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.annmonth)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.annyear)
        wd.find_element_by_name("new_group").click()
        # additional information
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address_2)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.home_2)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes_2)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def logout(self, wd):
        wd.find_element_by_link_text("home page").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://192.168.64.2/addressbook/index.php")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
