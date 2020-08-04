from selenium.webdriver.support.select import Select


class ContactHelper:

    def __init__(self, rty):
        self.app = rty

    def create_new_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # add new contact
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

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

    def test_edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("(//img[@alt='Edit'])").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()

    def test_delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def count_contacts(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def clear_all_contacts(self):
        wd = self.app.wd
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
