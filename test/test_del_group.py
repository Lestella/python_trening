from model.group import Group
from random import randrange


def test_del_group(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="Name For Delete"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    # print(index)
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count_groups()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups

#
# def test_del_first_group(app):
#     if app.group.count_groups() == 0:
#         app.group.create(Group(name="Name For Delete"))
#     old_groups = app.group.get_group_list()
#     app.group.delete_first_group()
#     assert len(old_groups) - 1 == app.group.count_groups()
#     new_groups = app.group.get_group_list()
#     old_groups[0:1] = []
#     assert old_groups == new_groups