# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_new_contact(Contact(firstname="Name1", middlename="Middle Name", lastname="Last Name",
                                           nickname="Nickname", title="Title", company="Company", address="Address",
                                           hometelephone="Hometelephone", mobiletelephone="mobiletelephone",
                                           worktelephone="worktelephone", fax="fax", email_1="email1", email_2="email2",
                                           email_3="email3",
                                           homepage="homepage", birthday="2", birthmonth="August", birthyear="1900",
                                           annday="2",
                                           annmonth="March", annyear="1900", address_2="address 2", home_2="home 2",
                                           notes_2="notes 2"))

    app.session.logout()
