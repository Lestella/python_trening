from model.contact import Contact
from random import randrange


def test_edit_first_contact_firstname(app):
    if app.contact.count_contacts() == 0:
        app.contact.create_new_contact(Contact(firstname="For Edit"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Edited Firstname")
    contact.id = old_contacts[index].id
    contact.firstname = old_contacts[0].firstname
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_edit_first_contact_lastname(app):
#     if app.contact.count_contacts() == 0:
#         app.contact.create_new_contact(Contact(lastname="For Edit"))
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(lastname="Edited Lastname")
#     contact.id = old_contacts[0].id
#     contact.firstname = old_contacts[0].firstname
#     app.contact.edit_first_contact(contact)
#     assert len(old_contacts) == app.contact.count_contacts()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts[0] = contact
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
