from model.contact import Contact


def test_edit_first_contact_firstname(app):
    app.contact.test_edit_first_contact(
        Contact(firstname="Name_new_1"))


def test_edit_first_contact_middlename(app):
    app.contact.test_edit_first_contact(
        Contact(middlename="Middle Name_new_2"))
