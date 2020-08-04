from model.group import Group


def test_edit_first_group_name(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="Name For Delete"))
    app.group.edit_first_group(Group(name="New group"))


def test_edit_first_group_header(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(header="Header For Delete"))
    app.group.edit_first_group(Group(header="New header"))
