# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
        app.open_home_page()
        app.login(username="admin", password="secret")
        app.create_new_contact(Contact(firstname="Name", middlename="Middle Name", lastname="Last Name",
                                        nickname="Nickname", title="Title", company="Company", address="Address",
                                        hometelephone="Hometelephone", mobiletelephone="mobiletelephone",
                                        worktelephone="worktelephone", fax="fax", email_1="email1", email_2="email2",
                                        email_3="email3",
                                        homepage="homepage", birthday="2", birthmonth="August", birthyear="1900",
                                        annday="2",
                                        annmonth="March", annyear="1900", address_2="address 2", home_2="home 2",
                                        notes_2="notes 2"))

        app.logout()


if __name__ == "__main__":
    unittest.main()
