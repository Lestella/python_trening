from model.group import Group
from random import randrange


def test_edit_group_name(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="Name For Edit"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Edited group1")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    assert len(old_groups) == app.group.count_groups()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

