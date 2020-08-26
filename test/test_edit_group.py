from model.group import Group
from random import randrange


def test_edit_first_group_name(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="Name For Edit"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    print(index)
    group = Group(name="New group")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(group, index)
    assert len(old_groups) == app.group.count_groups()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_edit_first_group_header(app):
#     if app.group.count_groups() == 0:
#         app.group.create(Group(header="Header For Edit"))
#     old_groups = app.group.get_group_list()
#     group = Group(header="New header")
#     group.id = old_groups[0].id
#     app.group.edit_first_group(group)
#     assert len(old_groups) == app.group.count_groups()
#     new_groups = app.group.get_group_list()
#     old_groups[0] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

