import re
from random import randrange
from model.contact import Contact


def test_main_contact_info_on_home_page(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    # main info
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    # phones homepage
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(
        contact_from_edit_page)
    # phones from view page
    assert contact_from_view_page.all_phones_from_view_page == merge_phones_like_on_home_page(
        contact_from_edit_page)
    # emails
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(
        contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.email_1, contact.email_2, contact.email_3]))))


def test_contact_db_info_matches_ui(app, db):
    ui_list = app.contact.get_contact_list()
    print("ui list", ui_list)
    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip(),
                       address=contact.address.strip(), all_phones_from_home_page=merge_phones_like_on_home_page(contact),
                       all_emails_from_home_page=merge_emails_like_on_home_page(contact))
    db_list = map(clean, db.get_contact_list())
    print("db list", db_list)
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)