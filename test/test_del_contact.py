from model.contact import Contact


def test_del_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.create_new_contact(Contact(firstname="For Delete"))
    app.contact.test_delete_first_contact()
