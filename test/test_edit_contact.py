from model.contact import Contact
from random import randrange


def test_edit_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.create_new_contact(Contact(firstname="Firstname for edit", lastname="Lastname for edit"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Edited Firstname")
    contact.id = old_contacts[index].id
    contact.lastname = old_contacts[index].lastname
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
