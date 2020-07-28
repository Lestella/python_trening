from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_new_contact(
        Contact(firstname="Name_new", middlename="Middle Name_new", lastname="Last Name__new",
                nickname="Nickname_new", title="Title_new", company="Company_new", address="Address_new",
                hometelephone="Hometelephone_new", mobiletelephone="mobiletelephone_new",
                worktelephone="worktelephone_new", fax="fax_new", email_1="email1_new", email_2="email2_new",
                email_3="email3_new",
                homepage="homepage_new", birthday="9", birthmonth="July", birthyear="1908",
                annday="5",
                annmonth="September", annyear="1990", address_2="address 2_new", home_2="home 2_new",
                notes_2="notes 2_new"))

    app.session.logout()
