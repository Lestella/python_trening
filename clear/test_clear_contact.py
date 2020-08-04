def test_clear_contact(app):
    while 0 != app.contact.count_contacts():
        app.contact.clear_all_contacts()
    else:
        print("Contact list is already empty")
