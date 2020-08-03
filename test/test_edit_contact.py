from model.contact import Contact


def test_edit_first_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.test_edit_first_contact(
        Contact(firstname="Name_new_1"))
    app.session.logout()

def test_edit_first_contact_middlename(app):
        app.session.login(username="admin", password="secret")
        app.contact.test_edit_first_contact(
            Contact(middlename="Middle Name_new_2"))
        app.session.logout()
