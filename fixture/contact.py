from selenium.webdriver.support.select import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, rty):
        self.app = rty

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home").click()

    def create_new_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # add new contact
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email_1)
        self.change_field_value("email2", contact.email_2)
        self.change_field_value("email3", contact.email_3)
        self.change_field_value("homepage", contact.homepage)
        self.change_select_date("bday", contact.birthday)
        self.change_select_date("bmonth", contact.birthmonth)
        self.change_field_value("byear", contact.birthyear)
        self.change_select_date("aday", contact.annday)
        self.change_select_date("amonth", contact.annmonth)
        self.change_field_value("ayear", contact.annyear)
        self.change_field_value("address2", contact.address_2)
        self.change_field_value("phone2", contact.secondaryphone)
        self.change_field_value("notes", contact.notes_2)

    def change_select_date(self, field_name, date):
        wd = self.app.wd
        if date is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(date)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("(//img[@alt='Edit'])")[index].click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.open_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_css_selector("a[href='edit.php?id=%s" % id).click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.open_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s" % id).click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_elements_by_css_selector("div.msgbox")
        self.open_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_elements_by_css_selector("div.msgbox")
        self.open_home_page()
        self.contact_cache = None

    def count_contacts(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def clear_all_contacts(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    contact_cache = None

    # def get_contact_list(self):
    #     if self.contact_cache is None:
    #         wd = self.app.wd
    #         self.app.open_home_page()
    #         self.contact_cache = []
    #         for element in wd.find_elements_by_xpath("//tr[./td]"):
    #             id = element.find_element_by_name("selected[]").get_attribute("id")
    #             firstname = element.find_elements_by_tag_name("td")[2].text
    #             lastname = element.find_elements_by_tag_name("td")[1].text
    #             self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname))
    #     return list(self.contact_cache)

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                contact = Contact(firstname=firstname, lastname=lastname, address=address,
                                  id=id,
                                  all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails)
                self.contact_cache.append(contact)
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("a[href='edit.php?id=%s" % id).click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("a[href='view.php?id=%s" % id).click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").text
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, address=address,
                       id=id,
                       homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone,
                       email_1=email1, email_2=email2, email_3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        print(text)
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        all_phones_view_page = "\n".join((homephone, mobilephone, workphone, secondaryphone))
        return Contact(all_phones_from_view_page=all_phones_view_page)

    def add_contact_to_group_by_id(self, contact_id, group_id, group_name):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_xpath("(//option[@value=%s])[2]" % group_id).click()
        wd.find_element_by_name("add").click()
        wd.find_element_by_link_text('group page "%s"' % group_name).click()

    def remove_contact_from_group(self, group_id, contact_id):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_name("group").click()
        wd.find_element_by_xpath("//option[@value=%s]" % group_id).click()
        # wd.find_element_by_xpath("//option[@value=422]").click()
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("remove").click()
        wd.find_element_by_css_selector("div.msgbox")