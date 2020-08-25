from model.contact import Contact


def test_edit_first_contact_firstname(app):
    if app.contact.count_contacts() == 0:
        app.contact.create_new_contact(Contact(firstname="For Edit"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Edited Firstname")
    contact.id = old_contacts[0].id
    contact.firstname = old_contacts[0].firstname
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_edit_first_contact_middlename(app):
#     if app.contact.count_contacts() == 0:
#         app.contact.create_new_contact(Contact(middlename="For Edit"))
#     app.contact.edit_first_contact(
#         Contact(middlename="Middle Name_new_2"))
