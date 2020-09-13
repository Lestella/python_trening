from model.contact import Contact
import random


def test_edit_contact(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.contact.create_new_contact(Contact(firstname="Firstname for edit", lastname="Lastname for edit"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    new_contact_data = Contact(firstname="Edited Firstname")
    app.contact.edit_contact_by_id(contact.id, new_contact_data)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    contact.firstname = new_contact_data.firstname
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
