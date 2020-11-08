# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random


def test_delete_contact_from_group(app, orm):
    if len(app.contact.get_contact_list()) == 0:
        app.contact.create_new_contact(Contact(firstname="For Add to Group", lastname="For Add to Group"))
    all_contacts = orm.get_contact_list()
    if len(app.group.get_group_list()) == 0:
        app.group.create(Group(name="For Add a Contact", header="For Add a Contact"))
    all_groups = orm.get_group_list()
    contact = random.choice(all_contacts)
    group = random.choice(all_groups)
    app.contact.remove_contact_from_group(group.id, contact.id)
    contacts_not_in_group = orm.get_contacts_not_in_group(group)
    print("contacts in group", contacts_not_in_group)
    assert contact in contacts_not_in_group