from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.test_edit_first_group(Group(name="Group 2", header="aaaaa", footer="bbbbb"))
    app.session.logout()
