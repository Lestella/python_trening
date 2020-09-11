import re
from random import randrange


def test_emails_on_home_page(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    print("index", index)
    contact_from_home_page = app.contact.get_contact_list()[index]
    print("home", contact_from_home_page.all_emails_from_home_page)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    print("edit", merge_emails_like_on_home_page(contact_from_edit_page))
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(
        contact_from_edit_page)


def clear(s):
    return re.sub("[() ]", "", s)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.email_1, contact.email_2, contact.email_3]))))