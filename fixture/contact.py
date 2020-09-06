from selenium.webdriver.support.select import Select
from model.contact import Contact

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
        self.change_field_value("home", contact.hometelephone)
        self.change_field_value("mobile", contact.mobiletelephone)
        self.change_field_value("work", contact.worktelephone)
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
        self.change_field_value("phone2", contact.home_2)
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

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
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

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[./td]"):
                id = element.find_element_by_name("selected[]").get_attribute("id")
                firstname = element.find_elements_by_tag_name("td")[2].text
                lastname = element.find_elements_by_tag_name("td")[1].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname))
        return list(self.contact_cache)
