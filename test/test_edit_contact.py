from model.contact import Contact


def test_edit_first_contact_firstname(app):
    if app.contact.count_contacts() == 0:
        app.contact.create_new_contact(Contact(firstname="For Delete"))
    app.contact.test_edit_first_contact(
        Contact(firstname="Name_new_1"))


def test_edit_first_contact_middlename(app):
    if app.contact.count_contacts() == 0:
        app.contact.create_new_contact(Contact(middlename="For Delete"))
    app.contact.test_edit_first_contact(
        Contact(middlename="Middle Name_new_2"))
