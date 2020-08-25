from model.contact import Contact
import time


def test_del_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.create_new_contact(Contact(firstname="For Delete", lastname="For delete"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    time.sleep(3)
    assert len(old_contacts) - 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
