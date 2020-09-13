from model.group import Group
import random


def test_edit_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Name For Edit"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group_data = Group(name="Edited Group")
    app.group.edit_group_by_id(group.id, new_group_data)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    group.name = new_group_data.name
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

