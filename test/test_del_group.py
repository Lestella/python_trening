from model.group import Group


def test_del_group(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="Name For Delete"))
    app.group.test_delete_first_group()
