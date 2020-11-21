from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given('a contact list', target_fixture="contact_list")
def contact_list(db):
    return db.get_contact_list()


@given('a contact with <firstname>, <lastname>, <homephone>, <mobilephone>, <workphone>, <secondaryphone>, <address>, <email_1>, <email_2>, <email_3>', target_fixture="new_contact")
def new_contact(firstname, lastname, homephone, mobilephone, workphone, secondaryphone, address, email_1, email_2, email_3):
    return Contact(firstname=firstname, lastname=lastname, homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone, address=address, email_1=email_1, email_2=email_2, email_3=email_3)


@when('I add a the contact the list')
def add_new_contact(app, new_contact):
    app.contact.create_new_contact(new_contact)


@then('the new contact list is equal the old list with the added contact')
def verify_new_contact(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@given('a random contact', target_fixture="random_contact")
def random_contact(contact_list):
    return random.choice(contact_list)


@given('a contact with the new data', target_fixture="edit_contact_data")
def edit_contact_data():
    return Contact(firstname="edited firstname", lastname="edited lastname")


@when('I edit contact data')
def edit_contact(app, random_contact, edit_contact_data):
    app.contact.edit_contact_by_id(random_contact.id, edit_contact_data)


@then('the new contact list is equal the old list with the edited contact')
def verify_edited_contact(db, contact_list, edit_contact_data, random_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    random_contact.firstname = edit_contact_data.firstname
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@when('I delete contact')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@then('the new contact list is equal the old list with the deleted contact')
def verify_edited_contact(db, contact_list, random_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(random_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



