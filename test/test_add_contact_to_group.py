# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(Contact(firstname="For Add to Group", lastname="For Add to Group"))
    all_contacts = db.get_contact_list()
    all_groups = db.get_group_list()
    contact = random.choice(all_contacts)
    group = random.choice(all_groups)
    app.contact.add_contact_to_group_by_id(contact.id, group.id, group.name)


